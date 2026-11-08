"""Génère les pages intérieures de la maquette avec un en-tête et un pied communs."""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1])

NAV = [("index.html", "Accueil"), ("publications.html", "Publications"),
       ("textes.html", "Textes"), ("qui-sommes-nous.html", "Qui sommes-nous")]

def entete(actif):
    items = "\n".join(
        '          <li><a href="%s"%s>%s</a></li>' % (h, ' aria-current="page"' if h == actif else "", t)
        for h, t in NAV)
    cur = lambda f: ' aria-current="page"' if actif == f else ""
    return """  <a class="lien-evitement" href="#contenu">Aller au contenu</a>
  <header class="bandeau">
    <div class="conteneur bandeau-int">
      <p class="bandeau-surtitre">Groupe pour la construction du parti ouvrier révolutionnaire, la construction de l'Internationale ouvrière révolutionnaire</p>
      <a class="bandeau-marque" href="index.html">
        <img class="bandeau-logo" src="img/logo.jpg" alt="" width="120" height="120">
        <span class="bandeau-textes">
          <span class="bandeau-titre">Combattre pour le socialisme</span>
          <span class="bandeau-citation">« On ne peut aller de l'avant si l'on craint d'aller au socialisme » (Lénine)</span>
        </span>
      </a>
    </div>
    <nav class="barre-onglets" aria-label="Navigation principale">
      <div class="conteneur barre-int">
        <button class="bouton-menu" type="button" aria-expanded="false" aria-controls="onglets">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18" stroke-linecap="round"/></svg>
          Menu
        </button>
        <ul class="onglets" id="onglets">
ITEMS
        </ul>
        <a class="onglet-abonner" href="abonnement.html"CURA>S'abonner</a>
      </div>
    </nav>
  </header>""".replace("ITEMS", items).replace("CURA", cur("abonnement.html"))


PIED = '''  <script>
    const btn = document.querySelector('.bouton-menu');
    const nav = document.getElementById('onglets');
    btn.addEventListener('click', () => {
      const ouvert = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!ouvert));
      nav.classList.toggle('ouvert', !ouvert);
    });
    document.querySelectorAll('form').forEach(f => f.addEventListener('submit', e => {
      if (!f.getAttribute('action')) e.preventDefault();
    }));
  </script>'''

def page(fichier, actif, titre, description, corps):
    html = f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titre} — Combattre pour le socialisme</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
{entete(actif)}

  <main id="contenu">
{corps}
  </main>

{PIED}
</body>
</html>
'''
    (OUT / fichier).write_text(html, encoding="utf-8")

# ------------------------------------------------------------------ ARTICLE
P = lambda t: f"        <p>{t}</p>"
article = '''    <article class="section">
      <div class="conteneur article">
        <header class="article-entete">
          <p class="surtitre">Supplément au n° 98 · Déclaration · <time datetime="2026-11-01">1<sup>er</sup> novembre 2026</time></p>
          <h1 class="titre-page">Pour défaire le gouvernement Macron-Lecornu-Nuñez : manifestation centrale à l'Assemblée nationale</h1>
          <p class="meta" style="margin:0">Sur les mots d'ordre :</p>
          <ul class="mots-ordre">
            <li>À bas le projet de budget 2027 !</li>
            <li>À bas la répression !</li>
            <li>Satisfaction des revendications !</li>
          </ul>
          <div class="barre-article">
            <a class="bouton bouton--contour" href="#">Télécharger le PDF (2 pages)</a>
            <span class="meta">Thèmes : <a href="publications.html">Budget</a>, <a href="publications.html">Jeunesse</a>, <a href="publications.html">Libertés démocratiques</a></span>
          </div>
        </header>

        <div class="article-corps">
''' + "\n".join([
P("Le 24 octobre, et même encore le 31, malgré les interdictions de manifester, les modifications de trajet, la peur des violences policières, les gazages de cortèges et les nasses, des centaines de milliers de jeunes et travailleurs ont déferlé à nouveau pour défendre le droit de manifester et les libertés démocratiques contre le gouvernement."),
"          <h2>La jeunesse, les travailleurs se dressent contre la situation que le capitalisme leur destine</h2>",
P("Leur détermination est à la hauteur de la profondeur de la révolte de la jeunesse contre l'avenir que lui préparent la bourgeoisie et le gouvernement Macron-Lecornu : le saccage de l'école publique et la remise en cause du droit aux études pour financer les budgets d'armement, l'emploi précaire comme seule perspective, la militarisation et le renforcement du caractère policier de l'État. Dès le début, le gouvernement Macron-Lecornu a mesuré le danger de cette mobilisation lycéenne et l'a immédiatement réprimée avec une férocité inouïe. L'explosion du nombre de gardes à vue, les mutilations, les arrestations arbitraires et les lourdes condamnations judiciaires ont pour objectif de terroriser la jeunesse et les travailleurs. Les fermetures administratives des universités se multiplient dans le but d'interdire aux étudiants de se réunir, de se mobiliser."),
P("Cette détermination est aussi le fait des travailleurs qui ont vu dans la mobilisation de la jeunesse lycéenne, l'engagement d'un véritable combat, tranchant avec les sempiternelles journées d'actions impuissantes des appareils syndicaux."),
P("Ce mouvement de fond touche de nombreux pays d'Europe. Sous des formes diverses : en Albanie, en Italie, en Grèce, en Belgique, en Espagne et au Portugal, la jeunesse et les travailleurs se révoltent et manifestent contre le sort que leur réservent les bourgeoisies décadentes."),
"          <h2>Le gouvernement Macron-Lecornu fait l'unité des partis bourgeois au nom de l'ordre</h2>",
P("Le gouvernement a déchaîné une répression policière d'autant plus féroce que la bourgeoisie n'a aucune réponse positive à apporter. Soutenus par le RN, les partis bourgeois veulent incarner le « parti de l'ordre », couvrir les violences policières et interdire les manifestations."),
P("Le Sénat vient d'adopter le projet de loi « casseurs-payeurs » avec les voix des partis de la réaction (EPR, LR, RN, Horizons, MODEM). Ce projet scélérat vise à faire payer aux manifestants les dégradations commises, même s'ils n'en sont pas responsables."),
"          <h2>À bas le projet de budget 2027 !</h2>",
P("Le projet de budget pour 2027 concentre toute la politique de Macron avec des milliards en plus pour l'armée et la police, pour le remboursement de la dette et les aides aux capitalistes et des milliards en moins pour l'éducation, la santé, le logement et les salaires des fonctionnaires."),
"          <h2>Imposer la rupture avec le gouvernement</h2>",
P("C'est pourquoi les travailleurs et la jeunesse ont à s'organiser pour surmonter l'obstacle de la politique des directions syndicales qui ne veulent surtout pas affronter le gouvernement. Il faut que le mouvement de la jeunesse se structure avec la tenue de véritables assemblées générales qui élisent leurs délégués, pour imposer aux directions syndicales CGT, FO et FSU qu'elles appellent avec les organisations de la jeunesse à :"),
'''          <div class="encadre">
            <p style="margin:0"><strong>une puissante manifestation centrale à l'Assemblée nationale</strong>, pour faire capituler le gouvernement Macron-Lecornu et infliger une défaite aux partis de la réaction, en exigeant :</p>
            <ul>
              <li>À bas le projet de budget 2027 !</li>
              <li>À bas Parcoursup, à bas la sélection à l'université ;</li>
              <li>À bas la répression ! Pour la défense de la liberté de manifester ;</li>
              <li>À bas le projet de loi anti-manifestation « casseurs-payeurs ».</li>
            </ul>
          </div>''',
"          <h2>Quelle issue politique ?</h2>",
P("Pour les prolétariats et la jeunesse en Europe, il n'y a pas de véritable issue en dehors de l'expropriation du capital, la constitution de gouvernements ouvriers qui se fixent pour tâche d'aller vers les États-Unis socialistes d'Europe. C'est ce pourquoi combattent les militants du Groupe pour la construction du POR et de l'IOR."),
]) + '''
          <p class="meta"><em>Extraits. Le texte complet figure dans le PDF.</em></p>
        </div>

        <footer class="article-pied">
          <p class="surtitre">À lire aussi</p>
          <ul class="liste-liens">
            <li><a href="index.html#journal">Le n° 98 de Combattre pour le socialisme (1<sup>er</sup> octobre 2026)</a></li>
            <li><a href="publications.html">Inconditionnellement du côté de la mobilisation lycéenne et de ses revendications</a></li>
          </ul>
        </footer>
      </div>
    </article>'''
page("article.html", "", "Pour défaire le gouvernement Macron-Lecornu-Nuñez",
     "Supplément au n° 98 de Combattre pour le socialisme, 1er novembre 2026.", article)

# ------------------------------------------------------------------ QUI SOMMES-NOUS
qui = '''    <div class="section">
      <div class="conteneur">
        <h1 class="titre-page">Qui sommes-nous ?</h1>
        <div class="colonnes">
          <div>
            <p class="intro">Le Groupe pour la construction du parti ouvrier révolutionnaire, de l'Internationale ouvrière révolutionnaire, publie le bulletin <cite>Combattre pour le socialisme</cite>. Il est l'héritier politique du Comité fondé par Stéphane Just en 1984.</p>
            <blockquote class="citation">
              <p style="margin:0">« Il n'est plus question aujourd'hui, comme au XIX<sup>e</sup> siècle, d'assurer simplement un développement plus rapide et plus sain de la vie économique : il s'agit aujourd'hui de sauver l'humanité du suicide. »</p>
              <footer>Léon Trotsky, <cite>Manifeste d'alarme</cite>, 1940</footer>
            </blockquote>
            <div class="article-corps">
              <p>L'humanité est à nouveau brutalement confrontée à la barbarie capitaliste sous toutes ses formes : militarisme et guerre, nouveaux développements de la misère et de la famine, liquidation de tous les acquis ouvriers, destruction des conditions naturelles indispensables à l'existence humaine. Pour sauver l'humanité du suicide, rien n'est plus indispensable et urgent que de combattre pour le socialisme. Cela ne peut se faire sans construire le parti ouvrier révolutionnaire.</p>
              <p>Plus que jamais, la crise de l'humanité se réduit à la crise de la direction révolutionnaire. Il est impossible d'œuvrer à la résolution de cette crise sans combattre inlassablement contre la politique de soumission-collaboration des directions syndicales avec la bourgeoisie et ses gouvernements.</p>
              <p>Le Groupe constate que la IV<sup>e</sup> Internationale a été détruite comme organisation révolutionnaire. Mais les acquis politiques de la IV<sup>e</sup> Internationale, comme ceux des I<sup>re</sup>, II<sup>e</sup> et III<sup>e</sup> Internationales, demeurent plus que jamais vivants.</p>
            </div>

            <p style="margin-top:2rem"><a class="bouton bouton--contour" href="textes.html">Textes fondamentaux et conférences</a></p>

            <h2 id="cjr" style="margin-top:2.5rem">Cercle de jeunes révolutionnaires (CJR)</h2>
            <p>Le CJR regroupe les jeunes pour qui le combat pour le socialisme est une nécessité absolue. Aux côtés de la classe ouvrière, il s'engage dans la construction de l'organisation révolutionnaire de la jeunesse. Il publie le bulletin <cite>Socialisme ou Barbarie</cite>.</p>
            <p>Contact : <a href="mailto:cjr.mtp@gmail.com">cjr.mtp@gmail.com</a></p>
          </div>

          <aside aria-labelledby="histoire">
            <h2 id="histoire" style="font-size:1.25rem">Repères</h2>
            <ol class="frise">
              <li><strong>1984</strong> Exclusion de Stéphane Just du PCI ; fondation du Comité et premier numéro du bulletin.</li>
              <li><strong>1991</strong> VI<sup>e</sup> conférence : le PCI et la IV<sup>e</sup> Internationale-CIR détruits comme organisations trotskystes.</li>
              <li><strong>1997</strong> « Une nouvelle perspective », après le rétablissement du capitalisme en Russie.</li>
              <li><strong>2000</strong> Fondation du Cercle.</li>
              <li><strong>2007</strong> Fusion du Cercle et du Comité : naissance du Groupe.</li>
              <li><strong>2026</strong> VII<sup>e</sup> conférence du Groupe.</li>
            </ol>
            <h2 id="liens" style="font-size:1.25rem;margin-top:2rem">Liens</h2>
            <ul class="liste-liens">
              <li><a href="http://www.combatepelosocialismo.com.br/">Combate pelo socialismo</a> (Brésil)</li>
              <li><a href="http://maghrebsocialiste.free.fr/">Maghreb socialiste</a></li>
              <li><a href="http://www.frontunique.com/">Courant Front unique</a> (enseignement public)</li>
              <li><a href="https://www.marxists.org/francais/just/index.htm">Textes de Stéphane Just</a> (marxists.org)</li>
            </ul>
          </aside>
        </div>
      </div>
    </div>'''
page("qui-sommes-nous.html", "qui-sommes-nous.html", "Qui sommes-nous ?",
     "Présentation du Groupe pour la construction du parti ouvrier révolutionnaire et du Cercle de jeunes révolutionnaires.", qui)

# ------------------------------------------------------------------ ABONNEMENT
abo = '''    <div class="section">
      <div class="conteneur">
        <h1 class="titre-page">S'abonner, nous contacter</h1>
        <p class="intro">Soutenez notre action : abonnez-vous au bulletin, ou recevez gratuitement nos publications par courriel.</p>
        <div class="offres">
          <section class="offre offre--mise-en-avant" aria-labelledby="o1">
            <h2 id="o1">Abonnement au bulletin</h2>
            <p class="prix">30 € <span>pour dix numéros</span></p>
            <p style="margin:0">Chèque à l'ordre de <strong>A.E.P.S.</strong>, à envoyer à :</p>
            <address class="adresse">A.E.P.S.<br>1 bis, rue Gutenberg<br>93100 Montreuil</address>
          </section>
          <section class="offre" id="anciens" aria-labelledby="o2">
            <h2 id="o2">Anciens numéros</h2>
            <p class="prix">2 € <span>le numéro</span></p>
            <p style="margin:0">4 € pour le numéro spécial Stéphane Just. Commande à la même adresse.</p>
          </section>
          <section class="offre" aria-labelledby="o3">
            <h2 id="o3">Liste de diffusion</h2>
            <p class="prix">Gratuit</p>
            <form>
              <label for="courriel-abo" style="display:block;margin-bottom:.4rem">Adresse électronique</label>
              <input class="champ" id="courriel-abo" type="email" autocomplete="email" placeholder="nom@exemple.fr">
              <button class="bouton" type="submit" style="width:100%;margin-top:.75rem">M'inscrire</button>
            </form>
          </section>
        </div>
        <section id="contact" aria-labelledby="c" style="margin-top:3rem;max-width:var(--texte)">
          <h2 id="c">Contact</h2>
          <p>Pour toute question, ou pour recevoir la copie électronique d'anciens articles qui ne sont pas en ligne, écrivez-nous : <a href="mailto:socialisme@free.fr">socialisme@free.fr</a></p>
          <p>Jeunesse (CJR) : <a href="mailto:cjr.mtp@gmail.com">cjr.mtp@gmail.com</a></p>
        </section>
      </div>
    </div>'''
page("abonnement.html", "abonnement.html", "S'abonner, nous contacter",
     "Abonnement au bulletin Combattre pour le socialisme, liste de diffusion et contact.", abo)


# ------------------------------------------------------------------ ACCUEIL
def entree(date_iso, date, type_, titre, chapo="", sommaire=None, lien="article.html"):
    som = ""
    if sommaire:
        som = '\n              <ul class="entree-sommaire">' + "".join(f'<li><a href="{lien}">{x}</a></li>' for x in sommaire) + "</ul>"
    ch = f"\n              <p>{chapo}</p>" if chapo else ""
    return f"""          <li>
              <p class="entree-tete"><span class="entree-type">{type_}</span> <time class="entree-date" datetime="{date_iso}">{date}</time></p>
              <h3 class="titre-resultat"><a href="{lien}">{titre}</a></h3>{ch}{som}
              <p class="entree-liens"><a href="{lien}">Lire</a> · <a href="#">PDF</a></p>
          </li>"""

entrees = "\n".join([
  entree("2026-11-02", "2 novembre 2026", "Supplément à <cite>Socialisme ou Barbarie</cite> · CJR",
         "Pour satisfaire nos revendications et défaire le gouvernement, une manifestation centrale et unitaire à l'Assemblée nationale est nécessaire !",
         "Contre la division : imposons cette manifestation à toutes les organisations lycéennes et étudiantes !"),
  entree("2026-11-01", "1<sup>er</sup> novembre 2026", "Supplément au n° 98",
         "Pour défaire le gouvernement Macron-Lecornu-Nuñez : manifestation centrale à l'Assemblée nationale",
         "À bas le projet de budget 2027 ! À bas la répression ! Satisfaction des revendications !"),
  entree("2026-10-05", "5 octobre 2026", "Supplément au n° 98 · Lycées",
         "Inconditionnellement du côté de la mobilisation lycéenne et de ses revendications",
         "Contre le gouvernement et la répression qu'il déchaîne sur les lycéens. À bas le projet de budget !"),
  entree("2026-10-05", "5 octobre 2026", "Supplément au n° 98 · Enseignement public",
         "Pour obtenir des moyens pour l'École publique et l'abrogation de Parcoursup : à bas le budget d'austérité de l'Éducation nationale 2027 !"),
  entree("2026-10-01", "1<sup>er</sup> octobre 2026", "<strong>Combattre pour le socialisme n° 98</strong> (nouvelle série)",
         "Éditorial : Le programme du MEDEF et de tous les partis bourgeois : démanteler les conquêtes des travailleurs et jeunes, les écraser",
         "", ["Après le 54<sup>e</sup> congrès confédéral, où va la CGT ?",
              "Les militants interviennent et informent C.P.S. : enseignement public, Cercle de jeunes révolutionnaires",
              "Bolivie : une défaite pour le prolétariat dont la direction de la COB porte l'écrasante responsabilité",
              "Cuba assiégé par l'impérialisme, la bureaucratie accélère le processus de restauration du capital"]),
  entree("2026-05-30", "30 mai 2026", "Supplément au n° 97",
         "À bas les crédits militaires et la militarisation !",
         "Face à l'offensive ultra-réactionnaire de la bourgeoisie, quelle issue pour les travailleurs et la jeunesse ?"),
  entree("2026-04-30", "30 avril 2026", "<strong>Combattre pour le socialisme n° 97</strong> (nouvelle série) · numéro spécial",
         "Rapport sur la situation internationale adopté par la VII<sup>e</sup> conférence du Groupe : contre l'impérialisme qui enfonce l'humanité dans le chaos, la seule alternative est le combat pour le socialisme"),
  entree("2026-04-10", "10 avril 2026", "Déclaration · Supplément au n° 96",
         "À bas la proposition de loi Yadan !",
         "Front unique des organisations du mouvement ouvrier pour le retrait de cette proposition de loi, pour la défense des libertés démocratiques."),
  entree("2026-03-07", "7 mars 2026", "Déclaration · Supplément au n° 96",
         "Inconditionnellement du côté de l'Iran, du peuple palestinien, des peuples du Moyen-Orient",
         "Contre l'impérialisme américain et l'État d'Israël. Contre Macron et son gouvernement."),
  entree("2026-02-28", "28 février 2026", "<strong>Combattre pour le socialisme n° 96</strong> (nouvelle série)",
         "Éditorial : L'adoption du budget 2026 : un pas décisif pour le gouvernement, une défaite sans combat pour le prolétariat"),
])

ACCUEIL = """    <h1 class="visuellement-cache">Combattre pour le socialisme : accueil</h1>
    <section class="section" aria-labelledby="dernieres">
      <div class="conteneur">
        <h2 class="titre-section" id="dernieres">Dernières publications <a href="publications.html">Toutes les publications</a></h2>
        <ol class="liste-textes liste-chrono">
ENTREES
        </ol>
      </div>
    </section>""".replace("ENTREES", entrees)
page("index.html", "index.html", "Accueil",
     "Bulletin et prises de position du Groupe pour la construction du parti ouvrier révolutionnaire. Archives depuis 1984.", ACCUEIL)


# ------------------------------------------------------------------ PUBLICATIONS (liste + recherche)
def groupe_filtres(titre, ident, items):
    lis = "\n".join(f'            <li><a href="publications.html">{t} <span class="nombre">{n}</span></a></li>' for t, n in items)
    return f"""          <h3 class="filtre-titre" id="{ident}">{titre}</h3>
          <ul class="liens-filtres" aria-labelledby="{ident}">
{lis}
          </ul>"""

FILTRES = "\n".join([
    groupe_filtres("Thèmes", "f-themes", [
        ("Enseignement public", 220), ("Retraites", 37), ("Budget, finances publiques", 35),
        ("Sécurité sociale", 24), ("Fonction publique", 19), ("Syndicats et dialogue social", 18),
        ("Libertés démocratiques", 16), ("Guerre impérialiste", 19), ("Crise du capitalisme", 22),
        ("Palestine", 37), ("Algérie", 45)]),
    groupe_filtres("Type de texte", "f-type", [
        ("Numéros du bulletin", 199), ("Éditoriaux", 152), ("Suppléments, tracts", 159),
        ("Déclarations", 90), ("On nous communique", 52), ("Communiqués", 18)]),
    groupe_filtres("Organisation citée", "f-org", [
        ("FSU", 110), ("CGT", 71), ("Force ouvrière", 54), ("FEN", 40), ("UNEF", 33), ("PS", 31), ("PCF", 21)]),
    groupe_filtres("Période", "f-periode", [
        ("2020 – 2026", 156), ("2010 – 2019", 274), ("2000 – 2009", 248), ("1984 – 1999", 548)]),
])

PUBLICATIONS = """    <div class="section">
      <div class="conteneur">
        <h1 class="titre-page">Publications</h1>
        <form class="recherche-bloc" role="search" action="publications.html">
          <label class="visuellement-cache" for="q">Rechercher dans les publications</label>
          <input class="champ" id="q" name="q" type="search" placeholder="Un mot, un nom, un thème… (ex. : retraites, FSU, Palestine)">
          <button class="bouton" type="submit">Rechercher</button>
        </form>

        <div class="mise-en-page-recherche" style="margin-top:2rem">
          <nav class="filtres" aria-label="Filtrer les publications">
FILTRES
          </nav>

          <div>
            <p role="status" class="resultats-entete" style="margin-top:0"><span><strong>1 226 textes</strong>, du plus récent au plus ancien</span></p>
            <ol class="liste-textes liste-chrono">
ENTREES
            </ol>
            <nav aria-label="Pagination">
              <ul class="pagination">
                <li><span aria-current="page">1</span></li>
                <li><a href="#">2</a></li>
                <li><a href="#">3</a></li>
                <li><a href="#">…</a></li>
                <li><a href="#">123</a></li>
                <li><a href="#" style="padding:0 1rem">Suivant</a></li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>""".replace("FILTRES", FILTRES).replace("ENTREES", entrees)
page("publications.html", "publications.html", "Publications",
     "Tous les numéros et suppléments de Combattre pour le socialisme depuis 1984, avec recherche par thème.", PUBLICATIONS)

# ------------------------------------------------------------------ TEXTES (textes de référence)
def bloc(titre, items):
    lis = "\n".join(f'            <li><a href="#">{t}</a>{(" <span class=\"meta\">— " + m + "</span>") if m else ""}</li>' for t, m in items)
    return f"""        <h2 class="titre-section" style="margin-top:2.5rem">{titre}</h2>
        <ul class="liste-liens">
{lis}
        </ul>"""

TEXTES = """    <div class="section">
      <div class="conteneur" style="max-width:52rem">
        <h1 class="titre-page">Textes</h1>
        <p class="intro">Les textes de référence du Groupe, les rapports adoptés par ses conférences et les textes fondateurs du Comité (1984-1997).</p>
""" + "\n".join([
    bloc("Textes fondamentaux", [
        ("Programme de transition", "Léon Trotsky, 1938"),
        ("Les syndicats à l'époque de la décadence de l'impérialisme", "Léon Trotsky, 1940 ; préface de Stéphane Just, 1972"),
        ("La lutte pour l'émancipation des femmes, une composante essentielle du combat pour le socialisme", ""),
        ("Une nouvelle perspective", "IX<sup>e</sup> conférence du Comité, 1997"),
    ]),
    bloc("Conférences du Groupe (depuis 2007)", [
        ("Rapport sur la situation internationale", "VII<sup>e</sup> conférence, avril 2026 (CPS n° 97)"),
        ("Rapport sur la situation internationale", "V<sup>e</sup> conférence, 15-17 avril 2017"),
        ("Rapport sur la situation internationale", "3<sup>e</sup> conférence, 27 mai 2012 (CPS n° 47)"),
        ("Rapport international", "2<sup>e</sup> conférence, 11-13 avril 2009 (CPS n° 37)"),
        ("Rapport international", "1<sup>re</sup> conférence, avril 2007 (CPS n° 29)"),
        ("Résolution adoptée par la première conférence du Groupe", "9 avril 2007"),
    ]),
    bloc("Du Comité au Cercle (2000)", [
        ("Œuvrer à la construction du parti ouvrier révolutionnaire", "texte fondant le Cercle, bilan de la crise du Comité après le décès de Stéphane Just"),
    ]),
    bloc("Le Comité (1984-1997)", [
        ("Contribution à la discussion préparatoire du XXVIII<sup>e</sup> congrès du PCI", "Stéphane Just, 1984"),
        ("Où en est et où va la direction du PCI", "Stéphane Just, juillet 1984"),
        ("Comment le révisionnisme s'est emparé de la direction du PCI", "Stéphane Just, 27 août 1984"),
        ("Pourquoi ce bulletin", "CPS n° 1, octobre 1984"),
        ("1985 : une année cruciale. Éléments pour un programme d'action", "Stéphane Just"),
        ("Contribution à la conférence de la IV<sup>e</sup> Internationale (CIR)", "21 décembre 1990"),
        ("Rapport adopté par la VI<sup>e</sup> conférence du Comité", "1<sup>er</sup>-3 novembre 1991"),
        ("Lambert et ses « amis » « reproclament la IV<sup>e</sup> Internationale »", "supplément au n° 50, décembre 1993"),
        ("Complète dégénérescence", "supplément au n° 55, février 1995"),
        ("La politique du CCI-PT et de sa prétendue « IV<sup>e</sup> internationale » : un nouveau social-patriotisme", "2006"),
    ]),
]) + """
      </div>
    </div>"""
page("textes.html", "textes.html", "Textes",
     "Textes fondamentaux et rapports de conférence du Groupe pour la construction du parti ouvrier révolutionnaire.", TEXTES)

print("ok")
