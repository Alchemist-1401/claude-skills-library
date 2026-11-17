# Notes on driving EffectCraft (from its public docs and our tests)

Official docs: https://github.com/storytold/effectcraft/blob/main/docs/agents.md

- Headless script run: `effectcraft-cli script build.jsx --save-as out.ecproj`. Inside a script,
  `app.run("command.id", {params})` runs any engine command and returns its result (for example `{layer: 12}`).
- List commands: `effectcraft-cli commands --filter text`. Params are checked, so wrong keys give a clear error.
- Colors must be 6 digit hex (`#aabbcc`) or `[r,g,b]`.
- Motion is driven by expressions set with `prop.setExpression` using comp time (`easeOut(time,t0,t1,a,b)`). Layers
  keep start at 0 and are trimmed with `layer.timing {in, out}`, so comp time is always the clock.
- Draw-on lines: add a shape path (`shape.newPath` with `layer`), add `layer.addShapeItem {kind:"trim"}`,
  then an expression on `contents/trim/end`.
- Counting numbers: expression on `text/sourceText` returning a string.
- Stills: `effectcraft-cli render-frame proj.ecproj --time 3 --out f.png`.
- Render: `effectcraft-cli render proj.ecproj --comp Main --out v.mp4 --format h264 --audio on`.
- Audio: `file.import {paths}` then `layer.addItem {item: "<file name>", time}`.
- Bundled fonts: Inter, Noto Serif, JetBrains Mono. `text.fonts` lists everything installed.
- Known: text box height is set by us from an estimate. If wrapped text collides, shorten it or lower the size
  in the spec rather than fighting the estimate.
