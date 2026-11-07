# Copie du site « Combattre pour le Socialisme »

Copie de référence du site public de *Combattre pour le Socialisme*, faite le 7 novembre 2026 pour en étudier la structure et le design avant une refonte.

## Origine

- Le domaine `combattrepourlesocialisme.fr` **n'existe pas** (aucun enregistrement DNS au 07/11/2026).
- Le site réel est hébergé sur les pages perso de Free : **http://socialisme.free.fr/** (HTTP uniquement, pas de HTTPS).
- Les pages ont été récupérées via Firecrawl (navigateur distant), car le réseau de l'environnement de travail ne laisse sortir que le HTTPS.

## Contenu

```
site-original/
├── stylecps.css                         # feuille de style unique du site (copie exacte)
└── pages/
    ├── index.php.html                   # Accueil
    ├── texcons.php.html                 # Textes constitutifs
    ├── sommaire.php.html                # Publications (toutes, 1984 → 2026)
    ├── recherchethem.php_tag-null.html  # Index thématique (liste des tags)
    ├── recherchethem.php_tag-cjr.html   # Exemple de page de tag (CJR)
    ├── liens.php.html                   # Liens
    ├── contact.php.html                 # Abonnement & Contact
    └── quisommesnous.php.html           # Qui sommes-nous (page cassée en ligne, voir l'audit)
```

## Limites de la copie

- **HTML rendu, pas le code PHP.** Les fichiers `.php` s'exécutent sur le serveur de Free ; on ne récupère que le HTML qu'ils produisent. Les includes (`navt.php`, `navtminres.php`…) et la base de données derrière `recherchethem.php` ne sont pas accessibles.
- **HTML normalisé par le navigateur.** Firecrawl renvoie le DOM après analyse par Chromium : des balises comme `<tbody>` ont été ajoutées et les balises non fermées ont été refermées (d'où les cascades `<b><b><b>` sur l'accueil). C'est très proche du code servi, mais pas une copie octet par octet.
- **Pas d'images.** Les images (bandeau `img/entete.jpg`, titres de rubriques, photos) n'ont pas pu être téléchargées dans cet environnement. Les chemins restent référencés dans le HTML.
- **Pas de PDF.** Environ 460 PDF (bulletins, suppléments) sont liés depuis les pages ; ils ne sont pas copiés.
- **Pas les ~330 anciennes pages `.htm`** (exports Word des années 2000), sauf comme exemple dans l'audit.
- Les liens pointent toujours vers `http://socialisme.free.fr/…` (URL absolues d'origine).

Voir `../AUDIT.md` pour l'analyse.
