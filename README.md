
# Subway Stock Calculator (PWA)

A mobile-friendly, offline-capable web app to total Subway stock with inputs like `2B`, `1.5P`, or `12`. Works on iOS and Android. Install via **Add to Home Screen**.

## Quick Deploy (GitHub Pages)
1. Create a **public** GitHub repo (e.g., `subway-stock-calculator`).
2. Upload `index.html` to the repo root (no subfolders).
3. In **Settings → Pages**:
   - Source: **Deploy from a branch**
   - Branch: **main** / **master**, folder: **/** (root)
4. Wait ~1 minute. Your app will be live at:
   `https://<your-username>.github.io/<your-repo>/`

## Use on Phone
- **Android (Chrome):** Menu `⋮` → **Add to Home screen**.
- **iPhone (Safari):** Share → **Add to Home Screen**.

## Notes
- Data persists in `localStorage`.
- Works offline via a lightweight service worker cached on first load.
