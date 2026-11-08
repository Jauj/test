# Audit du site combattrepourlesocialisme.com

**Site audité :** https://combattrepourlesocialisme.com · **Date :** 8 novembre 2026
**Matériaux :** miroir HTML/CSS/JS/images dans [`site-wordpress/`](site-wordpress/), inventaire complet via l'API WordPress dans [`site-wordpress-api/`](site-wordpress-api/), captures dans [`audit-captures/`](audit-captures/).

> L'audit de l'ancien site `socialisme.free.fr`, fait par erreur, est rangé dans [`ancien-site-free/`](ancien-site-free/AUDIT.md). Il reste utile : le nouveau site reprend son archive.

---

## 1. Synthèse

Le site est une **migration récente et active** de l'ancien site Free vers WordPress. Il a déjà une vraie identité (logo, en-tête, cartes avec photos), un encadré « Dernier bulletin » réussi et une **recherche avec filtres** sur les bulletins, ce que l'ancien site n'avait pas. L'archive complète (1 226 articles, 1984 → 2026) est en ligne.

Les problèmes viennent surtout d'une construction par couches successives :

| Priorité | Constat |
|---|---|
| 🔴 Bloquant pour la mise en ligne | Le site est en **`noindex, nofollow`** : Google ne l'indexe pas. |
| 🔴 Bloquant pour la mise en ligne | **URL techniques** (`?page_id=10648`, `?p=…`) au lieu d'adresses lisibles. |
| 🟠 Structure | **Au moins quatre façons de présenter un article** (visionneuse PDF, cartes HTML à styles en ligne, blocs, page sur mesure). |
| 🟠 Structure | **139 catégories**, doublons, catégories vides ou « test », 7 articles « Uncategorized ». |
| 🟠 Contenu | 1 074 articles sur 1 226 **ne contiennent qu'un PDF** : texte non lisible par les moteurs ni confortable sur mobile. |
| 🟠 Design | **Boutons et liens bleus** (couleur par défaut du thème) qui jurent avec l'identité rouge. |
| 🟠 Mobile | En-tête mal aligné et très haut (≈ 300 px), titre du premier article absent en tête de carte. |
| 🟡 Technique | Deux constructeurs de blocs (Kadence Blocks **et** Gutentor), 143 Ko de CSS en ligne sur l'accueil, PHP 8.1 en fin de vie. |

---

## 2. Technique

### Pile logicielle
- **WordPress 7.1.4**, **PHP 8.1** (plus de correctifs de sécurité depuis fin 2025), Apache, hébergement **IONOS** (extension « IONOS Performance »).
- **Thème Kadence** + **Kadence Blocks** (version Pro détectée).
- Extensions repérées dans le code public : **Gutentor** (second constructeur de blocs), **Post Slider and Carousel**, **3D FlipBook (dFlip Lite)**, une visionneuse PDF par bloc, **FileBird** (dossiers de médias), **Instant Images**, **Code Snippets**, **All-in-One WP Migration**.

### Poids de l'accueil
- HTML : **190 Ko**, dont **143 Ko de CSS en ligne** (29 blocs `<style>`).
- **25 feuilles de style** et **9 scripts** externes.
- Chargement complet mesuré : ~4,3 s (ordinateur et mobile), dans cet environnement.
- Deux constructeurs de blocs (Kadence Blocks + Gutentor) font la même chose : en garder un seul allégerait le site et simplifierait l'édition.

### Référencement et partage
- `<meta name="robots" content="noindex, nofollow">` sur l'accueil : **sans doute volontaire pendant la construction**, mais à retirer au lancement.
- **Permaliens « simples »** : `/?page_id=4672` au lieu de `/qui-sommes-nous/`. À changer **avant** la mise en ligne publique, sinon les liens partagés casseront.
- Pas de `meta description`, pas de balises Open Graph (aperçu vide quand on partage un lien sur les réseaux ou par messagerie).
- **4 titres `<h1>`** sur l'accueil (un par carte) et aucun titre principal de page.
- Titre de la fenêtre très long (devise de Lénine incluse), coupé dans les onglets et dans Google.

---

## 3. Contenus

### Inventaire (API WordPress, 08/11/2026)

| Type | Nombre |
|---|---|
| Articles | **1 226** (1984 → 2026, un seul auteur) |
| Pages | 30 |
| Catégories | 139 (10 vides) |
| Étiquettes | 377 (servent aux numéros : « CPS 41 (Ancienne série) ») |
| Médias | 855 visibles : 531 PDF (**2,5 Go**), 324 images (32 Mo) |

Répartition par année : 20 à 45 articles par an de 1984 à 2023, puis une dizaine par an depuis 2024 (seulement les publications nouvelles).

### Formats d'articles hétérogènes
| Format (début du contenu) | Articles |
|---|---|
| Bloc « visionneuse PDF » seul | **1 074** |
| Carte HTML écrite à la main (`odtp-profile-card`, styles en ligne) | 84 |
| Blocs Gutenberg classiques (paragraphes, titres, listes) | 35 |
| Lien PDF simple (`cps-lien-pdf`) | 26 |
| Page sur mesure avec sa propre feuille `<style>` (`np-page`) | 1 |

- **4 418 attributs `style="…"`** dans les contenus : chaque article porte sa propre mise en forme (couleurs, bordures, tailles). Pour changer l'apparence, il faudra repasser sur chaque article.
- Exemple d'incohérence : deux cartes récentes encadrées l'une en noir (`#1a1a1a`), l'autre en rouge (`#F70C0C`) sur fond gris.
- Le contenu médian d'un article fait **253 caractères** : le texte réel est dans le PDF.

### Catégories
```
Publications (240)
├── Bulletins (199) · Suppléments (159) · Déclarations (90)
├── On nous communique (52) · Communiqués (18)
├── Index par pays → 59 sous-catégories
├── Index thématique → 4 sous-catégories → France (296), Enseignement public (220)…
└── Index chronologique (vide)
Racines vides : Journal CPS, Classiques du marxisme, Textes des conférences du Cercle / du Groupe
Uncategorized (10) · test (2) · Textes des conférences du Comité (2)
```
- Mélange de **trois logiques** dans le même arbre : type de publication, pays, thème. Elles gagneraient à être des taxonomies séparées.
- **Doublons** : « PCI » existe deux fois (dans « Organisations politiques » et dans son sous-groupe « Lambertistes »).
- **7 articles en « Uncategorized »**, dont deux avec un nom de fichier pour titre (« 2023 03 10 supp cps86 fu bdfn fsu », « 2023 02 24 supp cps retraite »).
- Catégorie **« test »** avec 2 articles publiés.

### Pages
- **Doublons** : « Résolution adoptée par la première conférence… (9 avril 2007) » existe deux fois (ids 11041 et 12860).
- Deux pages d'accueil : **« Actualité »** (utilisée) et **« Actualité1 »** (ancienne, encore publiée).
- Pages **vides** : « Publications », « Classiques du marxisme » ; page **« Blog »** probablement résiduelle.
- Une vingtaine de **textes fondamentaux longs** (jusqu'à 265 Ko) en pages, avec des adresses de plus de 150 caractères.

### Dates à vérifier (page Bulletins)
- « Combattre pour le socialisme n°96 – 28 février 2026 » est daté **2 février 2026**.
- Le rapport de la VIIe conférence (avril 2026) est daté **16 septembre 2026**.
La date WordPress ne correspond pas toujours à la date de parution, et le tri chronologique s'en ressent.

### Titres génériques
41 titres sont en double, souvent des titres de rubrique en capitales : « LES MILITANTS INTERVIENNENT ET INFORMENT CPS » (15 fois), « ON NOUS COMMUNIQUE » (8), « ENSEIGNEMENT PUBLIC » (5). Dans les résultats de recherche, on ne sait pas lequel ouvrir.

---

## 4. Design

### Ce qui fonctionne (à garder)
- **En-tête** clair : logo, titre en capitales rouges, devise, surtitre du Groupe.
- **Encadré « Dernier bulletin »** : couverture, éditorial, mots d'ordre en cadre, sommaire. C'est le meilleur élément du site.
- **Grille de cartes avec photos** sur l'accueil : vivante, lisible.
- **Recherche filtrée** sur la page Bulletins (dates, thème, organisation, lieu, nature, texte intégral).
- Bloc **« À lire et relire »** pour les textes fondamentaux.

### Ce qui pose problème
- **Couleurs :** les boutons « Lire la suite », « Rechercher », « Lire le texte » et les liens sont **bleus** (couleur par défaut de Kadence), alors que tout le reste est rouge. Le menu actif est **saumon**. On compte au moins trois rouges différents (logo, titre, cadres).
- **Menu :** « Abonnements et contacts » n'est pas dans le menu principal (seulement en bas de page et dans la colonne). « Publications » et « Bulletins » se recouvrent.
- **Hiérarchie typographique :** les résumés des cartes sont entièrement en gras, sans contraste avec les titres.
- **Champ de recherche :** le libellé « Tout le texte (articles et PDF) » est coupé (« …et PD »).

### Mobile (iPhone 13)
- L'**en-tête** prend environ 300 px : bouton de menu collé en haut à gauche, logo décalé vers le bas, titre sur 2 lignes et devise sur 2 lignes.
- Sur l'accueil, la **première carte commence par la date et le texte en gras** : le titre de l'article n'apparaît pas en tête.
- La colonne « Dernier bulletin » passe tout en bas de la page, après tous les articles.

Captures : `audit-captures/accueil-desktop.png`, `accueil-mobile.png`, `bulletins-desktop.png`, `textes-fondamentaux-mobile.png`, etc.

---

## 5. Recommandations

L'équipe publie déjà avec WordPress. Je recommande donc de **garder WordPress** et d'en assainir la structure, plutôt que de tout reconstruire.

### Avant la mise en ligne publique
1. Activer des **permaliens lisibles** (`/%postname%/` ou `/%year%/%postname%/`).
2. Retirer le **`noindex`**, ajouter une extension SEO légère (titres, descriptions, Open Graph, plan du site).
3. Supprimer ou dépublier : page « Actualité1 », doublon de la Résolution 2007, pages vides, catégorie « test » ; reclasser les 7 « Uncategorized » et corriger les titres-fichiers.
4. Monter **PHP en 8.3 ou plus** chez IONOS (réglage du panneau d'hébergement).

### Structure des contenus
5. Créer un **type de contenu « Numéro »** (bulletin) avec des champs : série, numéro, date de parution, PDF, couverture, sommaire. La page Bulletins et l'encadré « Dernier bulletin » se rempliraient tout seuls.
6. Séparer les classements en **taxonomies distinctes** : *Type* (supplément, déclaration, communiqué…), *Thème*, *Pays*, *Organisation*, *Numéro*. Cela correspond déjà aux filtres de la recherche.
7. Remplacer les cartes HTML écrites à la main par **un seul modèle** (bloc réutilisable ou gabarit), sans styles en ligne.
8. Mettre progressivement **le texte des éditoriaux et déclarations en HTML**, en gardant le PDF à télécharger.

### Design
9. Définir une **palette unique** dans les réglages globaux de Kadence : un rouge principal pour les boutons, liens et menu actif, un rouge foncé pour les survols, un neutre chaud. Plus de bleu.
10. Retravailler l'**en-tête mobile** : logo et titre sur une ligne, devise masquée ou réduite, menu à droite.
11. Ajouter **« S'abonner »** au menu principal, sous forme de bouton.
12. Sur mobile, remonter **le dernier bulletin** juste après la première actualité.
13. Supprimer **Gutentor** une fois ses blocs remplacés par des blocs Kadence.

---

## 6. Questions pour la suite

1. Le `noindex` est-il volontaire (site en construction) ? Quand prévoyez-vous l'ouverture ?
2. Qui publie, et à quelle fréquence ? (Cela décide du niveau d'automatisation à viser.)
3. Les cartes `odtp-profile-card` viennent-elles d'un outil de conversion depuis LibreOffice ? Si oui, on peut l'adapter pour produire du HTML propre.
4. Pouvons-nous travailler sur une **copie de test** du WordPress (IONOS propose souvent un environnement de préproduction), ou préférez-vous que je prépare d'abord des maquettes ?
5. Par quoi voulez-vous commencer : la **structure** (types de contenu, catégories, URL) ou le **design** (couleurs, en-tête, mobile) ?
