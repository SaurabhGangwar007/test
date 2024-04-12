import pandas as pd
import pickle
import streamlit as st

# Load the saved Ridge model
model_filename = r'C:\Users\Sourav Sharma\Desktop\Bhavik project\UsedCar.pkl'
with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Define available options
manufacturer_options = ['gmc', 'chevrolet', 'toyota']
condition_options = ['good', 'excellent', 'fair', 'like new', 'new', 'salvage']

# Streamlit app
st.title('Car Price Prediction')

# Sidebar for user input
st.sidebar.header('User Input')
user_input = {}
features = ['year', 'manufacturer', 'condition', 'odometer']

for feature in features:
    if feature == 'manufacturer':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', manufacturer_options)
    elif feature == 'condition':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', condition_options)
    elif feature == 'year':
        user_input[feature] = st.sidebar.number_input(f'Enter the {feature}:', min_value=1900, max_value=2024, step=1)
    else:
        user_input[feature] = st.sidebar.number_input(f'Enter the {feature}:')

# Add a "Submit" button
if st.sidebar.button('Submit'):
    # Convert user input to a DataFrame
    user_df = pd.DataFrame([user_input])

    # Perform one-hot encoding for categorical columns
    user_df_encoded = pd.get_dummies(user_df, columns=['manufacturer', 'condition'], drop_first=False)

    # Filter the encoded DataFrame to include only the features that the model expects
    user_df_encoded = user_df_encoded[['year'] + sorted(manufacturer_options) + sorted(condition_options)]

    # Make prediction using the loaded model
    user_prediction = loaded_model.predict(user_df_encoded)

    # Display the prediction
    st.subheader('Prediction Result')
    formatted_prediction = "${:.2f}".format(user_prediction[0])
    st.write(f'The predicted price for the car is: {formatted_prediction}')