# Customer Churnn Prediction

## 1. Overview

This project aims not only to predict the customer churn but also their interpretation using Explainable AI techniques. Customer churn refers to the percentage of customers that
stop using a company's product or service over a certain period. Identifying the potential churners using advanced machine learning techniques allow business to take proactive measures
to retain customers.

The project utilizes a machine learning model trained on historical customer data to predict whether a customer is likely to churn or not. The prediction is served through
a Flask web application, providing an easy-to-use interface for users to input customer data and obtain churn predictions

![Screenshot 2024-04-11 at 15 15 14](https://github.com/Adigo45/MasterThesis/assets/86388354/3ef09713-ac40-437e-a34d-04ea7b06b229)

## 2. Explainability of Model Prediction
- ##### Various Features at global level affecting the prediction of Customer Churn



<img width="937" alt="BeeswarmPlot" src="https://github.com/Adigo45/MasterThesis/assets/86388354/0088e276-d0dd-4f34-89ed-396c60bd365e">




- ##### Model interpreting why the particular customer churned and the impact of various features contributing to the particular prediction. Lime framework is used for this..



<img width="930" alt="Churn" src="https://github.com/Adigo45/MasterThesis/assets/86388354/7e6199a7-6260-4439-ae9f-360fd82868f3">



- ##### Model interpreting why the particular customer not churned and the impact of various features contributing to the particular prediction.

   <img width="988" alt="NotChurn" src="https://github.com/Adigo45/MasterThesis/assets/86388354/18a03991-8aaf-43f0-9e5e-44779558942c">




## 3. Features

- ### Data Cleaning:
  Processed and cleaned the dataset to handle missing values and outliers.
- ### Exploratory Data Analysis:
  Explored the dataset to understand the underlying patterns and relationships.
- ### Model Selection:
  Evaluated multiple machine learning algorithms and selected the best-performing one for customer
  churn prediction task.
- ### Model Training:
  Trained the selected model on the preprocessed dataset to predict customer churn.
- ### Model Evaluation:
  Evaluated the model's performance using appropriate metrics to ensure its reliability.
- ### Deployment:
  Deployed the model using a Flask web application, providing an interface for users to input
  customer data and recieve churn predictions.



## 4. Technology Used
- python
- scikit-learn
- Flask
- HTML/CSS
- Pandas
- NumPy
- Pickle


## 5. File Structure
ChurnPredictionDeployment/

app.py

model.pkl

templates/

-index.html

-result.html

requirements.txt

README.md


## 6. Getting Started

- ### Prerequisites
  - python 3.11.5
  - Pip (pacakage installer for python)
  - Git

- ### Installation
   - 1. Clone the repository:
        https://github.com/Adigo45/ChurnPredictionDeployment
   - 2. Navigate to the project directory:
        cd CustomerChurnDeployment
   - 3. Install the required packages:
        pip install -r requirements.txt

## 7. Usage
- 1. Run the Flask application:
  python app.py 
- 2. Open a web browser and navigate to http://127.0.0.1:5000 to access the application.
- 3. Fill in the customer details in the form and click on the "Predict" button to get the churn prediction.

## 8. Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 9. License
This project is licensed under the MIT License. See the License file for details.

