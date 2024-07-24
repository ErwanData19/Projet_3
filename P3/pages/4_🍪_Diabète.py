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
        <h1>Prédiction de pathologie : Diabète</h1>
    </div>
    """,
    unsafe_allow_html=True)
st.markdown(            
    """
    <div style="text-align: center;">
        <h4>Renseignez ici le résultats de vos analyses médicales : </h>
    </div>
    """,
    unsafe_allow_html=True)

def load_data_and_train_model():
    url = 'https://raw.githubusercontent.com/MaskiVal/DataSets/main/diabetes.csv'
    data = pd.read_csv(url)
    data = data.drop(columns="SkinThickness")
    data["BMI"].replace(0, 33, inplace=True)
    data["Glucose"].replace(0, 122, inplace=True)
    data["BloodPressure"].replace(0, 70, inplace=True)
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

model = load_data_and_train_model()

pregnancies = st.number_input('Nombre de grossesses', min_value=0, max_value=20, value=1)
glucose = st.number_input('Concentration de glucose', min_value=0, max_value=200, value=120)
blood_pressure = st.number_input('Pression artérielle (mm Hg)', min_value=0, max_value=150, value=70)
insulin = st.number_input('Insuline (mu U/ml)', min_value=0, max_value=900, value=80)
bmi = st.number_input('Indice de masse corporelle (BMI)', min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input('Âge', min_value=0, max_value=120, value=33)

# Bouton pour soumettre les données
if st.button('Soumettre'):
    # Création d'un DataFrame avec les données saisies
    input_data = {
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': blood_pressure,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': dpf,
        'Age': age
    }
    input_df = pd.DataFrame([input_data])
    
    # Affichage des données saisies
    #st.write('Données saisies :')
    #st.write(input_df)
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    proba = prediction_proba.max()
    proba = proba * 100
    proba = round(proba, 0)

    # Affichage du résultat de la prédiction
    st.write(f'Prédiction : {"Diabétique" if prediction[0] == 1 else "Non diabétique"}')

    if prediction[0] == 1:
        st.error('Diabétique', icon="🚨")
    else:
        st.success('Non Diabétique', icon="✅")

    st.write(f'Précision : {proba} %')
