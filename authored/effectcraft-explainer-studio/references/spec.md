# Beat sheet reference

Top level fields (all optional except `beats`):
- `name`: used in file names.
- `style`: `paper` | `ink` | `signal`. `colors`: override any of bg, fg, mute, panel, accent, accent2, grid (6 digit hex).
- `format`: `wide` | `tall` | `both`. `fps`: default 30.
- `captions`: `tall` (default) | `both` | `off`. Evenly spread, not word-aligned.
- `voice`: `{"engine":"auto|say|piper|espeak-ng","voice":"name or model path"}`.
- `music`: path (relative to the spec) of music you have the right to use, `music_db`: default -22.
- `fonts`: override `head`, `body`, `bold`, `mono` as `["Family","Style"]`. Families must exist on the machine.

Every beat: `id` (unique), `type`, `tag` (small chapter label), `vo` (narration), optional `dur` (minimum seconds),
`title`, `source` (string or `{"label","url"}`, or `"none"`), `data`.

Beat length = the longest of: `dur`, the type's minimum, narration length + 1 second.

| type | data | notes |
|---|---|---|
| hook | kicker, headline, sub | headline supports `*emphasis*` |
| kinetic | lines: [text] | one line at a time, `*emphasis*` |
| stat | value, prefix, suffix, decimals, label, context | number counts up |
| bars | items [{label,value}], unit, prefix, max, highlight | 2-4 items; first is highlighted |
| line | points [[x label, value]], unit, min, max, annotations [{at: index, text}] | draws on, pulsing end dot |
| map | highlight [ISO3 codes], pins [{lon,lat,label}], routes [{from:[lon,lat],to:[lon,lat]}], bbox [lon0,lat0,lon1,lat1] | Natural Earth 1:110m countries; auto-framing; world view uses Equal Earth, regions use plate carree |
| steps | steps [{title,text}] | 2-5 |
| timeline | events [{when,text}] | 2-6 |
| compare | left/right {label,value,note}, verdict | two big panels |
| quote | text, who | |
| touchgrid | cols, rows, touch [col,row], labels [3 strings] | animated mechanism diagram: sensor grid, finger ripple, signal change, found point; label it "simplified" |
| outro | takeaway, cta, show_sources | auto-lists sources |
| raw | jsx_file | custom EffectCraft script, variables T0 T1 W H |

`source` is required on: stat, bars, line, map, compare, timeline, and on any beat whose text has numbers or dates. `check` verifies presence only; you verify truth. `"source":"none"` is only for questions and pure explanation.

Map notes: ISO3 codes follow Natural Earth (France is FRA, Norway NOR, Kosovo is KOS, Somaliland SOL). Country
shapes are generalized and not for border disputes. Say "approximate map" if borders matter.
