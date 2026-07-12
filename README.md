# MEI Music Archive — Jekyll scaffold

Static, interactive catalog of MEI-encoded works. No user accounts, no backend.

## How it works

- `_data/metadata.csv` — your composer/title/editor/date/source metadata, plus an
  `id` column (matches the generated page URL) and `mei_file` column (matches a
  filename in `assets/mei/`).
- `scripts/generate_works.py` — pandas script that turns each CSV row into a
  page in `_works/`. Run it before building.
- `_layouts/work.html` — loads that work's MEI file, renders notation with
  Verovio, and derives MIDI for in-browser playback with html-midi-player.
- `index.md` + `assets/js/catalog-filter.js` — the browsable/filterable/sortable
  catalog table, plain JS, no dependencies.
- `.github/workflows/build.yml` — runs the generator script, builds Jekyll,
  deploys to GitHub Pages automatically on every push to `main`.

## Adapting to your real repo

1. Replace `_data/metadata.csv` with your actual CSV.
   - If your column names differ from `id, composer, title, editor, date, source,
     mei_file`, update the `COLUMNS` dict at the top of `scripts/generate_works.py`
     — nothing else needs to change.
2. Copy your `.mei` files into `assets/mei/`, matching the `mei_file` values in
   the CSV.
3. Push to GitHub, enable Pages under **Settings → Pages → Source: GitHub
   Actions**. The workflow handles the rest.

## Running locally

```bash
pip install pandas
python scripts/generate_works.py
bundle install
bundle exec jekyll serve
```

Then visit http://localhost:4000.

## Notes / things to revisit as this grows

- MIDI playback quality depends on the default soundfont Verovio/MIDI derive —
  fine for previewing, not a substitute for a real audio recording.
- For a large archive (hundreds+ of works), the plain-JS catalog filter will
  start to feel slow; a proper client-side search index (e.g. Lunr.js) would
  be the next step, but isn't needed yet.
