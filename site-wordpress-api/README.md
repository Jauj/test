# Inventaire WordPress de combattrepourlesocialisme.com

Export brut de l'API REST publique (`/wp/v2/…`), récupéré le 8 novembre 2026.

| Fichier | Contenu |
|---|---|
| `site.json` | Nom, description, extensions exposant une API |
| `posts.json` | 1 226 articles (titre, date, contenu HTML, catégories, étiquettes) |
| `pages.json` | 30 pages |
| `categories.json` | 139 catégories (hiérarchie via `parent`) |
| `tags.json` | 377 étiquettes |
| `media.json` | 855 médias (métadonnées seulement, pas les fichiers) |

Ce sont les données publiques que WordPress expose à tout visiteur. Le code PHP du thème et des extensions n'est pas inclus.
