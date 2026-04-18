# STEP viewer setup

Drop `.step` or `.stp` files into this folder, then list them in `manifest.json`.

Example:

```json
{
  "title": "Timber Ridge top-of-funnel volumetric models",
  "models": [
    { "label": "Bag 1", "file": "bag-1.step", "thumbnail": "thumbnails/bag-1.png", "caption": "Bag 1" },
    { "label": "Bag 2", "file": "bag-2.step", "thumbnail": "thumbnails/bag-2.png", "caption": "Bag 2" }
  ]
}
```

## Thumbnail workflow

The deck can load thumbnails from `assets/models/thumbnails/`.

Expected naming for the fast path:

- STEP: `bag-1.step`, `bag-2.step`, ...
- Thumbnail: `thumbnails/bag-1.png`, `thumbnails/bag-2.png`, ...

Or set `thumbnail` explicitly per model in `manifest.json`.

## Rendering consistent thumbnails

Use `thumbnail-viewer.html` with the STEP file passed as a query parameter.

Example local URL:

```text
http://127.0.0.1:8765/timber-ridge-daypack-development-clean/thumbnail-viewer.html?model=bag-1.step&zoom=1.2
```

The viewer is configured for consistent framing and orientation so screenshots can be turned into uniform thumbnails.
