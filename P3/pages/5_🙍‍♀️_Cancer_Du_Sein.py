import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

st.markdown(            
    """
    <div style="text-align: center;">
        <h1>Prédiction de pathologie : Cancer du Sein</h1>
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
    file_path = 'dataset\df_CS_final.csv'
    data = pd.read_csv(file_path)
    
    # Sélectionner les colonnes pertinentes
    columns = ["radius_mean", "texture_mean", "smoothness_mean", "compactness_mean", "concavity_mean",
               "concave points_mean", "radius_se", "perimeter_se", "area_se",
               "radius_worst", "texture_worst", "smoothness_worst", "compactness_worst", "concavity_worst",
               "concave points_worst"]
    X = data[columns]
    y = data["diagnosis"]
    
    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Entraîner le modèle Random Forest
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    return model, columns

# Charger et entraîner le modèle
model, columns = load_data_and_train_model()


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

    # Prédiction en utilisant le modèle Random Forest
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    proba = prediction_proba.max()
    proba = proba * 100
    proba = round(proba, 0)
    
     # Affichage du résultat de la prédiction
    if prediction[0] == 1:
        st.error('Tumeur Maligne', icon="🚨")
    else:
        st.warning('Tumeur Bénigne', icon="⚠️")

    st.write(f'Précision : {proba} %')
