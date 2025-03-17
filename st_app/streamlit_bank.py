import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io

##############################################################################
# PAGE SOMMAIRE
##############################################################################
st.sidebar.title("Sommaire")

pages = [
    "Le projet",
    "Extraction des données",
    "Exploration & Pré-traitement des données",
    "Analyse des données",
    "Modélisation & Prédictions",
    "Conclusion"
]

page = st.sidebar.radio("Aller à la page:", pages)

st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")

# Ajout des noms avec le logo LinkedIn cliquable(Mettre des balise pour separer les objets)

st.sidebar.markdown(r"""
**Groupe :**  
<a href="https://www.linkedin.com/in/matthieu-karr-6856a93a/" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="20" style="vertical-align:middle;margin-right:10px;">Matthieu Karr</a>  
<a href="https://www.linkedin.com/in/catherine-otieno-0537b9157/" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="20" style="vertical-align:middle;margin-right:10px;">Catherine Otieno</a>  
<a href="https://www.linkedin.com/in/ielhasnaoui-photonicsengineer/" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="20" style="vertical-align:middle;margin-right:10px;">Ikram El Hasnaoui</a>

**GitHub du projet :**  
<a href="https://github.com/noxmatt/mai24cds_satisfaction_client.git" target="_blank">
    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="20" style="vertical-align:middle;margin-right:10px;">mai24cds_satisfaction_client</a>

**Promotion :** Mai 24 CDS  
**Tuteur :** Sébastien Sime  
**Date de Soutenance :** 18 Mars 2025""", unsafe_allow_html=True)


##############################################################################
# PAGE 0
##############################################################################

if page == pages[0]:
    
    st.image("st_app/satisfaction.jpg", width=500)
    st.title("Analyse et Prédiction de la Satisfaction Client")

    st.markdown("""
    **Dans le cadre de notre formation en Data Science chez DataScientest**, nous avons mené un projet intitulé *"Fil Rouge"*, visant à analyser et prédire la satisfaction client dans la supply chain, en nous focalisant sur les banques en ligne. Ce projet a pour objectif d’explorer les thématiques clés des avis clients pour mieux comprendre et anticiper leurs attentes.

    Pour ce faire, nous avons adopté une approche méthodologique rigoureuse, allant de la collecte des données à l’application de techniques avancées telles que le clustering et la modélisation thématique. Ces étapes nous ont permis de dégager des perspectives riches et captivantes, tout en mettant en pratique les compétences développées au cours de notre formation.

    Ce projet reflète notre engagement à explorer des problématiques concrètes et actuelles à travers le prisme de la data science. En vous plongeant dans cette aventure, vous découvrirez comment les données deviennent une source d’insights stratégiques, ouvrant la voie à des solutions impactantes pour le monde d’aujourd’hui et de demain.
    """)
    

##############################################################################
# PAGE 1
##############################################################################
elif page == pages[1]:
    st.title("Extraction et Préparation : Le Pouvoir du Webscraping")
    
    st.markdown("""
    ### Méthodologie : Extraction et Structuration des Données
    Dans le cadre de ce projet, nous avons choisi de nous concentrer sur la satisfaction des clients des banques en ligne en France, tout en veillant à développer une méthodologie transposable à d'autres secteurs.

    ### Source des données
    Nous avons sélectionné **TrustPilot** comme source principale, en raison de la disponibilité des avis vérifiés et de sa popularité auprès des utilisateurs. Cette plateforme constitue une véritable mine d’or pour les données orientées BtoC.

    ### Approche d'extraction
    Pour récupérer les données nécessaires, nous avons exploré trois outils de web scraping : 
    - **Scrapy** : Puissant, mais adapté aux projets nécessitant une gestion complexe de grandes quantités de données.
    - **Selenium** : Idéal pour interagir avec des pages dynamiques, mais plus lourd et lent.
    - **BeautifulSoup** : Solution retenue pour sa **simplicité** et son **efficacité** sur des pages statiques.

    Grâce à cette approche, nous avons pu structurer les données efficacement, posant ainsi les bases solides de notre analyse.
    """)
    st.image("st_app/data_scraping.gif")

    if st.checkbox(
        "Affichage du code : le Webscraping avec BeautifulSoup"
    ):
        web_beautiful = """
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import os
    import time

    def scrape_trustpilot(company_name, num_pages):
    reviews = []
    base_url = f"https://fr.trustpilot.com/review/{company_name}"


    for page in range(1, num_pages + 1):
        url = f"{base_url}?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        time.sleep(3)  # Attendre que la page se charge
        review_elements = soup.find_all("div", {"class": "styles_cardWrapper__LcCPA"})

        for review in review_elements:
            id_cust = review.find("span", {"class": "typography_heading-xxs__QKBS8 typography_appearance-default__AAY17"})
            verif= review.find("button", {"class": "styles_reviewLabelButton__SNIsL"})
            title_element = review.find("h2", {"class": "typography_heading-s__f7029"})
            rating_element_indiv = review.find("div", {"class": "styles_reviewHeader__iU9Px"})
            text_element = review.find("p", {"class": "typography_body-l__KUYFJ"})
            date_element = review.find("time")

            id_cust = id_cust.text.strip() if text_element else 'No Text'
            verif = verif.text.strip() if verif else 'Non vérifié'
            title = title_element.text.strip() if title_element else 'No Title'
            rating = rating_element_indiv['data-service-review-rating'] if rating_element_indiv and 'data-service-review-rating' in rating_element_indiv.attrs else 'No Rating'
            text = text_element.text.strip() if text_element else 'No Text'
            date = date_element['datetime'] if date_element else 'No Date'

            reviews.append({
                'company_name': company_name, 
                'title': title,
                'id_cust': id_cust,
                'verif': verif,
                'rating_indiv': rating,
                'commentaire': text,
                'date': date
            })

    return pd.DataFrame(reviews)"""
        st.code(web_beautiful, language="python")
    st.markdown("""
            Nous avons utilisé cette fonction pour extraire des avis pour chacune des entreprises de façon séparée. 
            Plusieurs motifs ont motivés ce choix:
            - séquencer le temps de traitement pouvant atteindre plus d'une heure pour certaines entreprises,
            - optimisation des ressources & répartition du travail (machine & temps) pour chaque membre du projet.
                
            Nous avons fusionné les différentes bases de données collectées pour obtenir un jeu de données global et uniforme.
            A la fin de cette étape nous avons récupéré un dataframe de 10 Colonnes et 188 759 lignes, contenant les avis 
            des banques suivantes :
                
            BoursoBank, BforBank, Fortuneo, HelloBank, N26, Quanto, Revolut, MonaBank, 
            OrangeBank, Oney, Nickel, MaFrenchBanque, Floabank, YounitedCredit et Cofidis"""
        )
    st.markdown("""
        ### Affichage des données brutes du Webscrapping""")

    df = pd.read_csv("st_app/df_bank.csv")
    st.dataframe(df.head())

    st.write("""Le web scraping doit être réalisé dans le respect des lois en vigueur
            ainsi que des conditions d’utilisation des sites web ciblés. Il est essentiel
            d’adopter une approche éthique, en veillant à ne pas surcharger les serveurs ni
            violer les droits des propriétaires des données."""
    )

##############################################################################
# PAGE 2
##############################################################################

elif page == pages[2]:
    st.title("Exploration & Pré-traitement des données")
    df = pd.read_csv("st_app/df_bank.csv")

        # Centrer l'image
    st.image("st_app/nettoyage-des-donnees.png", width=300, caption="")
        
    if st.checkbox("Afficher le DataFrame brut du scrapping"):
        st.dataframe(df.head(), width=1500)
    st.write(
        "Voici le jeux de données d'orignine, nous allons maintenant explorer et nettoyer"
        "les données pour les rendre exploitables. Nous touverons pour cela toutes les étapes réalisées dans la liste ci dessous :"
    )

    exploration = st.selectbox(
        label="Selection des etapes de transformations et d'ajout des données",
        options=[
            "Dimension du DataFrame",
            "Types de données",
            "Données statistiques",
            "Valeurs manquantes",
            "Affichage des doublons",
            "Corrections des noms d'entreprise",
            "Transformations en format date de la colonne date",
            "Création de la colonne avis_global (Regroupement du titre et de l'avis)",
            "Ajout des variables complémentaires",
        ],
    )

    import re

    def findLink(texte):
        r1 = re.compile(r"https?://[a-zA-Z0-9./]+")
        links = r1.findall(texte)
        r2 = re.compile(r"www\.[a-zA-Z0-9.-:/]+")
        links += r2.findall(texte)
        return len(links)

    def findMail(texte):
        r = re.compile(r"[a-zA-Z0-9.-]+@[a-zA-Z.]+")
        mails = r.findall(texte)
        return len(mails)

    def findQuote(texte):
        r = re.compile(r"@[a-zA-Z0-9]+")
        quote = r.findall(texte)
        return len(quote)

    def findHashtag(texte):
        r = re.compile(r"#[a-zA-Z0-9]+")
        hashtag = r.findall(texte)
        return len(hashtag)

    def findCAPSLOCK(texte):
        r = re.compile(r"[A-Z]")
        capslock = r.findall(texte)
        return len(capslock)

    def find_chain_CAPSLOCK(texte):
        r = re.compile(r"[A-Z]{2,}")
        capslock = r.findall(texte)
        return len(capslock)

    def find_exclamation(texte):
        r = re.compile(r"\!")
        exclamation = r.findall(texte)
        return len(exclamation)

    def find_chain_exclamation(texte):
        r = re.compile(r"\!{2,}")
        exclamation = r.findall(texte)
        return len(exclamation)

    def find_interogation(texte):
        r = re.compile(r"\?")
        interogation = r.findall(texte)
        return len(interogation)

    def find_etc(texte):
        r = re.compile(r"\.{2,}")
        etc = r.findall(texte)
        return len(etc)

    def traitement(exploration, df):
        if exploration == "Dimension du DataFrame":
            return df.shape

        elif exploration == "Types de données":
            buffer = io.StringIO()
            df.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)
            return None

        elif exploration == "Données statistiques":
            return df.describe()

        elif exploration == "Valeurs manquantes":
            return df.isna().sum()

        elif exploration == "Affichage des doublons":
            return df.duplicated(subset=["ID", "avis", "titre"]).sum()

        elif exploration == "Corrections des noms d'entreprise":
            df["company"] = df["Company Name"].map(
                {
                    "www.younited-credit.com": "Younited-Credit",
                    "cofidis.fr": "Cofidis",
                    "boursobank.com": "Boursorama",
                    "nickel.eu": "Nickel",
                    "orangebank.fr": "OrangeBank",
                    "qonto.com": "Qonto",
                    "floabank.fr": "FloaBank",
                    "n26.com": "N26",
                    "fortuneo.fr": "Fortuneo",
                    "www.revolut.com": "Revolut",
                    "www.monabanq.com": "Monabanq",
                    "oney.fr": "Oney",
                    "hellobank.fr": "Hellobank",
                    "www.mafrenchbank.fr": "MaFrenchBank",
                    "bforbank.com": "BforBank",
                }
            )
            return df["company"].unique()

        elif exploration == "Transformations en format date de la colonne date":
            df["Date"] = pd.to_datetime(df["Date"])
            return df.head()

        elif (
            exploration
            == "Création de la colonne avis_global (Regroupement du titre et de l'avis)"
        ):
            if "titre" in df.columns and "avis" in df.columns:
                df["avis_global"] = df["titre"] + " " + df["avis"]
            return df.head()

        elif exploration == "Ajout des variables complémentaires":
            df["avis_global"] = df["titre"] + " " + df["avis"]
            df["quotes"] = df["avis_global"].apply(lambda x: findQuote(x))
            df["hashtags"] = df["avis_global"].apply(lambda x: findHashtag(x))
            df["capslock"] = df["avis_global"].apply(lambda x: findCAPSLOCK(x))
            df["chain_capslock"] = df["avis_global"].apply(
                lambda x: find_chain_CAPSLOCK(x)
            )
            df["exclamation"] = df["avis_global"].apply(lambda x: find_exclamation(x))
            df["chain_exclamation"] = df["avis_global"].apply(
                lambda x: find_chain_exclamation(x)
            )
            df["interogation"] = df["avis_global"].apply(lambda x: find_interogation(x))
            df["etc"] = df["avis_global"].apply(lambda x: find_etc(x))
            df["message_len"] = df["avis_global"].apply(len)
            return df.head()

        return None

    # Appel de la fonction
    resultat = traitement(exploration, df)
    if resultat is not None:
        st.write(resultat)

    df_global = pd.read_csv("st_app/df_global.csv")
    if st.checkbox(
        "Afficher le DataFrame qui vient d'être nettoyé, corrigé, et enrichi de nouvelles colonnes"
    ):
        st.dataframe(df_global.head())

##############################################################################
# PAGE 3
##############################################################################
elif page == pages[3]:
    st.write("### Analyse des données")
    st.write("""Dans cette première exploration des avis clients, nous nous concentrons sur une vue d'ensemble visuelle pour repérer
            les principales tendances et insights. Cette approche initiale vise à identifier rapidement les éléments clés des retours
            clients et nous aider à comprendre nos données.""")

    df_global = pd.read_csv("st_app/df_global.csv")
    

    st.subheader("Nombre d'avis par année")
    fig, ax1 = plt.subplots()
    sns.countplot(data=df_global, x="year", ax=ax1)
    st.pyplot(fig)
    st.write(
        r"""Les commentaires analysés montrent une évolution notable du volume et des caractéristiques
        des avis clients au fil des années. Depuis 2017, une augmentation constante a été observée, avec
        des pics en 2022 et 2024, avant une baisse en 2023 liée probablement au retour à la normalité
        post-Covid et à un regain d’intérêt pour les banques traditionnelles."""
    )

    fig1, ax2 = plt.subplots()
    sns.countplot(x="month", data=df_global,ax=ax2)
    st.title("Volume des avis par mois")
    st.pyplot(fig1)
    st.write(
        r"""La répartition mensuelle des avis montre qu'environ 15 000 avis sont déposés en moyenne chaque mois,
             à l'exception du mois d'avril, qui est la meilleure période en termes de nombre d'avis déposés."""
    )

    df_global["rating"] = df_global["rating"].astype("category")
    df_global["rating_category"] = df_global["rating"]  # Copie de la colonne
    print(df_global["rating"].isna().sum())

    st.subheader("Distribution des Notes")
    fig2, ax3 = plt.subplots()
    sns.countplot(
        x="rating", data=df_global, hue="rating_category", palette="flare", ax=ax3
    )
    st.pyplot(fig2)
    st.write(
        r"""La note 5 est de loin la plus courante dans notre jeu de données.
            Nous examinons s'il existe des différences entre les entreprises en ce qui concerne ces notations."""
    )

    st.subheader("Distribution des avis par entreprise")
    fig3, ax4 = plt.subplots()
    sns.countplot(y="company", hue="rating", palette="flare", data=df_global, ax=ax4)
    st.pyplot(fig3)
    st.write(
        r"""En matière de satisfaction, la note de 5 domine largement, bien que des différences
        significatives apparaissent entre entreprises. Par exemple, certaines comme Oney ont une proportion plus
        élevée de notes négatives (1) par rapport à d’autres ayant des volumes d’avis similaires, comme Monabanq.
        Cela soulève des questions sur la corrélation entre les volumes d’avis et la qualité perçue.."""
    )

    st.write("### Analyse des notes en pourcentage")
    st.image(
        "st_app/percent_cum_rates.png", width=1500
    )
    st.write(
        r"""Ce graphique montre que le pourcentage de notation des entreprises varie en fonction du nombre total d'avis déposés.
             On constate que les scores 1 peuvent être plus ou moins élevés selon les entreprises, ce qui peut sembler être un problème lié aux volumes d'avis.
             Cependant, dans certains cas d'entreprises ayant presque le même volume d'avis, ce n'est pas le cas.
             Par exemple : Oney (5 227 avis) comptabilise 54% de notes 1 et 31% de la note 5 alors que Monabanq (5 535 avis) enregistre seulement 1
             graphique pourcentage cumulé par entreprise"""
    )

    st.write("### Longueur des avis")
    st.image("st_app/len_words.png", width=1500)
    st.write(
        r"""Nous constatons que la longueur des commentaires des clients satisfaits avec un score de 5 est très courte par rapport à ceux des clients insatisfaits.
             Cela confirme la corrélation négative observée sur la heatmap, et nous pouvons envisager d'utiliser cette variable pour améliorer notre modèle si nécessaire. """
    )

    st.write("### Word Cloud ou Nuage de Mots")
    col3, col4 = st.columns(2)
    with col3:
        st.image(
            "st_app/wordcloud_pos.png", width=1500
        )
    with col4:
        st.image(
            "st_app/wordcloud_neg.png", width=1500
        )
    st.write(
        r"""Pour les commentaires positifs, nous pouvons identifier quelques thèmes liés à un service clientèle rapide et de qualité, à une bonne expérience et même à des recommandations.

Pour les commentaires négatifs, les thèmes ne sont pas explicites, mais nous pouvons commencer à identifier des problèmes liés au service à la clientèle, etc. ....

Dans les deux catégories, il n'est pas facile d'identifier les sujets principaux et réels de satisfaction ou d'insatisfaction.
Pour aller plus loin, nous allons expérimenter d'autres méthodes telles que LDA et Bertopics.
graphique : deux nuages de mots (positif + négatif) """
    )
    st.markdown(
        r"""
        En conclusion, bien que les avis positifs soient majoritaires, l’hétérogénéité des performances
        entre entreprises et les thèmes non explicitement identifiés dans les avis négatifs soulignent des
        opportunités d’amélioration pour mieux répondre aux attentes des clients. L’analyse thématique approfondie
        pourrait guider des actions ciblées pour renforcer la satisfaction globale.""")

##############################################################################
# PAGE 4
##############################################################################

elif page == pages[4]:
    st.title("Modélisations & Prédictions")

    if st.checkbox("#Première modélisation -Modélisation avec vectorisation des mots"):
        texte = """Nous avons lancé une première modélisation sans prétraitement des mots afin 
        d’obtenir une base de comparaison. En respectant les recommandations de scikit-learn et en
        considérant plusieurs critères (taille, type, prédiction attendue, structure et format des données),
        nous avons choisi trois catégories de modèles supervisés :

- Naive Bayes : Utilisation de BernoulliNB et MultinomialNB, qui classifient les avis en supposant l’indépendance
des caractéristiques.

- KNN : Un système de vote où le label de classe majoritaire est déterminé parmi les « k » voisins les
plus proches dans l’espace des caractéristiques.

- Logistic Regression : Un modèle statistique visant à estimer la probabilité d’un événement à partir d’un ensemble
de variables indépendantes."""

        st.header("Modélisation avec vectorisation des mots")

        st.markdown(texte)

        df_global = pd.read_csv(
            "st_app/df_global.csv"
        )
        data_size = st.slider(
            "Sélectionnez la taille du jeu de données",
            min_value=100,
            max_value=len(df_global),
            value=50000,
            step=1000,
            key="slider_data_size1",
        )
        df_global = df_global.sample(n=data_size, random_state=42)

        df = df_global[["avis_global", "rating"]]

        X = df["avis_global"]
        y = df["rating"]

        # importation des bibliothèques
        from sklearn.model_selection import train_test_split
        from sklearn.naive_bayes import BernoulliNB, MultinomialNB
        from sklearn.linear_model import LogisticRegression
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import StandardScaler
        from sklearn.metrics import classification_report

        # découpage des données
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Définir les pipelines pour chaque modèle
        models = {
            "Bernoulli Naive Bayes": Pipeline(
                [
                    ("vectorizer", CountVectorizer()),
                    ("scaler", StandardScaler(with_mean=False)),
                    ("bernoulli", BernoulliNB()),
                ]
            ),
            "Multinomial Naive Bayes": Pipeline(
                [
                    ("vectorizer", CountVectorizer()),
                    ("scaler", StandardScaler(with_mean=False)),
                    ("multinomial", MultinomialNB()),
                ]
            ),
            "K-Nearest Neighbors": Pipeline(
                [
                    ("vectorizer", CountVectorizer()),
                    ("scaler", StandardScaler(with_mean=False)),
                    ("knn", KNeighborsClassifier(n_neighbors=3)),
                ]
            ),
            "Logistic Regression": Pipeline(
                [
                    ("vectorizer", CountVectorizer()),
                    ("scaler", StandardScaler(with_mean=False)),
                    ("lr", LogisticRegression(max_iter=200)),
                ]
            ),
        }

        # Sélection du modèle
        model_name = st.selectbox("Choisissez un modèle", list(models.keys()), key="1")
        model = models[model_name]

        # Entraîner le modèle sélectionné
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Afficher les résultats
        st.write(f"### {model_name}")
        st.text(classification_report(y_test, y_pred))

        # Afficher les scores de précision
        accuracy = model.score(X_test, y_test)
        st.write(f"Précision: {accuracy:.2f}")
        st.write(
            "Nous voyons que les resultats ne sont pas encore satisfaisants, nous allons donc essayer de les améliorer en utilisant la vectorisation des mots et la binarisation des notes."
        )

    # Binarisation des notes
    # on sépare les notes en 2 catégories (-1,1,)
    if st.checkbox("#Deuxième modélisation - binarization des notes"):
        st.write(
            "### Modélisation avec vectorisation des mots et Binarisation des notes"
        )

        df_global = pd.read_csv(
            "st_app/df_global.csv"
        )
        df_global = df_global[
            df_global.rating != 3
        ]  # enlever la note 3 du jeu de données car non significative en volume et dans l'entre deux
        df_global["rating_2"] = df_global.rating.replace(
            [1, 2, 3, 4, 5], [-1, -1, 1, 1, 1]
        )
        st.write(
            "Tranformationd des notes en deux catégories : -1 pour les notes négatives(1,2) et 1 pour les notes positives(4,5), supression de la note 3"
        )

        fig4, ax = plt.subplots()
        sns.countplot(
            x="rating_2", data=df_global, palette="flare", hue="rating_2", ax=ax
        )
        st.header("Distribution des Notes")
        st.pyplot(fig4)

        data_size = st.slider(
            "Sélectionnez la taille du jeu de données",
            min_value=100,
            max_value=len(df_global),
            value=50000,
            step=1000,
            key="slider_data_size2",
        )
        df_global = df_global.sample(n=data_size, random_state=42)
        df = df_global[["avis_global", "rating_2"]]
        X = df["avis_global"]
        y = df["rating_2"]

        # importation des bibliothèques
        from sklearn.model_selection import train_test_split
        from sklearn.naive_bayes import BernoulliNB, MultinomialNB
        from sklearn.linear_model import LogisticRegression
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import StandardScaler
        from sklearn.metrics import classification_report

        # découpage des données
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Définir les pipelines pour chaque modèle
        models = {
            "Bernoulli Naive Bayes": Pipeline(
                [
                    ("vectorizer", CountVectorizer()),
                    ("scaler", StandardScaler(with_mean=False)),
                    ("bernoulli", BernoulliNB()),
                ]
            ),
            "Multinomial Naive Bayes": Pipeline(
                [
                    ("vectorizer", CountVectorizer()),
                    ("scaler", StandardScaler(with_mean=False)),
                    ("multinomial", MultinomialNB()),
                ]
            ),
            "K-Nearest Neighbors": Pipeline(
                [
                    ("vectorizer", CountVectorizer()),
                    ("scaler", StandardScaler(with_mean=False)),
                    ("knn", KNeighborsClassifier(n_neighbors=3)),
                ]
            ),
            "Logistic Regression": Pipeline(
                [
                    ("vectorizer", CountVectorizer()),
                    ("scaler", StandardScaler(with_mean=False)),
                    ("lr", LogisticRegression(max_iter=200)),
                ]
            ),
        }
        # Sélection du modèle
        model_name = st.selectbox("Choisissez un modèle", list(models.keys()), key="2")
        model = models[model_name]

        # Entraîner le modèle sélectionné
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Afficher les résultats
        st.write(f"### {model_name}")
        st.text(classification_report(y_test, y_pred))

        # Afficher les scores de précision
        accuracy = model.score(X_test, y_test)
        st.write(f"Précision: {accuracy:.2f}")
        st.write(
            "Nous voyons que les resultats sont meilleurs, mais potentiellement nous souhaitons voir si nous pouvons améliorer le resultat en utilisant la binarisation des notes"
        )

    if st.checkbox("#Rééquilibrage des données"):
        st.markdown(r"""
        Pour équilibrer le dataframe nous utilisons deux approches complémentaires : le **suréchantillonnage** et le **sous-échantillonnage**.

        ---

        #### Suréchantillonnage (**Oversampling**)

        Cette méthode augmente la représentation des classes minoritaires en générant de nouveaux exemples. Trois techniques couramment utilisées sont :
        - **RandomOverSampler** : duplique certains échantillons minoritaires.
        - **SMOTE** (*Synthetic Minority Oversampling Technique*) : crée des exemples synthétiques en interpolant entre les voisins.
        - **ADASYN** (*Adaptive Synthetic Sampling*) : génère davantage d’exemples autour des cas mal classés.

        ---

        #### Sous-échantillonnage (**Undersampling**)

        Cette méthode réduit la taille des classes majoritaires. Par exemple, la technique **Tomek Links** identifie les échantillons majoritaires se trouvant à proximité immédiate des exemples minoritaires et les élimine, atténuant ainsi le déséquilibre.

        ---

        L’utilisation combinée de ces techniques améliore la robustesse et la fiabilité des modèles prédictifs tout en optimisant la performance et la précision des systèmes de classification.
        """)
        st.image("st_app/shema_rus_ros.png", width=1500)


        import pandas as pd
        import streamlit as st

        # Sélecteur de méthode de rééchantillonnage
        resampling_method = st.selectbox(
            "Sélectionnons à présent la méthode de rééchantillonnage testée",
            [
                "FunctionSampler",
                "RandomOverSampler",
                "ADASYN",
                "SMOTE",
                "RandomUnderSampler",
            ],
        )

        # Créer visuel en fonction de la méthode sélectionnée
        if resampling_method == "FunctionSampler":
            st.image("st_app/Fs_model1.png")
        elif resampling_method == "RandomOverSampler":
            st.image("st_app/ros_model1.png")
        elif resampling_method == "ADASYN":
            st.image("st_app/adasyn_model1.png")
        elif resampling_method == "SMOTE":
            st.image("st_app/smote_model1.png")
        elif resampling_method == "RandomUnderSampler":
            st.image("st_app/rus_model1.png")
        st.write("Nous remarquons que les méthodes RandomOverSampler et FunctionSampler sont les plus éfficaces pour rééquilibrer les données.")
        st.write("Testons àprésent ces deux méthodes pour voir laquelle est la plus perform avec un autre scaler")
                 
    if st.checkbox("#Optimisation du scaler"):
        st.markdown(r"""

            Après avoir équilibré les données, il est essentiel de normaliser leurs caractéristiques pour éviter tout biais
            lié aux écarts d'échelle. Le **MaxAbsScaler** est particulièrement adapté aux données textuelles vectorisées car :
            - Il **conserve la sparsité** des matrices, optimisant ainsi les performances.
            - Il **met à l'échelle proportionnellement** dans l'intervalle [-1, 1], préservant les proportions initiales.

            Passons maintenant au test du MaxAbsScaler et comparons les performances des deux méthodes de rééquilbrage retenus.
            """)
        
        import pandas as pd
        import streamlit as st
        from sklearn.metrics import classification_report
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import train_test_split
        from sklearn.feature_extraction.text import CountVectorizer
        from imblearn.pipeline import make_pipeline
        from sklearn.preprocessing import MaxAbsScaler
        from imblearn import FunctionSampler
        from imblearn.over_sampling import RandomOverSampler

        # Charger les données
        df_global = pd.read_csv(
            "st_app/df_global.csv"
        )
        df_global = df_global[df_global.rating != 3]
        df_global["rating_2"] = df_global.rating.replace(
            [1, 2, 3, 4, 5], [-1, -1, 1, 1, 1]
        )
        data_size = st.slider(
            "Sélectionnez la taille du jeu de données",
            min_value=100,
            max_value=len(df_global),
            value=50000,
            step=100,
            key="slider_data_size2",
        )
        df_global = df_global.sample(n=data_size, random_state=42)
        df = df_global[["avis_global", "rating_2"]]

        # Préparer les données
        X = df[["avis_global"]]
        y = df["rating_2"]

        vectorisation = CountVectorizer()
        X = vectorisation.fit_transform(X.values.ravel())

        # Diviser les données en ensembles d'entraînement et de test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Initialiser le classificateur
        classifier = LogisticRegression()
        scaler = MaxAbsScaler()

        # Sélecteur de méthode de rééchantillonnage
        resampling_method = st.selectbox(
            "Sélectionnez la méthode de rééchantillonnage",
            ["FunctionSampler", "RandomOverSampler"],
        )

        # Créer le pipeline en fonction de la méthode sélectionnée
        if resampling_method == "FunctionSampler":
            pipeline = make_pipeline(FunctionSampler(), scaler, classifier)
        elif resampling_method == "RandomOverSampler":
            pipeline = make_pipeline(
                RandomOverSampler(random_state=42), scaler, classifier
            )

        # Ajuster et évaluer le pipeline
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        st.write(f"Classification report for {resampling_method}:")
        st.text(classification_report(y_test, y_pred))
        st.write(
            "Nous voyons que les résultats sont bons avec ces deux méthodes, car leur accurancy est équivalente 0.97 et 0.96."
            " Maitenant tous dépend de ce que nous recherchons, concernant le recall (Faux Negatif ou positifs)."
            "Nous voyons que la méthode RandomOverSampler est plus performante pour les notes positives, tandis que la méthode FunctionSampler est plus performante pour les notes négatives"
            " les deux méthodes sont donc complémentaires."
        )

    if st.checkbox("#Optimisation des hyperparamètres"):
        st.header(
            """L'optimisation des hyperparamètres."""
        )

        if st.checkbox(
            "Affichage du code utilisé pour faire la recherche d'hyperparamètres"
        ):
            code_hyper = """
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import MaxAbsScaler, FunctionTransformer
    from sklearn.linear_model import LogisticRegression
    from imblearn.pipeline import Pipeline as ImbPipeline
    from imblearn.over_sampling import RandomOverSampler
    from imblearn import FunctionSampler

    df = pd.read_csv("st_app/df_global.csv")
    df = df[df.rating != 3]
    df['rating_2'] = df.rating.replace([1, 2, 3, 4, 5], [-1, -1, 1, 1, 1])

    # Séparation des features et du target
    X = df['avis_global']
    y = df['rating_2']

    # Transformation du texte en vecteur
    vectorisation = CountVectorizer()
    X = vectorisation.fit_transform(X.values.ravel())

    # Division des données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Définition des pipelines
    pipelines = [
        {
            'name': 'LogisticRegression',
            'pipeline': ImbPipeline([
                ('sampler', RandomOverSampler(random_state=42)),
                ('scaler', MaxAbsScaler()),
                ('classifier', LogisticRegression(random_state=42))
            ]),
            'param_grid': {
                'classifier__C': [0.001, 0.01, 0.1, 1.0, 2.0, 100],
                'classifier__solver': ['lbfgs', 'liblinear'],
                'classifier__max_iter': [200, 500, 1000, 2000]
            }
        }
    ]

    # Initialisation du dictionnaire des meilleurs paramètres
    best_params_dict = {}

    # Utilisation de GridSearch pour chaque pipeline (Modèle)
    for pipeline_dict in pipelines:
        name = pipeline_dict['name']
        pipeline = pipeline_dict['pipeline']
        param_grid = pipeline_dict['param_grid']

        grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
        grid_search.fit(X_train, y_train)

        print(f"--- {name} ---")
        print("Best parameters:", grid_search.best_params_)
        print("Best cross-validation score:", grid_search.best_score_)

        # Stockage des meilleurs paramètres dans le dictionnaire
        best_params_dict[name] = grid_search.best_params_

        # Évaluation sur le jeu de test
        y_pred = grid_search.predict(X_test)
        print(f"Classification Report:\n{classification_report(y_test, y_pred)}")

    # Affichage des meilleurs paramètres des modèles
    print("\\n--- Best Parameters for All Models ---")
    for model_name, best_params in best_params_dict.items():
        print(f"{model_name}: {best_params}")
        """
            st.code(code_hyper, language="python")

        st.image("st_app/hyper_param.png")

        st.write(
            "A présent pour verifier notre modele pré entrainé avec les hyperparametres,"
            "nous lui passons de nouveaux commentaires a analyser"
        )
        
        import joblib

        # Chargement du modèle pré-entraîné (incluant la vectorisation)
        model_lr = joblib.load(
            "st_app/model_lr"
        )

        # Titre de l'application
        import streamlit as st

# Titre de l'application
        st.subheader("Analyse de commentaire avec un modèle pré-entraîné et optimisé")
        st.write("Pour vérifier notre modèle pré-entraîné avec ses hyperparamètres, nous allons analyser de nouveaux commentaires.")

        # Zone de saisie pour le commentaire
        comment = st.text_area("Commentaire (au moins une phrase avec 5 mots minimum, idéalement) :")

        if comment:  # Vérification de la saisie d'un commentaire
            try:
                # Utilisation du pipeline pour effectuer la prédiction
                prediction = model_lr.predict([comment])[0]  # Obtenir la classe prédite
                probabilities = model_lr.predict_proba([comment])  # Les probabilités associées aux classes

                # Conversion du résultat en texte lisible
                if prediction == 1:
                    result_text = "Avis positif"
                elif prediction == -1:
                    result_text = "Avis négatif"
                else:
                    result_text = "Avis non classé"

                st.write("Résultat de la prédiction :", result_text)
                st.write("Probabilités associées à chaque classe :")

                # Mapping des indices vers des libellés explicites
                labels = {0: "Probabilité négative", 1: "Probabilité positive"}

                # Affichage des probabilités avec des libellés détaillés
                for i, prob in enumerate(probabilities[0]):
                    st.write(f"{labels.get(i, 'Classe ' + str(i))} : {prob:.2f}")

            except Exception as e:
                st.error(f"Une erreur est survenue lors de la prédiction : {e}")


        st.write("Nous voyons que les résultats sont bons")

        st.write(
            """La partie modélisation nous à permi de calculer notre meilleur prédiction, nous devons maintenant nous concentrer sur la détection des thématiques, pour cela nous avons besoin de retravailler le contenu des avis"""
        )

    if st.checkbox("#Reconnaissance des thématiques avec LDA et Bertopics", key="lda1"):
        st.write(
            """Nous allons comparer ces deux methodes, LDA (Latent Dirichlet Allocation) et Bertopics."""
        )
        if st.checkbox("Méthode LDA", key="lda2"):
            # le topic modeling pour connaitre les themes les plus importants
            st.subheader("""LDA (Latent Dirichlet Allocation) :""")
            st.image("st_app/shema_lda.png")
            st.write("""--LDA un modèle probabiliste qui détecte des thèmes latents en analysant les fréquences de mots dans les documents,
            sans tenir compte du contexte sémantique profond.--            
            L'allocation de Dirichlet latente (LDA) est un modèle génératif probabiliste utilisé pour découvrir des sujets abstraits dans
            une collection de documents. Elle suppose que chaque document est un mélange de plusieurs sujets et que chaque sujet est un
            mélange de mots.
                LDA est une technique de modélisation de sujets qui applique l'apprentissage non supervisé sur de grands ensembles
            de données textuelles pour produire un ensemble résumé de termes représentant les principaux sujets de la collection.
            Elle est largement utilisée en traitement du langage naturel (NLP) pour analyser les tendances et les thèmes dans les textes
         """)
            if st.checkbox("J'affiche le code", key="lda3"):
                code_lda = r"""
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

df_clean = pd.read_csv("st_app/df_clean.csv")
df_clean = df_clean[df_clean.rating != 3]
df_clean['rating_2'] = df_clean.rating.replace([1, 2, 3, 4, 5], [-1, -1, 1, 1, 1])
df_clean['avis_clean'] = df_clean['avis_clean'].fillna('').astype(str)

# Vectorisation des avis
vectorizer = CountVectorizer()
df_clean['avis_clean'] = df_clean['avis_clean'].astype(str)
dtm = vectorizer.fit_transform(df_clean['avis_clean'])

# Creation du LDA modele
lda = LatentDirichletAllocation(n_components=10, random_state=42)
lda.fit(dtm)

# Recuperation des mots pour chaque théme.
for index, topic in enumerate(lda.components_):
    print(f"Top words for topic {index}:")
    print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]]) # Adjust the number of top words to display

# Transformation des docuements en matrice de distribution
topic_results = lda.transform(dtm)

# Ajout de la catégorie de topics dans le DataFrame
df['topic_distribution'] = list(topic_results)
df['topic'] = df['topic_distribution'].apply(lambda x: np.argmax(x))

# Affichage des topics
st.write("### Topics")
st.write("Les topics sont les suivants :")
st.write(df['topic'].value_counts())
"""
                st.code(code_lda, language="python")

            st.image("st_app/LDA10thm.png")
            st.image("st_app/bertopics_graph8.png")

        if st.checkbox("Méthode Bertopics", key="bertopics1"):
            import pandas as pd
            import numpy as np
            from bertopic import BERTopic
            from transformers import pipeline
            st.write("""Bertopic, en revanche, combine des embeddings sémantiques (ex. BERT) avec des techniques de regroupement pour extraire des thèmes contextuellement riches,
                 tenant compte des relations entre les mots dans leurs contextes.""")

            # le topic modeling pour connaitre les themes les plus importants
            if st.checkbox("J'affiche le code", key="bertopic2"):
                    st.write("""
                    import pandas as pd
                    import numpy as np
                    from bertopic import BERTopic
                    from transformers import pipeline
                    # allèger le jeu de données pour le temps de traitement

                    # Définition de la taille de l'échantillon
                    sample_size = 100000

                    # Générer des echantillons aléatoires selon une distribution normale
                    indices = np.random.choice(df.index, size=sample_size, replace=False)

                    # Sélectionner les lignes correspondantes
                    df_sample = df.loc[indices]

                    # Afficher le DataFrame échantillonné
                    print(df_sample)

                    # Préparer les avis pour BERTopic
                    avis = df_sample['avis_clean'].tolist()

                    # Vérifier le type de chaque avis
                    #assert all(isinstance(a, str) for a in avis), "Tous les avis doivent être de type 'str'"

                    # Créer un pipeline d'encodage Camembert (modèle BERT pour le français)
                    embedder = pipeline("feature-extraction", model="camembert-base", tokenizer="camembert-base")

                    # Generate embeddings for each avis, handling variable sequence lengths
                    embeddings = []
                    for avis_item in avis:
                        embedding = embedder(avis_item, truncation=True, padding=True, max_length=512)  # Adjust max_length as needed
                        embeddings.append(embedding[0][0])

                    # Convert the embeddings to a 2D NumPy array
                    embeddings = np.array(embeddings)

                    # Reshape the embeddings to have a single column if needed
                    # embeddings = embeddings.reshape(-1, 1)  #This line is no longer needed

                    # Créer un modèle BERTopic en utilisant les embeddings
                    topic_model = BERTopic(language="french")
                    topics, probabilities = topic_model.fit_transform(avis, embeddings)

                    # Ajouter les sujets trouvés au DataFrame
                    df_sample['topics'] = topics

                    # Afficher les résultats


                    display(topic_model.get_topic(0))  # Afficher les termes pour le sujet 0""")

    if st.checkbox("#Cas pratique", key="cas_pratique"):
                        st.write("Cas pratique")
                        from sklearn.feature_extraction.text import CountVectorizer
                        from sklearn.decomposition import LatentDirichletAllocation
                        import pandas as pd
                        from nltk.corpus import stopwords
                        import nltk

                        nltk.download("stopwords")
                        import numpy as np
                        import joblib

                        # Charger les stop words par défaut
                        try:
                            stop_words_default = stopwords.words("french")
                        except:
                            st.warning(
                                "Téléchargez le corpus stopwords pour NLTK si ce n'est pas encore fait :"
                            )
                            st.code("import nltk\nnltk.download('stopwords')")
                            stop_words_default = []

                        # Charger et préparer les données
                        df_clean = pd.read_csv("st_app/df_clean.csv")
                        df_clean = df_clean[df_clean.rating != 3]
                        df_clean["rating_2"] = df_clean.rating.replace([1, 2, 3, 4, 5], [-1, -1, 1, 1, 1])
                        df_clean["avis"] = df_clean["avis_clean"].fillna("").astype(str)

                        df_global = pd.read_csv("st_app/df_global.csv")
                        df_global = df_global[df_global.rating != 3]
                        df_global["rating_2"] = df_global.rating.replace([1, 2, 3, 4, 5], [-1, -1, 1, 1, 1])
                        df_global["avis"] = df_global["avis_global"].fillna("").astype(str)

                        # Ajouter une option pour sélectionner le jeu de données
                        st.write("### Choix de la source de données")
                        data_source = st.radio(
                            "Sélectionnez la source de données :", options=["df_clean", "df_global"]
                        )

                        if data_source == "df_clean":
                            df = df_clean[["avis", "rating_2", "company"]]
                        else:
                            df = df_global[["avis", "rating_2", "company"]]

                        # Filtrage par entreprise
                        company_name = st.selectbox("Choisissez une entreprise", df["company"].unique())
                        filtered_df = df[df["company"] == company_name]

                        # Filtrage interactif
                        data_size = st.slider(
                            "Taille du jeu de données",
                            min_value=100,
                            max_value=len(filtered_df),
                            value=10000,
                            step=100,
                            key="slider_data_size2",
                        )
                        filtered_df = filtered_df.sample(n=data_size, random_state=42)

                        # Ajouter des scénarios fixes pour les n-grammes
                        st.write("### Scénarios des n-grammes")
                        ngram_scenarios = {
                            "Vision normale (1,1)": (1, 1),
                            "Bi-gram (2,2)": (2, 2),
                            "Tri-gram (3,3)": (3, 3),
                        }
                        selected_scenario = st.radio(
                            "Choisissez un scénario n-gram :", options=list(ngram_scenarios.keys())
                        )
                        ngram_range = ngram_scenarios[selected_scenario]

                        st.write(f"Vous avez choisi le scénario : {selected_scenario} avec n-gram = {ngram_range}")

                        # Ajouter des entrées pour paramétrer le nombre de mots et de sujets
                        st.write("### Paramètres des sujets et des mots-clés")
                        n_topics = st.number_input(
                            "Nombre de sujets", min_value=1, max_value=5, value=3, step=1, key="num_topics"
                        )
                        n_top_words = st.number_input(
                            "Nombre de mots-clés par sujet",
                            min_value=1,
                            max_value=8,
                            value=5,
                            step=1,
                            key="num_top_words",
                        )

                        # Ajouter des stop words supplémentaires
                        stop_words_input = st.text_area(
                            "Stop words supplémentaires à enlever (séparés par une virgule)", ""
                        )
                        user_stop_words = [
                            word.strip() for word in stop_words_input.split(",") if word.strip()
                        ]
                        all_stop_words = list(stop_words_default + user_stop_words)

                        # Fonction pour extraire les sujets avec LDA et calculer la représentativité
                        def analyze_topics_with_representativity(
                            reviews, n_topics, n_top_words, stop_words=None, ngram_range=(2, 2)
                        ):
                            vectorizer = CountVectorizer(stop_words=stop_words, ngram_range=ngram_range)
                            X = vectorizer.fit_transform(reviews)

                            lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
                            topic_distributions = lda.fit_transform(X)

                            feature_names = vectorizer.get_feature_names_out()
                            topics = [
                                [feature_names[i] for i in topic.argsort()[: -n_top_words - 1: -1]]
                                for topic in lda.components_
                            ]
                            return topics, topic_distributions

                        # Création des colonnes pour affichage des avis positifs et négatifs
                        col1, col2 = st.columns(2)
                        with col1:
                            st.header("### Sujets pour les avis positifs")
                            positive_reviews = filtered_df[filtered_df["rating_2"] == 1]["avis"]
                            positive_topics, positive_distributions = analyze_topics_with_representativity(
                                positive_reviews,
                                n_topics=n_topics,
                                n_top_words=n_top_words,
                                stop_words=all_stop_words,
                                ngram_range=ngram_range,
                            )
                            st.write(positive_topics)

                        with col2:
                            st.header("### Sujets pour les avis négatifs")
                            negative_reviews = filtered_df[filtered_df["rating_2"] == -1]["avis"]
                            negative_topics, negative_distributions = analyze_topics_with_representativity(
                                negative_reviews,
                                n_topics=n_topics,
                                n_top_words=n_top_words,
                                stop_words=all_stop_words,
                                ngram_range=ngram_range,
                            )
                            st.write(negative_topics)


##############################################################################
# PAGE 5
##############################################################################
elif page == pages[5]:
    st.write("### Conclusion")
    st.write("""
    Notre projet a permis d’identifier les principaux facteurs influençant la satisfaction client et de comparer
    différentes approches de modélisation thématique. L’analyse des avis clients offre aux banques en ligne un levier
    stratégique pour améliorer leurs services et fidéliser leur clientèle.
            
    Nous avons atteint une précision finale de 97% avec la régression logistique et le Random Over Sampler et identifié
    ces cinq clusters principaux via la LDA. Le BERTopic a permis une meilleure détection des thèmes avec des embeddings BERT.
         """)
