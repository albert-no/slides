# /standalone-deck

Generate a self-contained `<deck>.standalone.html` from a deck HTML source by inlining all CSS, JS, fonts, and images. Wraps `scripts/bundle.py`.

## Inputs

- Target deck path (HTML file). If none given, default to:
  - the single non-`.standalone.html` `*.html` under the current deck folder, or
  - `--all` if the user explicitly says "all decks" / "every deck".

## Workflow

1. **Resolve target.**
   - If the user passed a path, use it.
   - If no argument and cwd is a deck folder, pick the single `*.html` (excluding `*.standalone.html`).
   - If ambiguous (multiple candidates), list them and ask which one — do not guess.
2. **Run the bundler:**
   ```bash
   python3 scripts/bundle.py <deck>.html
   # or
   python3 scripts/bundle.py --all
   ```
3. **Report** the output path and file size from the bundler's stdout. Note that `*.standalone.html` is gitignored — it's a build artifact for distribution, not for committing.

## Do not

- Edit the source deck.
- Commit the standalone output (it's gitignored by design).
- Re-bundle a file that already ends in `.standalone.html` (the script skips these, but don't pass them in).
