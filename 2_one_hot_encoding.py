import pandas as pd

data = pd.read_csv("data.csv")

encoded = pd.get_dummies(data, columns=["City", "Occupation"])

print("After one hot encoding:")
print(encoded.head())
