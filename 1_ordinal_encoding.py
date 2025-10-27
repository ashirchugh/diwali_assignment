import pandas as pd

data = pd.read_csv("data.csv")

gender_map = {"Male": 1, "Female": 0}
data["Gender"] = data["Gender"].map(gender_map)

edu_map = {"High School": 1, "Graduate": 2, "Postgraduate": 3}
data["Education"] = data["Education"].map(edu_map)

print("After ordinal encoding:")
print(data.head())
