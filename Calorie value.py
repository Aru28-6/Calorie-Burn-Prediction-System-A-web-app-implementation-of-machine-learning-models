# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users/DELL/Desktop/Cloud Computing/Minor Project/Calorie_burn/trained_model_c.sav', 'rb'))
# Example input data: replace these values with the actual inputs
input_data = {
    'Gender': 0,  # 0 for male, 1 for female
    'Age': 25,
    'Height': 175,
    'Weight': 70,
    'Duration': 30,
    'Heart_Rate': 120,
    'Body_Temp': 98.6
}

# Convert the input data into a DataFrame to match the model's expected format
input_df = pd.DataFrame([input_data])

# Predict calorie burn
predicted_calories = loaded_model.predict(input_df)

# Display the prediction
print(f"Predicted Calorie Burn: {predicted_calories[0]:.2f} calories")


