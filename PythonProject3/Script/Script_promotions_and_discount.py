import pandas as pd

df = pd.read_csv("../Input_CSV_files/Promotions_and_Discounts.csv")

df = df.dropna()
df = df.drop_duplicates()

df.to_csv("../Output_CSV_files/stats_promotions_and_discounts_clean.csv", index=False)

print("Fisierul curatat a fost salvat cu succes")