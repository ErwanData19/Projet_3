import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.markdown(            
    """
    <div style="text-align: center;">
        <h1>Prédiction de pathologie : Maladie du Foie</h1>
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

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Charger les données et entraîner le modèle
@st.cache_data
def load_data_and_train_model():
    file_path = 'dataset\df_foie.csv'
    data = pd.read_csv(file_path)
    
    # Sélectionner les colonnes pertinentes
    columns = ["Age", "Gender", "Total_Bilirubin", "Alkaline_Phosphotase", "Alamine_Aminotransferase", "Albumin_and_Globulin_Ratio"]
    X = data[columns]
    y = data["Dataset"]
    
    # Encoder la colonne "Gender"
    X = pd.get_dummies(X, columns=["Gender"], drop_first=True)
    
    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Entraîner le modèle de régression logistique
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    return model, X.columns

# Charger et entraîner le modèle
model, columns = load_data_and_train_model()

# Création des champs de saisie pour les données numériques
inputs = {}
for col in columns:
    if col == "Gender_Male":
        inputs[col] = st.selectbox("Gender", options=["Male", "Female"], index=0)
    else:
        inputs[col] = st.number_input(col.replace('_', ' ').capitalize(), value=0.0)

# Transformer la saisie pour le genre en une variable numérique
if "Gender_Male" in inputs:
    inputs["Gender_Male"] = 1 if inputs["Gender_Male"] == "Male" else 0

# Bouton pour soumettre les données
if st.button('Soumettre'):
    # Création d'un DataFrame avec les données saisies
    input_df = pd.DataFrame([inputs])
    
    # Affichage des données saisies
    #st.write('Données saisies :')
    #st.write(input_df)

    # Prédiction en utilisant le modèle de régression logistique
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    proba = prediction_proba.max()
    proba = proba * 100
    proba = round(proba, 0)
    
    # Affichage du résultat de la prédiction
    st.markdown(f'**Précision :** {proba} %')
    
    if prediction[0] == 1:
        st.error('Maladie détectée', icon="🚨")
    else:
        st.success('Pas de maladie', icon="✅")