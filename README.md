# Parliamo — Italian from scratch

A small mobile-first web app for learning Italian: eight short illustrated lessons (greetings, introductions, the bar, numbers, directions, *essere*, food, colours), spaced-repetition review with a weekly activity strip, and an AI conversation partner. It can be added to the phone's home screen like an app.
The interface is available in **Russian** and **English** (switch in the top-right corner, or open the site with `?lang=en` / `?lang=ru`).

Every word and phrase is voiced with pre-recorded neural voices (Isabella, female, and Diego, male), so it sounds the same on every device. If a recording is missing, the browser's built-in speech synthesis is used instead.

## Structure

- `index.html` — the whole app (HTML, CSS, JS), no build step.
- `audio/f/`, `audio/m/` — MP3 recordings for the female and male voice, named by a hash of the phrase.
- `icons/`, `manifest.webmanifest` — home-screen icon and web app manifest.
- `tools/` — scripts used to regenerate the recordings:
  - `extract.js` collects every speakable phrase from `index.html` into `texts.json`;
  - `genall.py` records them with [edge-tts](https://github.com/rany2/edge-tts) (`pip install edge-tts`). After regenerating, paste `texts.json` into the `AUDIO` constant in `index.html`.

## Deployment

Pushing to `main` deploys the site to GitHub Pages via `.github/workflows/pages.yml`.

The chat partner relies on the Claude artifact runtime, so it only answers when the page is opened inside Claude; on GitHub Pages lessons and review work fully, and the chat shows a notice.
