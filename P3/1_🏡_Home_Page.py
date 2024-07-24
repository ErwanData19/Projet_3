import streamlit as st
import pandas as pd
from PIL import Image
import base64
import io
from io import BytesIO
import numpy as np
import random

st.set_page_config(layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
col1, col2, col3 = st.columns(3)
with col2:
    st.image('images\logo.png')
    st.markdown("")
    st.markdown("")
    st.markdown("")



st.markdown(            
    """
    <div style="text-align: center;">
        <h1>Bienvenue sur notre plateforme à destination des professionnels de santé.</h1>
    </div>
    """,
    unsafe_allow_html=True)
st.markdown('')
col1, col2, col3 = st.columns([0.05, 0.9, 0.05])
with col2 : 

    st.markdown("#### Grace à nos modèles de Machine Learning ultra poussés, nous permettons aux Medecins et Hopitaux d'interpréter efficacement les résultats d'analyses sanguines, de biopsie, de tests d'urines.")
    st.markdown("#### Sous-traitez nous le traitement des données médicales de vos patients et gagnez du temps dans leur accompganement personnel.")
    st.markdown("#### A ce jour, nous sommes à même de détecter les pathologies suivantes : ")
    st.markdown('')
    st.markdown('')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1 :
        st.markdown("##### - Diabète")
    with col2 : 
        st.markdown("##### - Cancer du Sein")
    with col3:
        st.markdown("##### - Maladies Cardiques")
    with col4:
        st.markdown("##### - Maladies Rénales")
    with col5:
        st.markdown("##### - Maladie du foie")
    st.markdown("")
    st.markdown("")
    st.markdown("#### Vous souhaitez rejoindre notre programme ? Rien de plus simple ! Contactez-nous via le formulaire dans l'onglet 'Qui Sommes Nous'. L'un de nos commerciaux se chargera de prendre contact avec vous dans les plus bref délais.")


