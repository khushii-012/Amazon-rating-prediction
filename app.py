import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("amazon_rating_model.pkl")

# App Title
st.title("Amazon Product Rating Prediction")

st.write("Predict whether a product is High Rated or Low Rated")

# User Inputs
discounted_price = st.number_input(
    "Discounted Price",
    min_value=0.0
)

actual_price = st.number_input(
    "Actual Price",
    min_value=0.0
)

discount_percentage = st.number_input(
    "Discount Percentage",
    min_value=0.0
)

rating_count = st.number_input(
    "Rating Count",
    min_value=0
)

# Prediction Button
if st.button("Predict"):

    input_data = pd.DataFrame({
        'discounted_price': [discounted_price],
        'actual_price': [actual_price],
        'discount_percentage': [discount_percentage],
        'rating_count': [rating_count]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("High Rated Product ⭐")

    else:
        st.error("Low Rated Product")
