import pandas as pd

df = pd.read_csv("../Input_CSV_files/Monthly_Seasonal_Planning.csv")

df = df.dropna()
df = df.drop_duplicates()

df.to_csv("../Output_CSV_files/stats_monthly_seasonal_planning_clean.csv", index=False)

print("Fisierul curatat a fost salvat cu succes")