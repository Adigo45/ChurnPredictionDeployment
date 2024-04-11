from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder


app = Flask(__name__)

## load the trained model and preprocessing steps
with open('model.pkl', 'rb') as file:
    pipe_best = pickle.load(file)



@app.route('/')
def index():
    return render_template('form.html')

@app.route('/predict',methods=['POST'])
def predict():
    # Get data from the request form
    data = {
        'EstimatedSalary': float(request.form['EstimatedSalary']),
        'CreditScore': float(request.form['CreditScore']),
        'Age' : float(request.form['Age']),
        'Tenure': int(request.form['Tenure']),
        'Balance': float(request.form['Balance']),
        'NumOfProducts': int(request.form['NumOfProducts']),
        'IsActiveMember': int(request.form['IsActiveMember']),
        'HasCrCard': int(request.form['HasCrCard']),
        'Geography' : request.form['Geography'],
        'Gender' :request.form['Gender']      
    }

    ## Convert to DataFrame

    df = pd.DataFrame([data])

    # Preprocess the Data

    X = pipe_best['Encoding'].transform(df)


    # Make Prediction

    prediction = pipe_best['Estimator'].predict(X)
    if prediction[0] == 0:
        prediction = 'Not Churn'
    else:
        prediction = 'Churn'
    return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug= True)
