House Price Prediction Web App

This is a Machine Learning-based web application that predicts house prices using features such as area, number of garage cars, total basement area, and more. The model was trained on the Ames Housing Dataset in Google Colab, and deployed using Flask as a web app.


📌 Project Highlights

- 🔍 ML Model: Random Forest Regressor (trained in Google Colab)
- ⚙️ Backend: Python Flask
- 🎨 Frontend: HTML + Bootstrap CSS
- 🧠 Inputs: 7 house features
- 📦 Output: Predicted house price
- ✅ Easy to run locally
- 🌐 Ready to deploy on Render or Vercel


🧠 Tech Stack

| Layer      | Technology            |
|------------|------------------------|
| ML Model   | scikit-learn, Pandas, NumPy |
| Backend    | Flask (Python)         |
| Frontend   | HTML5, Bootstrap5      |
| IDE        | Google Colab (for training) |
| Hosting    | Render (optional)      |


📥 Input Features

The model takes the following 7 input features**:

| Feature Name      | Description                       |
|-------------------|-----------------------------------|
| `Gr_Liv_Area`     | Ground living area (in sq. ft.)   |
| `Garage_Cars`     | Number of cars in garage          |
| `Garage_Area`     | Garage area (in sq. ft.)          |
| `Total_Bsmt_SF`   | Basement area (in sq. ft.)        |
| `Full_Bath`       | Number of full bathrooms          |
| `Year_Built`      | Construction year of the house    |
| `Overall_Qual`    | Overall quality (1 = Low, 10 = High)|

---

🔧 How to Run Locally

> ⚠️ Make sure Python 3.x is installed

📌 Step-by-step:

```bash
# 1. Clone the repository
git clone https://github.com/santhiya0607/HousePricePredictionApp.git
cd HousePricePredictionApp

2. Create virtual environment (optional but recommended)

python -m venv venv

# For Windows
venv\Scripts\activate

# For Mac/Linux
source venv/bin/activate

# 3. Install all required libraries
pip install -r requirements.txt

# 4. Run the Flask app
python app.py


