# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:28:43 2024

@author: DELL
"""


import pickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the saved model
loaded_model = pickle.load(open('C:/Users/DELL/Desktop/Cloud Computing/Minor Project/Calorie_burn/trained_model_c.sav', 'rb'))


def calorie_prediction(input_data):
    # Create DataFrame from input
    input_df = pd.DataFrame([input_data], columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'])
    
    # Convert categorical data
    label_encoder = LabelEncoder()
    input_df['Gender'] = label_encoder.fit_transform(input_df['Gender'])
    
    # Ensure all numeric columns are float
    numeric_cols = ['Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
    input_df[numeric_cols] = input_df[numeric_cols].astype(float)
    
    # Predict
    predicted_calories = loaded_model.predict(input_df)
    return predicted_calories


def main():
    # Title of the app
    st.title('Calorie Burn Prediction Web App')
    
    # Input data from user
    Gender = st.text_input('Gender of the person (e.g., Male/Female)')
    Age = st.text_input('Age of the person')
    Height = st.text_input('Height of the person in cm')
    Weight = st.text_input('Weight of the person in kg')
    Duration = st.text_input('Duration of exercise in minutes')
    Heart_Rate = st.text_input('Heart rate of the person (bpm)')
    Body_Temp = st.text_input('Body Temperature of the person in °C')
    
    # Code for prediction
    diagnosis = ''
    
    # Create a button for prediction
    if st.button('Calorie Burn Test Result'):
        try:
            # Convert inputs to appropriate types
            Age = float(Age)
            Height = float(Height)
            Weight = float(Weight)
            Duration = float(Duration)
            Heart_Rate = float(Heart_Rate)
            Body_Temp = float(Body_Temp)
            
            # Call the prediction function
            diagnosis = calorie_prediction([Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp])
            
            # Display the result
            st.success(f"Predicted Calorie Burn: {diagnosis[0]:.2f} calories")
        
        except ValueError:
            st.error("Please ensure all numeric inputs are valid numbers.")
    
if __name__ == '__main__':
    main()
