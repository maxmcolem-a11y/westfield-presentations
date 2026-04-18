# STEP viewer setup

Drop `.step` or `.stp` files into this folder, then list them in `manifest.json`.

Example:

```json
{
  "title": "Timber Ridge top-of-funnel volumetric models",
  "models": [
    { "label": "Shape Family 01", "file": "shape-family-01.step", "caption": "Faceted volume study" },
    { "label": "Shape Family 02", "file": "shape-family-02.step", "caption": "Ordered chaos study" }
  ]
}
```

The deck will load the selected STEP file in-browser with orbit, pan, and zoom enabled.
