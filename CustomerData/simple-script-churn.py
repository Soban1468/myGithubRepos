import pickle
import pandas as pd
print('Welcome to Churn Prediction Model:')
gender = int(input("Please enter your gender (1 for male , 2 for female , 0 for others): "))
age = int(input("Please enter your age: "))
usage_history = float(input("Please enter your usage history (between 0 to 1): "))
location_london = int(input("Please enter 1 if your location is London otherwise enter 0: "))
location_New_York = int(input("Please enter 1 if your location is New_York otherwise enter 0: "))
location_Sydney = int(input("Please enter 1 if your location is Sydney otherwise enter 0: "))
location_Tokyo = int(input("Please enter 1 if your location is Tokyo otherwise enter 0: "))
location_Toronto = int(input("Please enter 1 if your location is Toronto otherwise enter 0: "))
status_Active = int(input("Please enter 1 if your status is Active otherwise enter 0: "))
status_Inactive = int(input("Please enter 1 if your status is Inactive otherwise enter 0: "))
status_Cancelled = int(input("Please enter 1 if your status is Cancelled otherwise enter 0: "))
data = {
    'gender' : gender,
    'age' : age,
    'usage_history' : usage_history,
    'location_London' : location_london,
    'location_New York' : location_New_York,
    'location_Sydney' : location_Sydney,
    'location_Tokyo' : location_Tokyo,
    'location_Toronto' : location_Toronto,
    'status_Active' : status_Active,
    'status_Cancelled' : status_Cancelled,
    'status_Inactive' : status_Inactive
}
data = pd.DataFrame([data])
with open(r'F:\Python codes\machine-learning Practices\CustomerData\churn-model.pkl' , 'rb') as file:
    Model = pickle.load(file)

y_predict = Model.predict(data)
if y_predict[0] == 1:
    print("Customer is at high risk of churn.")
else:
    print("Customer is likely to stay.")

