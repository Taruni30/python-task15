import pandas as pd

df = pd.read_csv("dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
df.info()

df.fillna(0, inplace=True)

if "age" in df.columns:
    df.sort_values(by="age", inplace=True)

if "department" in df.columns:
    print("\nGroup By Department:")
    print(df.groupby("department").size())

if "salary" in df.columns:
    df["bonus"] = df["salary"] * 0.10

df.to_csv("cleaned_dataset.csv", index=False)

print("\nData analysis completed!")
