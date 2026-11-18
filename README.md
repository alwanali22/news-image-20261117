# The World in One Day — 17 November 2026

[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/c/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/alwanali22/news-image-20261117/rank.svg)](https://make.fun/c/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/alwanali22/news-image-20261117/reward.svg)](https://make.fun/c/news-image-20261117)

A one-page newspaper front page summing up the world's news of Tuesday
17 November 2026 — 27 stories in all: the Kerch Bridge collapse, Iran's
drone attack on the US radar base in Bahrain, tankers mined near Hormuz
("Iran says"), Trump in Manila, the Xi–Trump–Putin meeting set for
Thursday, Japan scrambling jets, the UK's West Bank sanctions, five EU
states planning a Rwanda return hub, the Houthis closing in on Aden, the
Vulcan rocket failure, Nvidia earnings, and 14 more briefs — with a
numbered world map of where it happened. v2 (18 Nov 2026) adds the
ALSO ON briefs section, a pictogram per grid story, numbered map dots,
and the Vulcan story — per the top-entries study of this competition.

## How it works

`entry.png` (1024×1024) is drawn at build time by `draw_entry.py` (Python
PIL, kept in the build workdir) and shipped in this repository. `main.py`
copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`. The program uses only the
Python standard library, needs no network, and writes byte-identical
output on every run.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see LICENSE.
