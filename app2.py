import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('crop_recommendation.pkl', 'rb'))

# Sidebar Navigation
st.sidebar.title("🌿 Menu")
page = st.sidebar.radio("Go to", ["Home", "Crop Recommendation"])

# Homepage
if page == "Home":
    st.title("🌾 Crop Recommendation System")

    # Button for quick access to crop recommendation
    if st.button("Go to Crop Recommendation"):
        page = "Crop Recommendation"

    # Image below the title and button
    st.image("field.jpg", use_container_width=True)  # Updated parameter
    st.write(
        "Optimize your farming by selecting the best crop based on soil nutrients, weather conditions, and rainfall."
    )

# Crop Recommendation Page
if page == "Crop Recommendation":
    st.title("🌱 Crop Recommendation")
    st.write("Enter soil and weather details to get the best crop recommendation.")

    # Input fields
    N = st.number_input("Nitrogen (N)", min_value=0, max_value=150, step=1)
    P = st.number_input("Phosphorus (P)", min_value=0, max_value=150, step=1)
    K = st.number_input("Potassium (K)", min_value=0, max_value=150, step=1)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
    ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, step=0.1)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, step=0.1)

    # Predict crop
    if st.button("Recommend Crop"):
        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        prediction = model.predict(input_data)
        st.success(f"🌾 Recommended Crop: **{prediction[0]}**")
