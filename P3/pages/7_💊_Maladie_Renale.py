import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(            
    """
    <div style="text-align: center;">
        <h1>Prédiction de pathologie : Maladie Rénale</h1>
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
    file_path = 'dataset\df_ml_R1.csv'
    data = pd.read_csv(file_path)
    
    # Sélectionner les colonnes pertinentes
    columns = ['hemoglobin', 'serum_creatinine', 'specific_gravity',
               'blood_glucose_random', 'pus_cell', 'hypertension', 'albumin_0.0',
               'albumin_1.0', 'albumin_2.0', 'albumin_3.0', 'albumin_4.0',
               'albumin_5.0', 'diabetes_mellitus']
    X = data[columns]
    y = data["classification"]
    
    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    
    # Entraîner le modèle SVC
    model = SVC(probability=True)
    model.fit(X_train, y_train)
    
    return model, columns

# Charger et entraîner le modèle
model, columns = load_data_and_train_model()

# Titre de l'application
st.title('Saisie de données numériques et prédiction avec Streamlit')

# Création des champs de saisie pour les données numériques
inputs = {}
for col in columns:
    inputs[col] = st.number_input(col.replace('_', ' ').capitalize(), value=0.0)

# Bouton pour soumettre les données
if st.button('Soumettre'):
    # Création d'un DataFrame avec les données saisies
    input_df = pd.DataFrame([inputs])
    
    # Affichage des données saisies
    #st.write('Données saisies :')
    #st.write(input_df)

    # Prédiction en utilisant le modèle SVC
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    proba = prediction_proba.max()
    proba = proba * 100
    proba = round(proba, 0)
    
    # Affichage du résultat de la prédiction
    if prediction[0] == 1:
        st.error('Maladie détectée', icon="🚨")
    else:
        st.success('Pas de maladie', icon="✅")
    st.write(f'Précision : {proba} %')

   

    
