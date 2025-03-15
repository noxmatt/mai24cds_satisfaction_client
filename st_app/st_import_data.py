import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import os

def scrape_trustpilot(company_name, num_pages):
    reviews = []
    base_url = f"https://fr.trustpilot.com/review/{company_name}"

    for page in range(1, num_pages + 1):
        url = f"{base_url}?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        time.sleep(3)  # Attendre que la page se charge
        review_elements = soup.find_all("div", {"class": "styles_cardWrapper__kOLEb styles_show__qAseP"})

        for review in review_elements:
            #id_cust = review.find("span", {"class": "typography_heading-xxs__QKBS8 typography_appearance-default__AAY17"})
            #verif = review.find("button", {"class": "styles_reviewLabelButton__SNIsL"})
            #title_element = review.find("h2", {"class": "typography_heading-s__f7029"})
            rating_element_indiv = review.find("div", {"class": "styles_reviewHeader__PuHBd"})
            #text_element = review.find("p", {"class": "typography_body-l__v5JLj typography_appearance-default__t8iAq"})
            #date_element = review.find("time")

            #id_cust = id_cust.text.strip() if id_cust else 'No ID'
            #verif = verif.text.strip() if verif else 'Non vérifié'
            #title = title_element.text.strip() if title_element else 'No Title'
            rating = rating_element_indiv['data-service-review-rating'] if rating_element_indiv and 'data-service-review-rating' in rating_element_indiv.attrs else 'No Rating'
            #text = text_element.text.strip() if text_element else 'No Text'
            #date = date_element['datetime'] if date_element else 'No Date'

            reviews.append({
                #'company_name': company_name,
                #'title': title,
                #'id_cust': id_cust,
                #'verif': verif,
                'rating_indiv': rating,
                #'commentaire': text,
                #'date': date
            })

    return pd.DataFrame(reviews)

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    st.success(f"Fichier sauvegardé sous {filename}")

st.title("Projet Data Science - Satisfaction des Clients des Banques en Ligne")

company_name = st.text_input("Nom de l'entreprise")
num_pages = st.number_input("Nombre de pages à scraper", min_value=1, value=1)

if st.button("Scraper Trustpilot"):
    if company_name:
        with st.spinner('Scraping en cours...'):
            df = scrape_trustpilot(company_name, num_pages)
            dossier = "C:/Users/matth/OneDrive/Formation/st_app"
            filename = os.path.join(dossier, f"df_{company_name}.csv")
            save_to_csv(df, filename)
            st.dataframe(df)
    else:
        st.error("Veuillez entrer le nom de l'entreprise.")