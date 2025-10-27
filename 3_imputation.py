import pandas as pd

data = pd.read_csv("data.csv")

# Fill missing values
data["Age"] = data["Age"].fillna(data["Age"].mean())
data["Salary"] = data["Salary"].fillna(data["Salary"].median())

print("After imputation:")
print(data.isnull().sum())
