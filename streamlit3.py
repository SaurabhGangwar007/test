import pandas as pd
import pickle
import streamlit as st

# Load the saved Ridge model
model_filename = r'C:/Users/20rew/Downloads/used_car_price_model.pkl'
with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Define available options
manufacturer_options = ['gmc', 'chevrolet', 'toyota', 'ford', 'jeep', 'nissan', 'ram',
       'mazda', 'cadillac', 'honda', 'dodge', 'lexus', 'jaguar', 'buick',
       'chrysler', 'volvo', 'audi', 'infiniti', 'lincoln', 'alfaromeo',
       'subaru', 'acura', 'hyundai', 'mercedesbenz', 'bmw', 'mitsubishi',
       'volkswagen', 'porsche', 'kia', 'rover', 'mini', 'pontiac', 'fiat',
       'tesla', 'saturn', 'mercury', 'harleydavidson', 'land rover',
       'astonmartin', 'ferrari']

condition_options = ['good', 'excellent', 'fair', 'like new', 'new', 'salvage']

title_status_options = ['clean', 'lien', 'parts only', 'missing', 'rebuilt', 'salvage']

transmission_options = ['manual', 'other', 'automatic']

drive_options = ['4wd', 'fwd', 'rwd']

type_options = ['pickup', 'truck', 'other', 'coupe', 'SUV', 'hatchback',
                'mini-van', 'sedan', 'offroad', 'convertible', 'wagon', 'van', 'bus']

paint_color_options = ['white', 'blue', 'red', 'black', 'silver', 'grey', 'brown',
                       'yellow', 'orange', 'green', 'custom', 'purple']

state_options = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga',
                 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma',
                 'mi', 'mn', 'ms', 'mo', 'mt', 'nc', 'ne', 'nv', 'nj', 'nm', 'ny',
                 'nh', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx',
                 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

fuel_options = ['gas', 'other', 'diesel', 'hybrid', 'electric']

# Streamlit app
st.title('Car Price Prediction')

# Sidebar for user input
st.sidebar.header('User Input')
user_input = {}
features = ['region', 'year', 'manufacturer', 'model', 'condition', 'cylinder', 'odometer',
            'title_status', 'transmission', 'drive', 'type', 'paint_color', 'state', 'fuel']

for feature in features:
    if feature == 'manufacturer':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', manufacturer_options)
    elif feature == 'condition':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', condition_options)
    elif feature == 'title_status':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', title_status_options)
    elif feature == 'transmission':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', transmission_options)
    elif feature == 'drive':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', drive_options)
    elif feature == 'type':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', type_options)
    elif feature == 'paint_color':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', paint_color_options)
    elif feature == 'state':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', state_options)
    elif feature == 'fuel':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', fuel_options)
    elif feature == 'year':
        user_input[feature] = st.sidebar.number_input(f'Enter the {feature}:', min_value=1989, max_value=2024, step=1)
    else:
        user_input[feature] = st.sidebar.text_input(f'Enter the {feature}:')


print(user_input)
# Add a "Predict" button
if st.sidebar.button('Predict'):
    # Convert user input to a DataFrame
    user_df = pd.DataFrame([user_input.values()], columns=['region', 'year', 'manufacturer', 'model', 'condition',
                                                          'cylinders', 'odometer', 'title_status', 'transmission',
                                                          'drive', 'type', 'paint_color', 'state', 'fuel'])

    print(user_df)

    
    user_prediction = loaded_model.predict(user_df)

    # Display the prediction
    st.subheader('Prediction Result')
    formatted_prediction = "${:.2f}".format(user_prediction[0])
    st.write(f'The predicted price for the car is: {formatted_prediction}')