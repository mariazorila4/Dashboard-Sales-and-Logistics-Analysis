import pandas as pd

df = pd.read_csv("../Input_CSV_files/Product_Information.csv")

df = df.dropna()
df = df.drop_duplicates()

df.to_csv("../Output_CSV_files/stats_product_information_clean.csv", index=False)

print("Fisierul curatat a fost salvat cu succes")