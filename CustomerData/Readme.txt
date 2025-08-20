----------------------------
|Customer Churn Prediction:|
----------------------------

1: Project Goal
The purpose of this project is to build a **Machine Learning model** that predicts whether a customer will **churn (leave the service)** or **stay**.  
We use **Logistic Regression** as a baseline model to classify churn based on customer attributes like:

- Gender  
- Age  
- Usage history  
- Location  
- Account status  

The trained model is saved and can be reused to make predictions on new customer data.

---

## Project Workflow
1. **Data Cleaning & Data Preprocessing** → `Data_Cleaning_Preprocessing.ipynb`
2. **Exploratory Data Analysis** → `EDA.ipynb`
3. **Model Training** → `ChurnPredictionModel.ipynb`
4. **Final Script** → `simple-script-churn.py`
5. **Readme** → Readme.txt


---

2: How to Run the Project

### 1. Clone the repository or download files
```bash
git clone <your-repo-link>
cd CustomerData

---

3: Install dependencies

pip install -r requirements.txt

---
4: Train the model

If you want to retrain the model:
python train_churn_model.py
This will generate a file called churn-model.pkl, which contains the trained Logistic Regression model.

---

5: Run the prediction script
python simple-script-churn.py


You will be asked to enter customer details (age, gender, location, etc.).
The script will then load the saved model and predict whether the customer will churn.

---

6: Example Output:

Welcome to Churn Prediction Model:
Please enter your gender (1 for male , 2 for female , 0 for others): 1
Please enter your age: 20
Please enter your usage history (between 0 to 1): 0.987
Please enter 1 if your location is London otherwise enter 0: 0
Please enter 1 if your location is New_York otherwise enter 0: 0
Please enter 1 if your location is Sydney otherwise enter 0: 0
Please enter 1 if your location is Tokyo otherwise enter 0: 1
Please enter 1 if your location is Toronto otherwise enter 0: 0
Please enter 1 if your status is Active otherwise enter 0: 1
Please enter 1 if your status is Inactive otherwise enter 0: 0
Please enter 1 if your status is Cancelled otherwise enter 0: 0
Customer is likely to stay.

---

