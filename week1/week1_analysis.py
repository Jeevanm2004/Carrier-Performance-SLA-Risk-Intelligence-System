import pandas as pd

# Load the dataset
df = pd.read_csv("../SLA Dataset/b2b_sla_logistics_dataset_200k.csv")

# Basic inspection
print(df.head())
print("\nShape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nDescribe:")
print(df.describe(include="all"))
#