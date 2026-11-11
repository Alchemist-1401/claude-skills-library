#!/usr/bin/env python3
"""Usage: python3 prepare_library.py [--destination PATH]
Prepare reviewed skill sources in one NEW folder (default: ./library).
Requires Python 3.9+ standard library and internet. Downloads public source
archives at pinned commits, verifies each selected file's hash, and copies the
repo's own guides/references. Never executes upstream code or installs anything.
Existing destinations are refused. Failure removes only its own staging folder.
"""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, os, shutil, stat, tarfile, tempfile, urllib.request


def safe_path(value):
    path=PurePosixPath(value)
    if path.is_absolute() or '..' in path.parts or '\\' in value or not path.parts:
        raise ValueError('Unsafe relative path: '+value)
    return path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def prepare(root, destination, opener=urllib.request.urlopen):
    if destination.exists() or destination.is_symlink():
        raise ValueError('Destination already exists; nothing overwritten: '+str(destination))
    if not destination.parent.is_dir():
        raise ValueError('Destination parent must already exist')
    index=json.loads((root/'manifests/index.json').read_text())
    if index['format']!=2:
        raise ValueError('Unsupported manifest format')
    stage=Path(tempfile.mkdtemp(prefix='.claude-library-prepare-',dir=destination.parent))
    try:
        sources=[]
        for part in index['parts']:
            obj=json.loads((root/str(safe_path(part))).read_text())
            sources.extend(obj['sources'])
        for own in index['own_files']:
            path=safe_path(own['path']);data=(root/str(path)).read_bytes()
            if digest(data)!=own['sha256']:
                raise ValueError('Repository file differs from reviewed manifest: '+str(path))
            target=stage/str(path);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
        for source in sources:
            entry=str(safe_path(source['entry']))
            expected={str(safe_path(f['path'])):f for f in source['files']}
            if not expected:
                continue
            repo=source['repo'];commit=source['commit']
            if not repo or len(repo.split('/'))!=2 or not all(c.isalnum() or c in '/_-. ' for c in repo) or ' ' in repo:
                raise ValueError('Invalid repository identifier')
            if not commit or len(commit)!=40 or any(c not in '0123456789abcdef' for c in commit):
                raise ValueError('Invalid pinned commit')
            url='https://codeload.github.com/'+repo+'/tar.gz/'+commit
            print('Fetching pinned source: '+repo,flush=True)
            request=urllib.request.Request(url,headers={'User-Agent':'Claude-Library-Intake/1.0'})
            received=0;seen=set()
            with opener(request,timeout=120) as response, tarfile.open(fileobj=response,mode='r|gz') as archive:
                for member in archive:
                    pieces=PurePosixPath(member.name).parts
                    if len(pieces)<2:
                        continue
                    rel='/'.join(pieces[1:])
                    if rel not in expected:
                        continue
                    safe_path(rel)
                    if not member.isfile() or member.issym() or member.islnk():
                        raise ValueError('Expected regular source file: '+rel)
                    spec=expected[rel]
                    if rel in seen or member.size!=spec['bytes'] or member.size>30_000_000:
                        raise ValueError('Unexpected size or duplicate source: '+rel)
                    received+=member.size
                    if received>250_000_000:
                        raise ValueError('Source exceeds extraction limit')
                    handle=archive.extractfile(member)
                    if handle is None:
                        raise ValueError('Unreadable source file')
                    data=handle.read(spec['bytes']+1)
                    if len(data)!=spec['bytes'] or digest(data)!=spec['sha256']:
                        raise ValueError('Pinned source hash mismatch: '+repo+'/'+rel)
                    target=stage/'entries'/entry/'upstream'/rel
                    target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data);seen.add(rel)
            if seen!=set(expected):
                raise ValueError('Pinned source is incomplete: '+repo)
        (stage/'PREPARED.md').write_text('# Prepared library\n\nSources are pinned and verified. Nothing was enabled or executed. Read guides/ before using a skill. Authored files and projects/ are separate. Source-linked and incomplete entries remain so.\n')
        if destination.exists() or destination.is_symlink():
            raise ValueError('Destination appeared during preparation; preserving it')
        os.rename(stage,destination)
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def main():
    root=Path(__file__).resolve().parent
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination',type=Path,default=root/'library')
    args=parser.parse_args()
    # Resolve the parent but not a possibly existing final symlink.
    destination=args.destination.expanduser().absolute()
    prepare(root,destination)
    print('Prepared '+str(destination)+'. No dependencies installed or skills activated.')

if __name__=='__main__':
    main()
