from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the review and model from the form data
    review = request.form['review']
    model = request.form['model']

    # Define the API endpoint for the selected model
    endpoint = f'http://localhost:8000/predict/{model}'

    # Send the review data to the API endpoint
    response = requests.post(endpoint, json={'review_es': review})

    # Parse the prediction from the API response
    prediction = response.json()

    # Render the HTML template with the prediction
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)