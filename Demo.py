import pandas as pd
import numpy as np

#df = pd.read_csv(r"C:\Users\halstead_rideriver\Downloads\Pre can data Y-axis.csv").to_string(index=False)
df = pd.read_csv(r"C:\Users\halstead_rideriver\Downloads\Pre can data Y-axis.csv")
# print(df)
#print(df.columns)
df2 = df.to_numpy()
arr = np.array(df2)
arr2 = arr[0]
print(arr2[1:])