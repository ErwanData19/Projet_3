import streamlit as st
import pandas as pd

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.1,2,0.1])

with col2 : 
    st.markdown(
    """
    <div style="text-align: center;">
        <h1>Qui sommes-nous ? </h1>
    </div>
    """,
    unsafe_allow_html=True) 
    st.markdown("")
    st.markdown("")

col1, col2, col3 = st.columns([0.1,2,0.1])

with col2 : 
    st.markdown(
    """
    <div style="text-align: center;">
        <h1>Notre Histoire</h1>
    </div>
    """,
    unsafe_allow_html=True) 
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Vital Stats a été fondée en 2024 avec une mission claire : révolutionner le domaine de la santé grâce aux données et au machine learning. Depuis nos débuts, nous nous sommes engagés à fournir des solutions innovantes qui aident les professionnels de santé à prédire et diagnostiquer les pathologies avec une précision sans précédent.</h4>
    </div>
    """,
    unsafe_allow_html=True) 
    st.markdown("")
    st.markdown("")

col1, col2, col3 = st.columns([0.1,2,0.1])

with col2 : 
    st.markdown(
    """
    <div style="text-align: center;">
        <h1>Nos missions</h1>
    </div>
    """,
    unsafe_allow_html=True) 
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Notre mission est d'améliorer la qualité des soins de santé en fournissant des outils de prédiction et d'analyse basés sur le machine learning. Nous croyons que la puissance des données peut transformer les soins de santé, réduire les diagnostics tardifs et permettre des interventions plus précoces et plus efficaces.</h4>
    </div>
    """,
    unsafe_allow_html=True) 
    st.markdown("")
    st.markdown("")

col1, col2, col3 = st.columns([0.1,2,0.1])

with col2 : 
    st.markdown(
    """
    <div style="text-align: center;">
        <h1>Nos Valeurs</h1>
    </div>
    """,
    unsafe_allow_html=True) 
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Innovation : Nous investissons continuellement dans la recherche et le développement pour rester à la pointe de la technologie.</h4>
    </div>
    """,
    unsafe_allow_html=True) 
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Fiabilité : Nos solutions sont rigoureusement testées pour garantir des prédictions précises et des résultats fiables.</h4>
    </div>
    """,
    unsafe_allow_html=True) 
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Éthique : Nous prenons la confidentialité des données de nos clients très au sérieux et nous nous conformons aux normes de protection des données les plus strictes.</h4>
    </div>
    """,
    unsafe_allow_html=True) 
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Collaboration : Nous travaillons en étroite collaboration avec les professionnels de santé pour développer des solutions adaptées à leurs besoins spécifiques.</h4>
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Excellence : Nous nous efforçons de fournir des analyses précises et fiables.</h4>
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")

col1, col2, col3 = st.columns([0.1,2,0.1])

with col2 : 
    st.markdown(
    """
    <div style="text-align: center;">
        <h1>Notre Equipe</h1>
    </div>
    """,
    unsafe_allow_html=True) 
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Chez Vital Stats, nous sommes fiers de notre équipe diversifiée et hautement qualifiée. Nos experts viennent de divers horizons, alliant expertise technique et médicale pour offrir des solutions complètes et intégrées : </h4>
    </div>
    """,
    unsafe_allow_html=True)
st.markdown("")
st.markdown("")
col6, col7, col8, col9, col10 = st.columns(5)
with col6 : 
    st.markdown(
    """
    <div style="text-align: center;">
        <h1>Hadi</h1>
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: center;">
        <h3>Scrum Master</h3>
    </div>
    """,
    unsafe_allow_html=True)

with col7 : 
    st.markdown(
    """
    <div style="text-align: center;">
        <h1>Sylvain</h1>
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: center;">
        <h3>Product Owner</h3>
    </div>
    """,
    unsafe_allow_html=True)  

with col8 : 
    st.markdown(
    """
    <div style="text-align: center;">
        <h1>Henry</h1>
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: center;">
        <h3>Developpeur Machine Learning</h3>
    </div>
    """,
    unsafe_allow_html=True)

with col9 : 
    st.markdown(
    """
    <div style="text-align: center;">
        <h1>Khadija</h1>
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: center;">
        <h3>Bio-Statisticienne</h3>
    </div>
    """,
    unsafe_allow_html=True)

with col10 : 
    st.markdown(
    """
    <div style="text-align: center;">
        <h1>Erwan</h1>
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: center;">
        <h3>Bio-Statisticien</h3>
    </div>
    """,
    unsafe_allow_html=True)

st.markdown("")
st.markdown("")

col1, col2, col3 = st.columns([0.1,2,0.1])

with col2 : 
    st.markdown(
    """
    <div style="text-align: center;">
        <h1>Nos Services</h1>
    </div>
    """,
    unsafe_allow_html=True) 
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Nous offrons une gamme de services conçus pour répondre aux besoins des établissements de santé et des professionnels de la santé :</h4>
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Consulting en Data Science : Nous aidons les organisations à exploiter leurs données pour améliorer les décisions cliniques et opérationnelles.</h4>
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Solutions de Machine Learning : Nous développons des modèles prédictifs pour une variété de pathologies, y compris le diabète, les maladies cardiaques, le cancer du sein, les maladies rénales et les maladies du foie.</h4>
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Analyse de Risque : Nos outils évaluent les risques de développement de maladies et permettent des interventions préventives.</h4>
    </div>
    """,
    unsafe_allow_html=True)
    st.markdown(
    """
    <div style="text-align: center;">
        <h4>Personnalisation des Soins : Nous utilisons les données patients pour adapter les traitements et améliorer les résultats cliniques.</h4>
    </div>
    """,
    unsafe_allow_html=True)

st.title("Formulaire de Contact")
# Formulaire de contact
with st.form("contact_form"):
    name = st.text_input("Nom")
    email = st.text_input("Email")
    subject = st.text_input("Sujet")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Envoyer")
    if submitted:
        if not name or not email or not subject or not message:
            st.error("Veuillez remplir tous les champs.")
        else:
            st.success("Merci pour votre message ! Nous vous recontacterons dans les plus brefs delais")
            # Ici, vous pouvez ajouter du code pour traiter et envoyer le message
            # Par exemple, envoyer un email avec le contenu du formulaire
            # Vous pouvez utiliser des bibliothèques comme smtplib, yagmail, etc.
            # Exemple de traitement (affichage du contenu)
            #st.write("Nom:", name)
            #st.write("Email:", email)
            #st.write("Sujet:", subject)
            #st.write("Message:", message)
st.write("")
    

    
    



    

