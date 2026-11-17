# QA checklist and what was verified

## Look at the stills (both formats)
- Nothing is cut off at the edges. Tall: keep important content out of the bottom 330 px (platform UI) and top 110 px.
- No text overlaps other text. Wrapped headlines fit above the accent rule.
- Smallest text is readable on a phone (tall) and on a laptop (wide).
- One accent color highlights one thing per beat.
- Map: the highlighted countries are the ones named in the narration.
- Numbers match the sources.
- The last still of each beat shows everything the narration mentions.

## Then watch the render once with sound
- Audio starts about 0.3 s after each beat begins. Narration never gets cut at a beat end.
- Wipes do not hide the first words of a headline.

## What was verified (EffectCraft 0.24.1, Linux x86_64, headless CLI, author's sandbox)
- check, build, stills and full mp4 renders for the starter spec (6 beats, ~49 s, includes the touchgrid mechanism
  diagram and 6 cited points) in both formats: 1920x1080 and 1080x1920, h264 + aac, Piper narration.
- Frames pulled from the rendered mp4 show the grid drawing on, the finger ripple, the located point, wipes and captions.
- All other beat types built and inspected as stills in both formats (examples/data-demo.spec.json, illustrative data).
- `check` rejects unsourced fact beats and unsourced numbers/dates in any beat type (tested on the demo specs).
- One 49 s render took about 75 s per format on that machine (environment specific).

## Not verified
- macOS and Windows runs (the CLI is documented there, but not run by the author). Expect only path differences.
- macOS `say` and espeak-ng voice generation.
- Videos longer than about one minute, 4K output, and the `music` option.
- Captions are not word-aligned. Map shapes are generalized. Text height is estimated, so long text can still
  crowd: inspect every still.
- EffectCraft is alpha software; its own README says it is not yet recommended for production client work.
  Check renders before publishing.
