from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("house_price_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form.get(f)) for f in [
            'GrLivArea', 'GarageCars', 'GarageArea',
            'TotalBsmtSF', 'FullBath', 'YearBuilt', 'OverallQual'
        ]]
        prediction = model.predict([features])[0]
        prediction = round(prediction, 2)
        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return f" Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)