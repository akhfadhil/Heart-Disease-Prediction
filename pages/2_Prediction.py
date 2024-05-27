import pickle
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
import streamlit as st

st.set_page_config(
    page_title = "Heart Attack Dashboard",
    page_icon="🧊",
    layout = "wide"
)

# Import model & scaler
jantung_model = pickle.load(open('HD_Machine.sav', 'rb'))
scaler = joblib.load('scaler.save') 

# Judul
st.title('Heart Attack Prediction')
with st.container(border=True):

    input = [0 for x in range(0, 13)]

    # Age
    age = st.number_input('Age', value=30, placeholder="Type your age...")
    input[0] = age

    # Sex
    sex = st.selectbox("Sex", ["Laki-laki", "Perempuan"])

    if sex == 'Laki-laki':
        input[1] = 1
    elif sex == 'Perempuan':
        input[1] = 0

    # Chest Pain Type
    cpt = st.selectbox("Chest Pain Type", ["1. Typical Angina", "2. Atypical Angina", "3. Non-anginal Pain", "4. Asymptomatic"])

    if cpt == '1. Typical Angina':
        input[2] = 1
    elif cpt == '2. Atypical Angina':
        input[2] = 2
    elif cpt == '3. Non-anginal Pain':
        input[2] = 3
    elif cpt == '4. Asymptomatic':
        input[2] = 4

    # Blood Pressure
    bp = st.number_input('Blood Pressure', value=120, placeholder="Type your blood pressure...")
    input[3] = bp

    # Cholesterol
    ch = st.number_input('Cholesterol', value=150, placeholder="Type your cholesterol...")
    input[4] = ch

    # FBS
    fbs = st.selectbox("Fasting Blood Sugar", ["Yes", "No"])

    if fbs == 'Yes':
        input[5] = 1
    elif fbs == 'No':
        input[5] = 0

    # EKG
    ekg = st.selectbox("EKG result", ["1. Normal", "2. Saving ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)",
                                      "3. Showing probable or definite left ventricular hypertrophy by Estes' criteria"])

    if ekg == '1. Normal':
        input[6] = 0
    elif ekg == '2. Saving ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)':
        input[6] = 1
    elif ekg == "3. Showing probable or definite left ventricular hypertrophy by Estes' criteria":
        input[6] = 2

    # Max HR
    hr = st.number_input('Max Heart Rate', value=80, placeholder="Type your heart rate...")
    input[7] = hr

    # Exercise Angina
    ea = st.selectbox("Exercise Angine", ["Yes", "No"])

    if ea == 'Yes':
        input[8] = 1
    elif ea == 'No':
        input[8] = 0

    # ST Depression
    std = st.number_input('Oldpeak (ST depression)', value=1.0, placeholder="Type ST depression...")
    st.caption('Use . instead of ,')
    input[9] = std

    # Slope of ST
    slope = st.selectbox("Slope of ST", ["1. Upsloping", "2. Flat", "3. Downsloping"])

    if slope == '1. Upsloping':
        input[10] = 1
    elif slope == '2. Flat':
        input[10] = 2
    elif slope == "3. Downsloping":
        input[10] = 3

    # Number of vessel fluro
    vessel = st.selectbox("Number of major vessels (0-3) colored by flourosopy", ["0", "1", "2", "3"])

    if vessel == '0':
        input[11] = 0
    elif vessel == '1':
        input[11] = 1
    elif vessel == "2":
        input[11] = 2
    elif vessel == "3":
        input[11] = 3

    # Thal
    thal = st.selectbox("Thallium", ["Normal", "Fixed defect", "Reversable defect"])

    if thal == 'Normal':
        input[12] = 2
    elif thal == 'Fixed Defect':
        input[12] = 6
    elif thal == "Rerversable defect":
        input[12] = 7

heart_attack_diag = ''
if st.button('Predict'):
    print(input)
    input = tuple(input)
    as_array = np.array(input)
    reshape = as_array.reshape(1, -1)
    std_data = scaler.transform(reshape)
    heart_attack_pred = jantung_model.predict(std_data)

    print(heart_attack_pred)
    if (heart_attack_pred[0]==0):
        heart_attack_diag = 'Tidak berpotensi menderita penyakit jantung'
    else:
        heart_attack_diag = 'Berpotensi menderita penyakit jantung'
    
    st.success(heart_attack_diag)
