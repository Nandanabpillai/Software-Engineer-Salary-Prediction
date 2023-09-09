import streamlit as st
import numpy as np
import pickle

def load_model():
    with open ('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data['model']
le_country = data['le_country']
le_education = data['le_education']

def show_pred_page():
    st.title("Software Developer Salary Prediction")
    st.write("""### We require some details!""")

    countries = (
        'United States of America',
       'United Kingdom of Great Britain and Northern Ireland',
       'Australia', 
       'Netherlands', 
       'Germany', 
       'Sweden', 
       'France', 
       'Spain',
       'Brazil', 
       'Italy', 
       'Canada', 
       'Switzerland', 
       'India', 
       'Norway',
       'Denmark', 
       'Israel', 
       'Poland'
    )

    education = (
        "Less than a Bachelor's degree",
        "Bachelor's degree", 
        "Master's degree", 
        'Post Grad'
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education", education)
    experience = st.slider('Years of Experience', 0, 50)

    submit = st.button("Calculate Salary")
    if submit:
        x = np.array([[country, education, experience]])
        x[:, 0] = le_country.transform(x[:, 0])
        x[:, 1] = le_education.transform(x[:, 1])
        x = x.astype(float)
        y_pred = model.predict(x)
        st.subheader(f"Estimated Salary: ${y_pred[0]:.2f}")