import pandas as pd
import numpy as np

data = {'City': ['Delhi', 'Mumbai', 'Kolkata', 'Delhi', 'Chennai']}
df = pd.DataFrame(data)

cities = df['City'].unique()

for city in cities:
    df[city] = [1 if x == city else 0 for x in df['City']]

print(df)
