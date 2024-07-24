import streamlit as st
import pandas as pd

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(            
    """
    <div style="text-align: center;">
        <h1>Mentions Legales</h1>
    </div>
    """,
    unsafe_allow_html=True)

st.markdown("## Editeur du Site")
st.markdown("Le site Vital Stats est édité par :")
st.markdown("Vital Stats")
st.markdown("Adresse : 123 Rue de l’Innovation, Paris, France")
st.markdown("Email : contact@vitalstats.com")
st.markdown("Téléphone : +33 1 23 45 67 89")
st.markdown(" Directeur de la publication : Hadi MOHABEDDINE")
st.markdown("")
st.markdown("")
st.markdown("## Hébergement")
st.markdown("Le site est hébergé par : ")
st.markdown("Wild Code School")
st.markdown("Adresse : 44 Rue Alphonse Penaud, 75020 Paris")
st.markdown("Téléphone : 09 78 45 04 38")
st.markdown("Email : celine.berthon@wildcodeschool.com")
st.markdown("")
st.markdown("")
st.markdown("## Propriété Intellectuelle")
st.markdown("Le contenu du site Vital Stats (textes, images, graphismes, logo, icônes, etc.) est la propriété exclusive de Vital Stats, sauf mention contraire. Toute reproduction, distribution, modification, adaptation, retransmission ou publication, même partielle, de ces différents éléments est strictement interdite sans l'accord écrit de Vital Stats.")
st.markdown("")
st.markdown("")
st.markdown("## Protection des Données Personnelles")
st.markdown("Vital Stats s'engage à ce que la collecte et le traitement de vos données, effectués à partir du site www.vitalstats.com, soient conformes au règlement général sur la protection des données (RGPD) et à la loi Informatique et Libertés.")
st.markdown("Responsable du traitement : Rami Galoul")
st.markdown("Finalité du traitement : Les données collectées sont utilisées pour les revendre aux Big Pharma.")
st.markdown("Droit d’accès, de rectification et de suppression : Vous disposez d’un droit d’accès, de rectification et de suppression des données vous concernant. Vous pouvez exercer ces droits en nous contactant à l'adresse email : contact@vitalstats.com.")
st.markdown("Pour plus d'informations, consultez notre Politique de Confidentialité.")
st.markdown("")
st.markdown("")
st.markdown("## Cookies")
st.markdown("Le site Vital Stats utilise des cookies pour améliorer votre expérience de navigation.")