import streamlit as st
import pickle
import pandas as pd

# Load the machine learning model
model_file = open('C:/Users/20rew/Downloads/used_car_price_model.pkl','rb')
model = pickle.load(model_file)

# Function to make predictions
def predict(region, year, manufacturer, model, condition, cylinders, odometer, title_status, transmission, drive, type, paint_color, state, fuel):
    # Preprocess the input data as needed before passing it to the model
    input_data = [region, year, manufacturer, model, condition, cylinders, odometer, title_status, transmission, drive, type, paint_color, state, fuel]
    # Make prediction
    prediction = model.predict([input_data])
    return prediction

# UI components
st.title('Car Price Prediction')

# Input components
region = st.text_input('Region')
year = st.slider('Year', 1989, 2024)
manufacturer = st.selectbox('Manufacturer', ['gmc', 'chevrolet', 'toyota', 'ford', 'jeep', 'nissan', 'ram',
       'mazda', 'cadillac', 'honda', 'dodge', 'lexus', 'jaguar', 'buick',
       'chrysler', 'volvo', 'audi', 'infiniti', 'lincoln', 'alfaromeo',
       'subaru', 'acura', 'hyundai', 'mercedesbenz', 'bmw', 'mitsubishi',
       'volkswagen', 'porsche', 'kia', 'rover', 'mini', 'pontiac', 'fiat',
       'tesla', 'saturn', 'mercury', 'harleydavidson', 'land rover',
       'astonmartin', 'ferrari'])
model = st.text_input('Model')
condition = st.selectbox('Condition', ['clean', 'lien', 'parts only', 'missing', 'rebuilt', 'salvage'])
cylinders = st.selectbox('Cylinder', [3, 4, 5, 6, 8])
odometer = st.number_input('Odometer')
title_status = st.selectbox('Title Status', ['clean', 'lien', 'parts only', 'missing', 'rebuilt', 'salvage'])
transmission = st.selectbox('Transmission', ['manual', 'other', 'automatic'])
drive = st.selectbox('Drive', ['4wd', 'fwd', 'rwd'])
type = st.selectbox('Type', ['pickup', 'truck', 'other', 'coupe', 'SUV', 'hatchback', 'mini-van', 'sedan', 'offroad', 'convertible', 'wagon', 'van', 'bus'])
paint_color = st.selectbox('Paint Color', ['white', 'blue', 'red', 'black', 'silver', 'grey', 'brown', 'yellow', 'orange', 'green', 'custom', 'purple'])
state = st.selectbox('State', ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'nc', 'ne', 'nv', 'nj', 'nm', 'ny', 'nh', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy'])
fuel = st.selectbox('Fuel', ['gas', 'other', 'diesel', 'hybrid', 'electric'])

# Prediction button
if st.button('Predict'):
    prediction = predict(region, year, manufacturer, model, condition, cylinders, odometer, title_status, transmission, drive, type, paint_color, state, fuel)
    st.write('Predicted Price:', prediction)
