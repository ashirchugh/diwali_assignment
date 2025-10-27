import pandas as pd

data = {'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small', 'Large']}
df = pd.DataFrame(data)

order = ['Small', 'Medium', 'Large']
mapping = {value: index + 1 for index, value in enumerate(order)}

df['Size_Encoded'] = [mapping[item] for item in df['Size']]

print(df)
