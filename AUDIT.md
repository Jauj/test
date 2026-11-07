# Audit du site « Combattre pour le Socialisme »

**Site audité :** http://socialisme.free.fr/ · **Date :** 7 novembre 2026 · **Copie de référence :** [`site-original/`](site-original/README.md)

> Le domaine `combattrepourlesocialisme.fr` n'existe pas encore (aucun DNS). Il est libre à l'achat, ou appartient à quelqu'un qui ne l'utilise pas : à vérifier auprès d'un registraire. C'est un bon candidat pour le futur site.

---

## 1. Synthèse

Le site fait son travail d'archive : 42 ans de publications (1984 → 2026), environ 380 entrées, 460 PDF et 330 anciennes pages HTML, avec un index thématique d'une centaine de tags. Le contenu est riche et bien daté.

La forme a vieilli et plusieurs problèmes touchent directement les visiteurs :

| Priorité | Problème | Effet pour le visiteur |
|---|---|---|
| 🔴 Critique | La page **« Qui sommes-nous ? »** est cassée | On voit du code Word et PHP brut au lieu du texte de présentation du Groupe |
| 🔴 Critique | **Pas de HTTPS** | Les navigateurs affichent « Non sécurisé » ; certains bloquent la page |
| 🔴 Critique | **Sur mobile, la colonne de gauche disparaît** | Ni dernier numéro, ni présentation, ni CJR sur téléphone |
| 🟠 Important | Liens cassés ou faux (voir § 4) | PDF qui ne s'ouvrent pas, actualité « avalée » sur l'accueil |
| 🟠 Important | Deux générations de pages sans rapport visuel | ~330 pages `.htm` style Word 2003, sans menu ni charte |
| 🟠 Important | Pas de recherche (« Ctrl F » conseillé) | Archive difficile à exploiter |
| 🟡 À améliorer | Titres de rubriques en images, pas d'`alt`, pas de `lang` | Accessibilité et référencement faibles |
| 🟡 À améliorer | Même `<title>` sur toutes les pages, pas de description | Mauvaise présence dans Google |

---

## 2. Architecture technique

### Hébergement
- **Pages perso Free** (`socialisme.free.fr`), PHP côté serveur, très probablement une base MySQL pour l'index thématique (`recherchethem.php?tag=…`).
- **HTTP uniquement** : la connexion HTTPS est refusée par le serveur.
- Statistiques via **phpMyVisites** sur `st.free.fr` (service ancien, en HTTP).
- Vérification Google Search Console présente sur l'accueil.

### Gabarit
Toutes les pages « modernes » (`.php`) partagent le même squelette :

```
<header>  2 images : bandeau ordinateur (img/entete.jpg) + bandeau mobile (minres.jpg)
<div id="banordi">  menu ordinateur  (tableau de 6 cellules)
<div id="minres">   menu mobile      (le même menu, en 2 tableaux de 3)
<div id="asideandarticle">
   <aside>   4 encadrés : dernier numéro / qui sommes-nous / à lire et relire / CJR
   <article> contenu
```

- L'en-tête et le menu sont inclus en PHP (`navt.php`, `navtminres.php`, visibles dans la page cassée).
- **Le menu est dupliqué** (desktop + mobile) et basculé en CSS ; les identifiants `banordi` et `minres` sont utilisés deux fois chacun (sur une image et sur un `div`), ce qui est invalide.
- **Mise en page en tableaux** (`<table>`) pour le menu, les encadrés et les pages intérieures.
- Toutes les URL internes sont **absolues en `http://socialisme.free.fr/…`**, ce qui compliquera tout changement de domaine.

### Deux générations de pages
1. **Pages PHP (époque estimée : années 2010)** : charte rouge, menu, mise en page commune. 7 pages.
2. **Pages `.htm` héritées (années 2000)** : exports « Enregistrer sous… HTML » de Microsoft Word. Elles n'ont **ni menu, ni bandeau, ni feuille de style commune** : police Times, liens bleus/violets, styles Word (`MsoNormal`, `OCorpsCPS`…), image de fond, encodage `windows-1252`. Exemple : `nouvelle_perspective0.htm` (texte de 1997, mis en ligne en 2004). Environ **330 liens** du sommaire y mènent.

### Feuille de style (`stylecps.css`)
- Le fichier commence par `<!--` puis `<!DOCTYPE HTML PUBLIC …>`. **Vérifié dans Chromium : la première règle (`html, body { margin:0; max-width:1080px; text-align:center }`) est ignorée**, car ce texte rend son sélecteur invalide. Les marges et la largeur maximale prévues ne s'appliquent donc pas.
- Largeurs incohérentes : `body` limité à 1080 px (règle ignorée), conteneur à 1200 px, article à 800 px, colonne à 320 px.
- Cinq rouges différents sans système : `#DF0000`, `#CF122B`, `#C30000`, `#990000`, plus le beige `#EDEDDF`.
- Une media query mobile vide (`max-device-width: 480px`).
- Classe `.datenews` : texte blanc sur beige clair (illisible), heureusement inutilisée.
- Pas de typographie définie (simple `sans-serif`), pas de hauteur de ligne, texte justifié sans césure.

---

## 3. Arborescence et contenus

```
Accueil (index.php)
├── Textes constitutifs (texcons.php)       ~30 textes de référence 1984-2017
├── Publications (sommaire.php)             1 seule page de 216 Ko : 382 entrées, 1984 → 2026
├── Index thématique (recherchethem.php)    ~100 tags en 5 groupes (Rubriques, France,
│                                           Partis & syndicats, Théorie, International)
├── Liens (liens.php)                       6 liens externes
├── Abonnement & Contact (contact.php)      chèque par courrier, adresse e-mail
└── [hors menu] Qui sommes-nous (quisommesnous.php)   ← accessible seulement depuis l'accueil
```

**Accueil :** 4 encadrés à gauche + **45 actualités empilées sans pagination**, de novembre 2026 à avril 2022. Chaque actualité est un `<h4>` daté, un `<h5>` vide, puis un paragraphe et un lien « Lire la suite » vers un PDF.

**Types de contenus identifiés** (utile pour le futur modèle de données) :
- Numéro de *CPS* (Nouvelle Série, n° 1 → 98) : date, numéro, PDF complet, sommaire d'articles, éditorial en PDF séparé
- Supplément / tract / déclaration : date, numéro de rattachement, titre, PDF
- Communiqué d'organisation sœur (Maghreb socialiste, CJR, courant Front Unique)
- Texte de référence / texte de conférence
- Tags thématiques (multi-tags par article)

**Formats :** dans le sommaire, 948 liens, dont ~460 PDF, ~330 pages `.htm`, quelques liens directs vers une page de PDF (`#page=23`). Presque tout le contenu récent n'existe **qu'en PDF**, donc peu lisible sur mobile et mal indexé.

---

## 4. Erreurs constatées

### Page cassée
- **`quisommesnous.php`** est un export Word enregistré en **UTF-16**. Le navigateur l'affiche comme du texte : le visiteur voit les balises `<html xmlns:v=…>`, les métadonnées Word (auteur, société « Hewlett-Packard »…) et les instructions `<?php include('./navt.php'); ?>` non exécutées. Le texte de présentation est noyé dedans avec des caractères corrompus (`s\u0019 exprimait`). C'est la page vers laquelle renvoie « Lire la suite… » de l'encadré « Qui sommes-nous ».

### Liens erronés
| Où | Problème |
|---|---|
| Accueil, encadré « Dernier numéro » | Lien vers `…/#http://…/2026_10_01_cps_98_180as.pdf` : l'URL du PDF est derrière un `#`, le PDF ne s'ouvre pas. Même défaut dans le sommaire. |
| Accueil, actualité du 04/06/2024 (Algérie) | Guillemet manquant dans le `href` : l'actualité suivante (sommaire de CPS n° 91) est **absorbée dans l'URL** du lien, elle n'apparaît pas et le lien est mort. |
| Sommaire | 5 liens « HTML » pointent vers `http://socialisme.free.fr/X` (texte provisoire jamais remplacé). |
| Sommaire | 5 noms de fichiers PDF avec des espaces (`%20`), fragiles. |
| Textes constitutifs | « Textes des conférences du groupe » pointe vers `lucas.vila.auteur.free.fr/SiteCPS/…`, un **site de développement**. |
| Textes constitutifs | « Manifeste du Parti Communiste » renvoie vers… le Programme de transition. |
| Textes constitutifs | Caractères `>` parasites affichés après les deux images. |
| Index thématique | `mailto:socialisme.free.fr` : adresse e-mail invalide (pas de `@`). |
| Contact | `mailto: socialisme@free.fr` avec une espace en tête (certains clients mail échouent). |

### Qualité du HTML
- Balises `<b>` non fermées sur l'accueil : le navigateur les imbrique (`<b><b><b>`), d'où des pans entiers en gras involontaire.
- `<ul>` utilisés sans `<li>` (Liens, Textes constitutifs), `<p>` à l'intérieur de `<ul>`.
- 45 titres `<h5>` vides sur l'accueil ; niveaux de titres incohérents (pas de `<h1>` principal sur l'accueil).
- 8 images sur 9 sans attribut `alt` ; les titres de rubriques (« Sommaire », « Actualités », « Qui sommes-nous »…) sont des **images de texte**.
- Pas d'attribut `lang="fr"`, pas de `<meta name="description">`, `<title>` identique sur toutes les pages.

---

## 5. Design et expérience utilisateur

**Ce qui fonctionne et mérite d'être gardé**
- Identité forte et lisible : le **rouge** et le bandeau-titre, la bande de menu rouge.
- Organisation claire en peu de rubriques.
- Les encadrés « Dernier numéro » et « À lire, à relire » sont de bonnes idées éditoriales.
- La datation systématique et l'archive complète depuis 1984.

**Ce qui pose problème**
- **Mobile :** sous 800 px, l'`aside` est masqué (`display:none`). Sur téléphone on perd le dernier numéro, la présentation du Groupe et le CJR. Le menu passe sur deux lignes de tableau.
- **Hiérarchie visuelle faible :** l'accueil est un long mur de texte en gras, sans images, sans séparation nette entre les actualités.
- **Pas de point d'entrée « Qui sommes-nous »** dans le menu principal.
- **Pas de recherche** dans l'archive ; l'index renvoie à « Ctrl F ».
- **Abonnement** uniquement par chèque ; l'inscription à la liste de diffusion passe par un lien `mailto:` vers `ml.free.fr`.
- **Formats de date mélangés** : `2026-11-01` sur l'accueil, `01/11/2026` dans le sommaire.
- **Rupture totale de charte** dès qu'on ouvre un ancien texte `.htm`.

---

## 6. Recommandations pour la refonte

### Technique
1. **Site statique** généré (Astro, Eleventy ou Hugo) : pas de PHP ni de base, hébergement gratuit en HTTPS (GitHub Pages, Netlify, Cloudflare Pages), facile à maintenir.
2. **Données séparées de la mise en page** : un fichier par numéro / supplément (Markdown + métadonnées : date, numéro, type, tags, PDF). Le sommaire actuel (`sommaire.php.html`) peut être converti automatiquement : il est régulier.
3. **Nom de domaine** propre (`combattrepourlesocialisme.fr` s'il est disponible), avec redirections depuis les anciennes URL si Free le permet (sinon, une page d'accueil de renvoi).
4. **Recherche plein texte** côté navigateur (Pagefind ou équivalent), qui fonctionne sans serveur.
5. **Reconvertir progressivement les ~330 pages Word** en Markdown propre, intégrées à la charte.
6. **Mettre le texte des éditoriaux et déclarations en HTML**, en gardant le PDF en téléchargement.

### Structure proposée
```
Accueil         dernier numéro en vedette · 5-6 dernières prises de position · accès rapides
Le journal      numéros de CPS par année (couverture, sommaire, PDF)
Prises de position   suppléments, déclarations, tracts (filtrables par thème)
Thèmes          index thématique avec vraie page par tag
Le Groupe       qui sommes-nous · textes constitutifs · conférences
Jeunesse (CJR)  présentation, Socialisme ou Barbarie, contact
S'abonner / Contact   abonnement, liste de diffusion, contact
```

### Design
- Garder le **rouge** et la tradition typographique du bulletin, mais avec **une seule palette** (un rouge principal, un rouge foncé, un neutre chaud).
- Typographie de presse : un caractère à empattements pour les textes longs, un sans-serif gras pour les titres et les mots d'ordre.
- **Mobile d'abord** : toutes les rubriques accessibles sur téléphone, menu repliable.
- Titres en texte (pas en images), contrastes conformes RGAA/WCAG AA, `alt` sur les images.

---

## 7. Questions pour la suite

1. Le nom de domaine `combattrepourlesocialisme.fr` est-il à acheter, ou l'avez-vous déjà réservé ?
2. Qui mettra le site à jour, et avec quel outil ? (Éditer des fichiers texte, ou une interface d'administration ?)
3. Faut-il reprendre **toute** l'archive dès le départ, ou commencer par les numéros récents et migrer l'historique ensuite ?
4. Avez-vous les fichiers sources des images (bandeau, logo) en meilleure qualité ? Je n'ai pas pu les télécharger.
5. Souhaitez-vous garder l'apparence actuelle en la modernisant, ou partir sur une nouvelle charte ?
