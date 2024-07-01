import pandas as pd
import numpy as np
import pickle as pkl
import streamlit as st
model=pkl.load(open('MIPML.pkl','rb'))
st.header('Health Insurance Premium Predictor')
gender=st.selectbox('**Choose your Gender**',['','Female','Male'])
smoker=st.selectbox('**Are you a smoker ?**',['','Yes','No'])
region=st.selectbox('**Select your Region**',['','SouthEast','SouthWest','NorthEast','NorthWest'])
age=st.number_input('**Enter your age**',0,80)
bmi=st.number_input('**Enter your BMI**',0.0, 100.0, format="%.1f")
children=st.number_input('**Choose no of children**',0,5)

if st.button('Predict Insurance Premium'):
    # Preprocessing the input data
    if gender == 'Female':
        gender = 0
    else:
        gender = 1

    if smoker == 'No':
        smoker = 0
    else:
        smoker = 1

    if region == 'SouthEast':
        region = 0
    elif region == 'SouthWest':
        region = 1
    elif region == 'NorthEast':
        region = 2
    else:
        region = 3

    # Preparing input data for the model
    input_data = (age, gender, bmi, children, smoker, region)
    input_data = np.asarray(input_data)
    input_data = input_data.reshape(1, -1)

    # Predicting the insurance premium
    prediction = model.predict(input_data)

    # Displaying the result
    st.write('**Estimated Health Insurance Premium: ${:,.2f} USD**'.format(prediction[0]))