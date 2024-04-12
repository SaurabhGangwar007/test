from flask import Flask, render_template, request, jsonify
import joblib
from transformers import pipeline

app = Flask(__name__, template_folder='C:/Users/Sourav Sharma/Desktop/Bhavik project/templates')

# Load the regression model
regression_model = joblib.load('C:/Users/Sourav Sharma/Desktop/Bhavik project/df.pkl')

# Load the sentiment analysis model from Hugging Face
sentiment_model = pipeline('sentiment-analysis')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_regression', methods=['POST'])
def predict_regression():
    try:
        # Get car details from the request
        car_details = request.json

        # Extract individual details
        year = int(car_details['year'])
        manufacturer = car_details['manufacturer']
        model = car_details['model']
        condition = car_details['condition']
        odometer = float(car_details['odometer'])

        # Example: Dummy prediction based on random values
        # Replace this with your actual prediction logic using the loaded model
        predicted_price = 25000

        return jsonify({'prediction': predicted_price})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    try:
        # Get text input from the request
        text = request.json['text']

        # Run sentiment analysis
        result = sentiment_model(text)

        # Extract the predicted label from the result
        predicted_label = result[0]['label']

        return jsonify({'prediction': predicted_label})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)