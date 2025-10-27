import pandas as pd
import numpy as np

data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']}
df = pd.DataFrame(data)

categories = df['Color'].unique()
encoded = np.zeros((len(df), len(categories)), dtype=int)

for i, cat in enumerate(categories):
    for j, val in enumerate(df['Color']):
        if val == cat:
            encoded[j][i] = 1

for i, cat in enumerate(categories):
    df[cat] = encoded[:, i]

print(df)

