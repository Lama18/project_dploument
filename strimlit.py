import streamlit as st
import requests


API_URL = "https://project-dploument-3.onrender.com"

st.title("Machine Learning Prediction")
st.write("Enter the features to make a prediction.")

age = st.number_input("age", min_value=18, max_value=40)
appearance = st.number_input("appearance ", min_value=0)
goals = st.number_input("goals", min_value=0)
assists = st.number_input("assists", min_value=0)
award = st.number_input("award", min_value=0, key="award_input")
highest_value = st.number_input("highest_value", min_value=0, key="highest_value_input")
team_AS_Monaco = st.selectbox("team_AS Monaco", ["yes", "no"])
team_Southampton_FC = st.selectbox("team_Southampton FC", ["yes","no"])


if st.button("Predict"):
    payload = {
        "age": age,
        "appearance": appearance,
        "goals": goals,
        "assists": assists,
        "award": award,
        "highest_value": highest_value,
        "team_AS Monaco": team_AS_Monaco,
        "team_Southampton FC": team_Southampton_FC,
    }

    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 200:
        prediction = response.json()["pred"]
        st.write(f"The prediction is: {prediction}")
    else:
       st.error("Error making prediction!")