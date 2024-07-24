import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(            
    """
    <div style="text-align: center;">
        <h1>Prédiction de pathologie : Maladie Cardiaque</h1>
    </div>
    """,
    unsafe_allow_html=True)
st.markdown(            
    """
    <div style="text-align: center;">
        <h4>Renseignez ici vos analyses médicales : </h>
    </div>
    """,
    unsafe_allow_html=True)

# Charger les données et entraîner le modèle
@st.cache_data
def load_data_and_train_model():
    url = 'https://raw.githubusercontent.com/MaskiVal/DataSets/main/heartDisease.csv'
    data = pd.read_csv(url)
    # Sélectionner uniquement les colonnes spécifiées
    columns = ['cp', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    X = data[columns]
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

# Charger et entraîner le modèle
model = load_data_and_train_model()



# Création des champs de saisie pour les données numériques
cp = st.number_input('Douleur thoracique ressentie (0-3)', min_value=0, max_value=3, value=1)
thalach = st.number_input('Fréquence cardiaque maximale atteinte', min_value=0, max_value=250, value=150)
exang = st.selectbox('Angine induite par l\'exercice', options=[0, 1], format_func=lambda x: 'Non' if x == 0 else 'Oui')
oldpeak = st.number_input('Dépression du segment ST induite par l\'exercice par rapport au repos', min_value=0.0, max_value=10.0, value=1.0)
slope = st.number_input('Pente du segment ST (0-2)', min_value=0, max_value=2, value=1)
ca = st.number_input('Nombre de vaisseaux majeurs colorés par fluoroscopie (0-4)', min_value=0, max_value=4, value=0)
thal = st.number_input('Type de thalassémie (1 = normale; 2 = défaut fixe; 3 = défaut réversible)', min_value=1, max_value=3, value=2)

# Bouton pour soumettre les données
if st.button('Soumettre'):
    # Création d'un DataFrame avec les données saisies
    input_data = {
        'cp': cp,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }
    input_df = pd.DataFrame([input_data])
    
    # Affichage des données saisies
    #st.write('Données saisies :')
    #st.write(input_df)

    # Prédiction en utilisant le modèle de Random Forest
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    proba = prediction_proba.max()
    proba = proba * 100
    proba = round(proba, 0)
    
    # Affichage du résultat de la prédiction

    if prediction[0] == 1:
        st.error('Maladie Cardiaque détectée', icon="🚨")
    else:
        st.success('Pas de maladie cardiaque', icon="✅")
    st.write(f'Précision : {proba} %')
    
    
