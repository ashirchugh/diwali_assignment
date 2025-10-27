import pandas as pd
import numpy as np

data = {'Age': [25, np.nan, 30, 35, np.nan, 40]}
df = pd.DataFrame(data)

mean_value = df['Age'][~df['Age'].isna()].mean()
df['Age_Mean_Imputed'] = [x if not np.isnan(x) else mean_value for x in df['Age']]

median_value = np.median(df['Age'][~df['Age'].isna()])
df['Age_Median_Imputed'] = [x if not np.isnan(x) else median_value for x in df['Age']]

values = df['Age'][~df['Age'].isna()].tolist()
mode_value = max(set(values), key=values.count)
df['Age_Mode_Imputed'] = [x if not np.isnan(x) else mode_value for x in df['Age']]

print(df)
