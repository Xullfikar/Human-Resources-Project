import joblib
import pandas as pd


def input_user():
    input_data = {}
    input_data["MonthlyIncome"] = int(input("Monthly Income: "))
    input_data["Age"] = int(input("Age: "))
    input_data["MonthlyRate"] = int(input("Monthly Rate: "))
    input_data["DailyRate"] = int(input("Daily Rate: "))
    input_data["HourlyRate"] = int(input("Hourly Rate: "))
    input_data["TotalWorkingYears"] = int(input("Total Working Years: "))
    input_data["DistanceFromHome"] = int(input("Distance From Home: "))

    return input_data


def prediction_attrition(input):
    model = joblib.load("model.joblib")

    features = [
        "MonthlyIncome",
        "Age",
        "MonthlyRate",
        "DailyRate",
        "HourlyRate",
        "TotalWorkingYears",
        "DistanceFromHome",
    ]

    input_user_df = pd.DataFrame([input], columns=features)

    prediction = model.predict(input_user_df)
    return prediction[0]


prediction_result = prediction_attrition(input_user())

print("----------------------------------------------")
print("Prediction Attrition: ", "Yes 1" if prediction_result == 1 else "No 0")
print("----------------------------------------------")
