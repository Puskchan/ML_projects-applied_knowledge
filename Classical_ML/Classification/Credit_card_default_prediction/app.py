import streamlit as st
import os
import pandas as pd
import numpy as np
import pickle
import joblib
import plotly.express as px
import shap
import matplotlib.pyplot as plt

# Load the model
@st.cache_resource
def load_model():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, 'model.pkl')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Load feature names
FEATURE_NAMES = [
    'RevolvingUtilizationOfUnsecuredLines',
    'age',
    'NumberOfTime30-59DaysPastDueNotWorse',
    'DebtRatio',
    'MonthlyIncome',
    'NumberOfOpenCreditLinesAndLoans',
    'NumberOfTimes90DaysLate',
    'NumberRealEstateLoansOrLines',
    'NumberOfTime60-89DaysPastDueNotWorse',
    'NumberOfDependents'
]

def main():
    st.title('Credit Card Default Prediction')
    st.write("""
    This app predicts the probability of credit card default based on various features.
    Please input the required information below.
    """)

    # Sidebar for user inputs
    st.sidebar.header('User Input Features')

    def user_input_features():
        data = {}
        
        data['RevolvingUtilizationOfUnsecuredLines'] = st.sidebar.slider(
            'Revolving Utilization Of Unsecured Lines', 0.0, 1.0, 0.5)
        
        data['age'] = st.sidebar.slider('Age', 20, 95, 35)
        
        data['NumberOfTime30-59DaysPastDueNotWorse'] = st.sidebar.slider(
            'Number Of Times 30-59 Days Past Due', 0, 12, 0)
        
        data['DebtRatio'] = st.sidebar.slider('Debt Ratio', 0.0, 5.0, 1.0)
        
        data['MonthlyIncome'] = st.sidebar.number_input(
            'Monthly Income', min_value=0.0, max_value=100000.0, value=5000.0)
        
        data['NumberOfOpenCreditLinesAndLoans'] = st.sidebar.slider(
            'Number Of Open Credit Lines And Loans', 0, 50, 10)
        
        data['NumberOfTimes90DaysLate'] = st.sidebar.slider(
            'Number Of Times 90 Days Late', 0, 16, 0)
        
        data['NumberRealEstateLoansOrLines'] = st.sidebar.slider(
            'Number Real Estate Loans Or Lines', 0, 20, 1)
        
        data['NumberOfTime60-89DaysPastDueNotWorse'] = st.sidebar.slider(
            'Number Of Times 60-89 Days Past Due', 0, 10, 0)
        
        data['NumberOfDependents'] = st.sidebar.slider(
            'Number Of Dependents', 0, 10, 0)
        
        return pd.DataFrame(data, index=[0])

    # Get user input
    df = user_input_features()

    # Show user input
    st.subheader('User Input Parameters')
    st.write(df)

    # Load the model and make prediction
    model = load_model()
    prediction_proba = model.predict_proba(df)
    prediction = model.predict(df)

    # Show prediction
    st.subheader('Prediction')
    default_status = 'Will Default' if prediction[0] == 1 else 'Will Not Default'
    st.write(f'The client {default_status}')

    # Show prediction probability
    st.subheader('Prediction Probability')
    st.write(f'Probability of Default: {prediction_proba[0][1]:.2%}')

    # SHAP values for explanation
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(df)

    # Plot SHAP values
    st.subheader('Feature Importance (SHAP Values)')
    fig, ax = plt.subplots()
    if isinstance(shap_values, list):
        # For binary classification, use shap_values[1] for positive class
        shap.summary_plot(shap_values[1], df, plot_type="bar", show=False)
    else:
        # For single output models
        shap.summary_plot(shap_values, df, plot_type="bar", show=False)
    st.pyplot(fig)
    plt.clf()


if __name__ == '__main__':
    main()