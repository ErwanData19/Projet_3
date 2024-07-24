import streamlit as st
import pandas as pd

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Connexion")
# Formulaire de contact
with st.form("Veuillez inserer votre identifiant et mot de passe"):
    message = st.text_area("identifiant")
    mdp = st.text_area("mot de passe")
    submitted = st.form_submit_button("Soumettre")
    if submitted:
        if not message or not submitted :
            st.error("Veuillez remplir tous les champs.")
        else:
            st.success("connection en cours")

    