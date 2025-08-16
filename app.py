import streamlit as st
import joblib
import numpy as np


model  = joblib.load("rf_model.pkl")

st.title("Laptop Price Prediction")
st.divider()

processor_speed = st.number_input("Enter Processor Speed",value=2.50,step=0.50)
ram_size = st.number_input("Enter Ram Size",value=16,step=8)
storage_capacity = st.number_input("Enter storage capacity",value=512,step=256)

X = [processor_speed,ram_size,storage_capacity]

st.divider()

prediction = st.button("Price Estimation Button!")

st.divider()

if prediction:
    x1 = np.array(X)
    prediction=model.predict([x1])[0]
    st.write(f"Price estimation for the laptop is {prediction:.2f}")
else:
    st.write("Please use the button for getting a prediction")