import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("amazon_rating_model.pkl")

# Page title
st.title("Amazon Product Rating Prediction")

st.write("Predict whether a product will be Highly Rated or Low Rated")

# User Inputs
discounted_price = st.number_input("Discounted Price")

actual_price = st.number_input("Actual Price")

discount_percentage = st.number_input("Discount Percentage")

rating_count = st.number_input("Rating Count")

# Predict Button
if st.button("Predict Rating Category"):

    # Create DataFrame
    input_data = pd.DataFrame({
        'discounted_price': [discounted_price],
        'actual_price': [actual_price],
        'discount_percentage': [discount_percentage],
        'rating_count': [rating_count]
    })

    # Prediction
    prediction = model.predict(input_data)

    # Output
    if prediction[0] == 1:
        st.success("High Rated Product ⭐")
    else:
        st.error("Low Rated Product")
