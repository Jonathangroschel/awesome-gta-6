# Contributing to Awesome GTA 6

Thanks for helping keep this the most accurate GTA 6 resource on GitHub. Everything you add is released under [CC0](LICENSE).

## The rules

1. **Accuracy beats speed.** Every fact needs a source link (an article, an official post or a video).
2. **Label what isn't confirmed.** Rumors go in the rumors tracker, marked unverified. Estimates (sales, map size) say "estimate".
3. **Link, don't re-host.** Never commit Rockstar trailers, screenshots, artwork or game files. Link to the official page instead.
4. **No leaked files, piracy or cheats for online play.** No "PC download", crack, mod-menu or exploit-for-money links. These get removed and may get the repo taken down.
5. **One link per line, one-line description**, in the format `- [Name](url): Description ending with a full stop.`
6. **No spoilers in titles or descriptions.** Use the `spoiler` flag in `missions.json`.

## Easiest way: open an issue

No Git needed. Pick a template:

- [Submit a cheat code](https://github.com/chinmaypaliwal1/awesome-gta-6/issues/new?template=cheat.yml)
- [Submit news](https://github.com/chinmaypaliwal1/awesome-gta-6/issues/new?template=news.yml)
- [Submit a rumor or leak](https://github.com/chinmaypaliwal1/awesome-gta-6/issues/new?template=rumor.yml)
- [Report wrong information](https://github.com/chinmaypaliwal1/awesome-gta-6/issues/new?template=correction.yml)

## Pull requests

The tables in `docs/cheat-codes.md`, `docs/missions.md` and `docs/news.md` are **generated from `data/*.json`**, so edit the JSON, not the tables:

```bash
# 1. Edit data/cheats.json, data/missions.json or data/news.json
# 2. Regenerate the tables
python3 scripts/build_docs.py
# 3. Commit both the JSON and the regenerated docs
```

### Cheat status

| Status | Meaning |
| :--- | :--- |
| `verified` | The same input is published by **2 or more** independent sources |
| `single-source` | Only one source so far |
| `unknown` | Unlock requirement known, input not found yet |

### News items

Add new items at the **top** of `data/news.json`. Set `"confirmed": false` for player reports, estimates and anything Rockstar or Take-Two hasn't stated.

## What we need most

- Missing cheat inputs (42 still unknown)
- Patch notes and title update details
- Leonida regions and their real-life Florida counterparts
- Radio stations and soundtrack listings
- Easter eggs and mysteries (with video proof)
- Trophy and achievement list
- Vehicle list

CI checks links weekly and checks that the generated tables match the JSON on every PR.
