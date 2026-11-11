#!/usr/bin/env python3
"""Usage: python3 prepare_library.py
Verify packages and expand into library/ beside this script. No installs, network,
upstream code execution or writes outside this repository. Existing library/ is
never overwritten. Requires Python 3.9+ standard library only.
"""
from pathlib import Path, PurePosixPath
import hashlib, io, json, os, shutil, stat, tempfile, zipfile

def main():
    root=Path(__file__).resolve().parent
    target=root/'library'
    if target.exists():
        raise SystemExit('library/ already exists. Keep it intact; compare a new prepared copy for updates.')
    manifest=json.loads((root/'manifest.json').read_text())
    stage=Path(tempfile.mkdtemp(prefix='.library-prepare-',dir=root))
    total=0
    try:
        for item in manifest['packages']:
            chunks=[]
            for part in item['parts']:
                rel=PurePosixPath(part['path'])
                if rel.is_absolute() or '..' in rel.parts:
                    raise ValueError('Unsafe package path')
                source=root/str(rel)
                if not source.exists():
                    candidates=list(source.parent.glob('*-'+source.name))
                    candidates=[p for p in candidates if p.name[:-len(source.name)-1].isdigit()]
                    if len(candidates)!=1:
                        raise ValueError('Missing or ambiguous package: '+str(rel))
                    source=candidates[0]
                data=source.read_bytes()
                if hashlib.sha256(data).hexdigest()!=part['sha256']:
                    raise ValueError('Package hash mismatch: '+str(rel))
                chunks.append(data)
            data=b''.join(chunks)
            if hashlib.sha256(data).hexdigest()!=item['zip_sha256']:
                raise ValueError('Archive hash mismatch: '+item['name'])
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                if len(z.infolist())!=item['files']:
                    raise ValueError('File count mismatch')
                for entry in z.infolist():
                    path=PurePosixPath(entry.filename)
                    if path.is_absolute() or '..' in path.parts or '\\' in entry.filename:
                        raise ValueError('Unsafe archive path')
                    if stat.S_ISLNK(entry.external_attr>>16):
                        raise ValueError('Archive symlink not allowed')
                    total+=entry.file_size
                    if total>500_000_000:
                        raise ValueError('Archive expansion exceeds 500 MB limit')
                    destination=stage/str(path)
                    if entry.is_dir():
                        destination.mkdir(parents=True,exist_ok=True)
                    else:
                        if destination.exists():
                            raise ValueError('Duplicate archive destination')
                        destination.parent.mkdir(parents=True,exist_ok=True)
                        with z.open(entry) as source, destination.open('wb') as output:
                            shutil.copyfileobj(source,output)
        if target.exists():
            raise ValueError('library/ appeared during preparation; leaving it intact')
        os.rename(stage,target)
        print('Prepared library/ in this repository. No skill activated and no dependencies installed.')
    finally:
        if stage.exists():
            shutil.rmtree(stage)

if __name__=='__main__':
    main()
