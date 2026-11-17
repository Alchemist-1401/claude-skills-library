# Narration

`ecx.py voice spec.json` writes `vo/<beat id>.wav` for every beat with a `vo`. Existing files are kept unless you
pass `--force`, so you can replace any beat with your own recording.

| engine | cost | quality | notes |
|---|---|---|---|
| say | free, built into macOS | good with Siri/Premium voices if installed | `voice.voice` = name, e.g. "Samantha". Check `say -v '?'` |
| piper | free, offline | good | Install separately (`pip install piper-tts`), download a voice model .onnx plus its .json, set `ECX_PIPER_MODEL` |
| espeak-ng | free | robotic | last resort |
| your own voice | free | best | record per beat, save as 16-bit WAV |

Licence cautions (not legal advice): Piper's code and each voice model have their own licences. Check the model card
before publishing commercially. Nothing from Piper is included in this package. Apple's system voices have usage
terms too; read them before using on a monetized channel.

Timing comes from the real audio length (wav read directly; other formats need `ffprobe`). Without audio the length is
estimated at 2.5 words per second.
