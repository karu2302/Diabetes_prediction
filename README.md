# 🩺 Diabetes Risk Prediction System

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit%20Learn-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red.svg)](https://streamlit.io/)

*A machine learning web tool that evaluates diabetes likelihood based on user-provided clinical health parameters.*

</div>

---

## 📖 What This Space Does
**Diabetes_prediction** is a clinical decision-support machine learning space. It accepts key health indicators—such as glucose levels, blood pressure, insulin levels, Body Mass Index (BMI), and age—and utilizes a pre-trained classification model to output an instant risk assessment indicating the likelihood of diabetes onset.

## 🧰 What is Inside This Space
- **Pre-trained ML Model File:** Serialized model artifacts (`.pkl` or `.joblib`) trained on healthcare classification datasets (e.g., PIMA Indians Diabetes Dataset).
- **Data Preprocessing & Scaling Pipeline:** Standardized transformers that scale numerical input features to match the exact distribution expected by the model.
- **Clinical Parameter Form:** Web input components (numerical inputs, sliders) designed for easy input of patient health vitals.
- **Risk Evaluation Output:** A visually distinct prediction card showing the outcome classification alongside calculated confidence/probability scores.

## ⚙️ How It Works
1. **Feature Input:** The user enters medical variables into the interactive web form.
2. **Feature Preprocessing:** The backend converts inputs into a structured NumPy array / Pandas DataFrame and applies necessary scaling or normalization.
3. **Model Prediction:** The serialized machine learning model executes `.predict()` and `.predict_proba()` on the preprocessed array.
4. **Result Presentation:** The system interprets the class probability and outputs a clear diagnostic risk indicator on screen.

---
*Migrated from Hugging Face Spaces by [karu2302](https://github.com/karu2302).*
