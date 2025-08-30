
import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load('food_recommendation_model.pkl')

# Function to predict diet recommendation
def predict_diet(input_data):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        return "Vegetarian"
    else:
        return "Non-Vegetarian"

# Streamlit User Interface
st.title("Personalized Food Recommendation")
st.write("Enter the health data for diet recommendation:")

# Collect input data from user
breakfast = st.number_input("Breakfast (0/1)", min_value=0, max_value=1, value=0)
lunch = st.number_input("Lunch (0/1)", min_value=0, max_value=1, value=0)
dinner = st.number_input("Dinner (0/1)", min_value=0, max_value=1, value=0)
calories = st.number_input("Calories", value=250)
fats = st.number_input("Fats", value=1.5)
proteins = st.number_input("Proteins", value=10.0)
iron = st.number_input("Iron", value=2.76)
calcium = st.number_input("Calcium", value=20.0)
sodium = st.number_input("Sodium", value=439)
potassium = st.number_input("Potassium", value=165)
carbohydrates = st.number_input("Carbohydrates", value=49.0)
fibre = st.number_input("Fibre", value=4.1)
vitamin_d = st.number_input("Vitamin D", value=0.0)
sugars = st.number_input("Sugars", value=6.1)

# Prepare input data for prediction
input_data = pd.DataFrame([[breakfast, lunch, dinner, calories, fats, proteins, iron,
                            calcium, sodium, potassium, carbohydrates, fibre, vitamin_d, sugars]],
                          columns=['Breakfast', 'Lunch', 'Dinner', 'Calories', 'Fats', 'Proteins', 
                                   'Iron', 'Calcium', 'Sodium', 'Potassium', 'Carbohydrates', 'Fibre', 
                                   'VitaminD', 'Sugars'])

# Predict and display result
if st.button("Get Diet Recommendation"):
    result = predict_diet(input_data)
    st.write(f"Recommended Diet: {result}")
