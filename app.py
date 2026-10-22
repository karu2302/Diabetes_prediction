from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

import os
os.system('pip install scikit-learn')
import streamlit as st
import numpy as np
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

import pickle
with open("knn_f.pkl", "rb") as f:
    model= pickle.load(f)
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .title {
            color: #2c3e50;
            text-align: center;
        }
        .stButton>button {
            background-color: #27ae60;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'> Diabetes Prediction App</h1>", unsafe_allow_html=True)

Age	= st.number_input("Enter Age:", min_value=1.000000, max_value=13.000000, value = 7.000000)
Sex	= st.number_input("Enter Sex:", min_value=0.000000, max_value=1.000000,value = 0.500000)
HighChol = st.number_input("Enter HighChol",min_value=0.000000,max_value=1.000000,value = 0.500000)
CholCheck = st.number_input("Enter CholCheck:", min_value=0.000000, max_value=1.000000,value = 0.500000)
BMI =st.number_input("Enter BMI :",min_value=12.000000,max_value=98.000000,value = 50.000000) 
Smoker = st.number_input("Enter Smoker or Not:", min_value=0.000000, max_value=1.000000,value = 0.500000)
HeartDiseaseorAttack = st.number_input("Enter HeartDiseaseorAttack",min_value=0.000000,max_value=1.000000,value = 0.500000)
PhysActivity = st.number_input("Enter PhysActivity",min_value=0.000000,max_value=1.000000,value = 0.500000)
Fruits = st.number_input("Enter Fruits",min_value=0.000000,max_value=1.000000,value = 0.500000)
Veggies = st.number_input("Enter Veggies",min_value=0.000000,max_value=1.000000,value = 0.500000)
HvyAlcoholConsump = st.number_input("Enter HvyAlcoholConsump",min_value=0.000000,max_value=1.000000,value = 0.500000)
GenHlth = st.number_input("Enter GenHlth",min_value=1.000000,max_value=5.000000,value = 3.000000)
MentHlth = st.number_input("Enter MentHlth",min_value=0.000000,max_value=30.000000,value = 16.000000)
PhysHlth = st.number_input("Enter PhysHlth",min_value=0.000000,max_value=30.000000,value = 16.000000)
DiffWalk = st.number_input("Enter DiffWalk",min_value=0.000000,max_value=1.000000,value = 0.500000)
Stroke = st.number_input("Enter Stroke",min_value=0.000000,max_value=1.000000,value = 0.500000)
HighBP = st.number_input("Enter HighBP",min_value=0.000000,max_value=1.000000,value = 0.500000)

if st.button("Diabetes Prediction"):
    user_data = np.array([[Age,	Sex,HighChol,CholCheck,	BMI,Smoker,HeartDiseaseorAttack,PhysActivity,Fruits,Veggies,HvyAlcoholConsump,GenHlth,MentHlth,PhysHlth,DiffWalk,Stroke,HighBP]], dtype=object)
    prediction = model.predict(user_data)
    st.success(f" Diabetes prediction : {prediction}")