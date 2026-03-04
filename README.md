# Test App v2 - PyInstaller Universal DMG

Version simplifiée avec un seul DMG universel (ARM + Intel).

## Différences vs v1

| | v1 | v2 |
|---|---|---|
| Builds macOS | 2 (ARM + Intel séparés) | 1 (Universal2) |
| Format macOS | `.app` | `.dmg` universel |
| Windows | `.exe` | `.exe` |
| Jobs GitHub Actions | 3 | 2 |

## Structure

```
test_app_v2/
├── app.py
└── .github/
    └── workflows/
        └── build.yml
```

## Artifacts récupérés

- `TestApp-macOS-Universal-DMG` → fonctionne sur ARM **et** Intel
- `TestApp-Windows` → Windows x86_64

## ⚠️ Attention

Si une dépendance n'est pas disponible en `universal2`, le build échoue.
Dans ce cas, revenir à la v1 avec 2 builds séparés.
