# Refonte de combattrepourlesocialisme.com : accessibilité, recherche, design

**Date :** 8 novembre 2026 · **Maquette :** [`maquette/`](maquette/) (accueil + recherche) · **Captures :** [`maquette/captures/`](maquette/captures/)

Ce document se lit avec [`AUDIT.md`](AUDIT.md). Il a trois parties : les normes d'accessibilité à respecter, le modèle de données pour la recherche, puis les modifications proposées, par ordre de priorité.

---

## 1. Normes d'accessibilité en vigueur (novembre 2026)

### Les textes de référence
| Référence | Ce que c'est | Pour CPS |
|---|---|---|
| **WCAG 2.2** (W3C, recommandation d'octobre 2023) | La norme internationale. Trois niveaux : A, **AA** (le niveau visé partout), AAA. | **Cible recommandée : niveau AA.** |
| **RGAA 4.1.2** | Version française des WCAG : 106 critères testables, avec une méthode d'audit. | **Obligatoire pour le secteur public et les grandes entreprises**, pas pour un groupe politique. C'est néanmoins la grille de contrôle la plus pratique en français. |
| **European Accessibility Act** (en vigueur depuis le 28 juin 2025) | Étend l'obligation à certains services privés (commerce en ligne, banque, transport…). | **Ne s'applique pas** à un site militant sans vente. |
| **WCAG 3.0** | Encore à l'état de **brouillon** (version de travail de septembre 2026). | À surveiller, rien à appliquer. La méthode de contraste « APCA » a été **retirée du brouillon en 2023**. On continue donc à mesurer avec la formule WCAG 2. |

Aucune obligation légale ne pèse sur CPS, mais un site accessible est lu par plus de monde : personnes malvoyantes, lecteurs sur un téléphone en plein soleil, personnes âgées, lecteurs d'écran.

### Les exigences qui comptent pour ce site (WCAG 2.2 AA)
| Critère | Exigence | Situation du site actuel |
|---|---|---|
| 1.4.3 Contraste du texte | **4,5:1** minimum (3:1 pour le texte de plus de 24 px, ou 19 px en gras) | Rouge du logo `#F70C0C` sur blanc : **4,2:1 ✗**. Menu actif saumon : **1,6:1 ✗**. |
| 1.4.11 Contraste des éléments d'interface | **3:1** pour les bordures de champs, les icônes, les indicateurs de focus | Bordures grises très claires sur les champs de recherche. |
| 2.4.7 / 2.4.11 Focus visible | Un contour net autour de l'élément sélectionné au clavier | Le thème masque le contour (`hide-focus-outline`). |
| **2.5.8 Taille des cibles** (nouveau en 2.2) | Zones cliquables d'au moins **24 × 24 px** | **Échec relevé par axe-core** sur l'accueil et la page Bulletins. |
| 1.1.1 Alternatives textuelles | `alt` pertinent sur les images informatives, `alt=""` sur les images décoratives | À vérifier article par article. |
| 1.3.1 Structure | Titres hiérarchisés (un seul `h1`), listes, champs étiquetés | **4 `h1`** sur l'accueil. |
| 2.4.1 Contournement | Lien « Aller au contenu » | Absent. |
| 3.1.1 Langue | `lang="fr"` | ✓ présent. |
| 1.4.10 Redistribution | Lisible à 320 px de large sans défilement horizontal | ✓ pas de débordement mesuré. |
| 2.3.3 / préférences | Respect de `prefers-reduced-motion` (moins d'animations) | Le carrousel d'articles à vérifier. |

**PDF :** un PDF est un contenu comme un autre et doit être accessible (texte sélectionnable, titres, ordre de lecture). Les PDF scannés des années 1980-1990 ne le sont pas. Le RGAA tolère de les garder s'ils sont accompagnés d'une **version HTML** ou d'une mention claire.

**Déclaration d'accessibilité :** les sites soumis au RGAA doivent afficher un statut (« non, partiellement ou totalement conforme »). Ce n'est pas obligatoire pour CPS, mais une petite page « Accessibilité » en pied de page montre le sérieux du site. La maquette la prévoit.

### Palette proposée, contrastes calculés (formule WCAG 2)
| Rôle | Couleur | Sur blanc | Usage |
|---|---|---|---|
| Texte principal | `#1A1A1A` | **17,4:1** | Titres et corps de texte |
| Texte secondaire | `#5C5C5C` | **6,7:1** | Dates, résumés, légendes |
| **Rouge principal** | `#C8102E` | **5,9:1** | Liens, boutons (texte blanc dessus : 5,9:1), surtitres, menu actif |
| Rouge foncé | `#A50E1E` | **7,8:1** | Survol des liens et boutons |
| Filets | `#D9D2CC` | 1,5:1 | **Décoratif uniquement** (séparateurs), jamais seul porteur d'information |
| Fond doux | `#FAF7F5` | — | Alternance de sections (le rouge reste à 5,5:1 dessus) |
| Surlignage recherche | `#FFE8A3` | — | Mots trouvés (texte noir dessus : 17:1) |

Le rouge actuel du logo peut rester **dans le logo**, car les logos sont exemptés. Pour le texte et les boutons, on passe à `#C8102E` : la différence se voit à peine, mais il est conforme.

---

## 2. Modèle de données pour la recherche

Aujourd'hui, tout est rangé dans un seul arbre de 139 catégories qui mélange le type de texte, le pays et le thème. Pour une recherche efficace, chaque texte doit être décrit **sur plusieurs axes indépendants**, et chacun de ces axes devient un filtre.

### Fiche d'un texte
| Champ | Type | Exemple | Sert à |
|---|---|---|---|
| **Titre** | texte | « À bas les crédits militaires et la militarisation ! » | Le mot d'ordre, pas « Supplément à CPS n° 97 » |
| Sous-titre / chapô | texte | « Face à l'offensive ultra-réactionnaire… » | Résumé dans les résultats |
| **Type de texte** | liste fermée | Éditorial, Article, Supplément-tract, Déclaration, Communiqué, Intervention syndicale, Texte de conférence, Classique | Filtre principal |
| **Date de parution** | date | 30/05/2026 | Tri, filtre « période » (distincte de la date de mise en ligne) |
| **Rattachement** | relation vers un Numéro | CPS n° 97 (nouvelle série) | « Tous les textes du n° 97 » |
| Pages dans le numéro | nombre | p. 7-12 | Lien direct `#page=7` dans le PDF |
| **Signataire** | liste fermée | Groupe, Cercle de jeunes révolutionnaires, courant Front unique, Maghreb socialiste | Filtre « qui parle » |
| **Thèmes** | liste contrôlée, plusieurs choix | Retraites, Budget, Enseignement public, Guerre impérialiste | Filtre et pages thématiques |
| **Pays / lieu** | liste contrôlée, plusieurs choix | France, Palestine, Bolivie | Filtre géographique |
| **Organisations citées** | liste contrôlée, plusieurs choix | CGT, FO, FSU, PS, PCF, LFI, RN | Filtre « organisations » |
| Secteur | liste contrôlée | RATP, SNCF, Santé, Université, Lycées | Filtre « secteur » (intervention militante) |
| Mots-clés libres | étiquettes | « loi Yadan », « Parcoursup », « 49.3 » | Termes ponctuels qui n'ont pas leur place dans les thèmes |
| **Texte intégral** | texte long | (HTML ou texte extrait du PDF) | Recherche plein texte |
| Fichier PDF | média | `2026-05-30-supp-cps-97.pdf` | Téléchargement |
| Image | média + texte alternatif | photo de manifestation | Carte d'accueil |
| Langue | code | fr, pt | Textes traduits (ex. supplément Brésil) |

### Fiche d'un numéro du bulletin
Série (ancienne / nouvelle), numéro, date, PDF complet, couverture, éditorial (lien vers sa fiche texte), sommaire (liste ordonnée des textes avec leurs pages).

### Vocabulaire contrôlé
- Une **liste courte de thèmes** (25 à 35 au maximum), plutôt que les ~100 actuels, avec une définition d'une ligne pour chacun.
- Des **synonymes** reconnus par la recherche : « Sécu » → Sécurité sociale ; « FN » → RN ; « Éducation nationale » → Enseignement public ; « retraite » → Retraites.
- Pas de doublons (« PCI » existe deux fois aujourd'hui).
- La correspondance entre les 139 catégories actuelles et les nouveaux axes peut se faire **automatiquement en grande partie**, à partir de `site-wordpress-api/categories.json`. Le reste se vérifie à la main.

### Fonctionnement de la recherche
- **Un seul champ** au départ, puis des **filtres à cocher** avec le nombre de résultats pour chacun (« Éditorial (10) »), comme dans la maquette.
- La recherche porte sur le **titre, le chapô et le texte intégral**, y compris le texte extrait des PDF.
- Les **filtres actifs restent visibles** et se retirent d'un clic.
- **Tri** : plus récents, plus anciens, pertinence.
- L'**adresse de la page reflète la recherche** (`/textes/?q=retraites&type=editorial`), pour qu'on puisse la partager ou la mettre en favori.
- **Accessibilité** : vraies cases à cocher dans des groupes légendés, nombre de résultats annoncé aux lecteurs d'écran (`role="status"`), fonctionnement **sans JavaScript** (formulaire classique) et amélioration avec.

### Outils possibles dans WordPress
| Besoin | Option |
|---|---|
| Champs structurés (numéro, pages, signataire…) | Extension **ACF** ou champs natifs du thème |
| Taxonomies séparées (Type, Thème, Pays, Organisation, Secteur) | Taxonomies personnalisées (ACF, Pods ou quelques lignes de code) |
| Recherche plein texte, PDF compris, avec filtres | **Relevanssi** ou **SearchWP** (tous deux savent indexer le texte des PDF), avec des filtres de type FacetWP ou équivalent |
| Extraction du texte des PDF anciens scannés | Reconnaissance de caractères (OCR) en lot, une seule fois |

La page Bulletins actuelle a déjà des filtres (Thème, Organisation, Lieu, Nature). On peut probablement s'appuyer sur ce travail existant.

---

## 3. Modifications proposées

### Navigation : 4 onglets + 1 bouton
| Onglet | Contient | Remplace |
|---|---|---|
| **Actualités** | Accueil : à la une, dernier numéro, prises de position | « Actualité » |
| **Publications** | Tous les numéros de CPS (couverture, sommaire, PDF), par année | « Bulletins » et « Publications » |
| **Textes** | Recherche dans les archives + textes fondamentaux + pages par thème | « Textes fondamentaux », « Publications », index |
| **Qui sommes-nous** | Présentation, histoire, conférences, CJR, liens | « Qui sommes-nous ? » et « Liens » |
| Bouton **S'abonner** | Abonnement, liste de diffusion, contact | « Abonnements et contacts » |

On passe de 6 onglets + 1 lien caché à **4 onglets + 1 bouton**, avec une **loupe** toujours visible.

### Priorité 1 : couleurs et accessibilité (réglages du thème Kadence, sans toucher aux contenus)
1. Remplacer **toutes les couleurs** par la palette ci-dessus dans *Apparence → Personnaliser → Couleurs* : boutons rouges `#C8102E`, plus de bleu, plus de saumon.
2. Rendre le **contour de focus visible** (désactiver « hide focus outline »).
3. Ajouter le lien **« Aller au contenu »**.
4. Agrandir les **zones cliquables** à 44 px au moins (le minimum légal est de 24 px).
5. Un **seul `h1`** par page ; titres des cartes en `h2`/`h3`.

### Priorité 2 : en-tête, menu, pied de page
6. En-tête sur **une ligne** : logo + nom à gauche, 4 onglets, loupe, bouton S'abonner. Devise de Lénine déplacée en **pied de page**.
7. Sur mobile : logo + nom + loupe + menu sur **une seule ligne** de 64 px (contre ~300 px aujourd'hui).
8. Pied de page sombre, avec l'inscription à la liste de diffusion, l'abonnement, le contact et la page « Accessibilité ».

### Priorité 3 : page d'accueil
9. **À la une** : une seule publication en grand, dont le **titre est le mot d'ordre** et non « Supplément à CPS n° 98 ». Le numéro passe en surtitre.
10. **Dernier numéro** : bloc dédié (couverture, éditorial, sommaire, deux boutons), placé **juste après** la une, y compris sur mobile.
11. **Prises de position** : 3 cartes avec photo, puis une liste sobre (date, type, titre, chapô).
12. **Explorer les archives** : champ de recherche + thèmes fréquents avec leur nombre de textes.
13. Supprimer le carrousel s'il existe encore, et les résumés tout en gras.

### Priorité 4 : contenus (avec le chantier « structure »)
14. **Retitrer les suppléments** avec leur mot d'ordre (une cinquantaine de textes récents).
15. Remplacer les **cartes HTML écrites à la main** (`odtp-profile-card`, styles en ligne) par un **modèle unique**.
16. Mettre les **dates de parution réelles**.
17. Ajouter les **taxonomies** et le **moteur de recherche** décrits en partie 2.
18. Mettre progressivement **le texte des éditoriaux et déclarations en HTML**, PDF en téléchargement.

### Typographie
- **Titres et interface** : police système sans empattement (déjà installée sur chaque appareil, rien à télécharger, aucun appel à Google Fonts, donc pas de question RGPD).
- **Textes longs et chapôs** : police à empattements, pour une lecture de presse plus confortable.
- Corps de texte à **17 px**, interligne 1,6, lignes de **65 à 75 caractères** au maximum.

---

## 4. Vérifications faites sur la maquette

- **Test automatique axe-core (WCAG 2.2 AA)** : **0 erreur** sur la maquette (accueil, recherche, menu mobile ouvert). Le site actuel en compte une (zones cliquables trop petites) sur l'accueil et sur Bulletins.
- **Contrastes** : tous calculés ci-dessus.
- **Mobile (iPhone 13)** : en-tête sur une ligne, menu déroulant accessible (`aria-expanded`), pas de défilement horizontal.
- **Limite** : un test automatique ne détecte qu'une partie des problèmes, environ un tiers selon les estimations courantes. Il faudra un test manuel au clavier et avec un lecteur d'écran (NVDA, VoiceOver) sur le site réel.

La maquette utilise de vrais textes et de vraies photos du site. Les étiquettes des cartes (« Jeunesse », « Lycées », « École ») et le texte de la légende photo sont des exemples.
