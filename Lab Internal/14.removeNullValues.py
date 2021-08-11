#Remove Null Values
import pandas as pd
file = pd.read_csv('details.csv')

x = file["Marks"].mean()

file["Marks"].fillna(x,inplace=True)
print(file.to_string())