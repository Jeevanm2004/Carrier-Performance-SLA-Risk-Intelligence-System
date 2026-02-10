import pandas as pd
import numpy as np

# Load raw dataset (never modify original file)
df = pd.read_csv("../SLA Dataset/b2b_sla_logistics_dataset_200k.csv")

print("Initial dataset shape:", df.shape)
# -----------------------------
# Handle Missing Values
# -----------------------------

# Separate numeric and categorical columns
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
categorical_cols = df.select_dtypes(include=["object"]).columns

# Fill numeric missing values with median
for col in numeric_cols:
    if df[col].isnull().any():
        df[col].fillna(df[col].median(), inplace=True)

# Fill categorical missing values with 'Unknown'
for col in categorical_cols:
    if df[col].isnull().any():
        df[col].fillna("Unknown", inplace=True)

print("Missing values after handling:", df.isnull().sum().sum())
# -----------------------------
# Fix Date Columns
# -----------------------------

date_cols = [c for c in df.columns if "date" in c.lower()]

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")

print("Date columns converted:", date_cols)
# -----------------------------
# Remove Duplicate Records
# -----------------------------

before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print("Duplicate rows removed:", before - after)
# -----------------------------
# Sanity Checks
# -----------------------------

if "shipping_cost" in df.columns:
    df = df[df["shipping_cost"] >= 0]

if "weight" in df.columns:
    df = df[df["weight"] >= 0]

if "volume" in df.columns:
    df = df[df["volume"] >= 0]

if "planned_delivery_days" in df.columns:
    df = df[df["planned_delivery_days"] > 0]

print("Shape after sanity checks:", df.shape)
# -----------------------------
# Save Cleaned Dataset
# -----------------------------

df.to_csv("week1_cleaned_data.csv", index=False)
print("Saved cleaned dataset: week1_cleaned_data.csv")
# -----------------------------
# Step 5: Target Variable Creation
# -----------------------------

df = pd.read_csv("week1_cleaned_data.csv")
print("Loaded cleaned dataset:", df.shape)
# Create SLA breach flag
df["sla_breach_flag"] = (
    df["actual_delivery_days"] > df["planned_delivery_days"]
).astype(int)

print("SLA breach flag created")
# -----------------------------
# Validate SLA Breach Flag
# -----------------------------

print("\nSLA Breach Flag Distribution:")
print(df["sla_breach_flag"].value_counts())

print("\nSLA Breach Percentage:")
print(df["sla_breach_flag"].value_counts(normalize=True) * 100)

print("\nUnique values in sla_breach_flag:")
print(df["sla_breach_flag"].unique())
# -----------------------------
# Save Dataset with Target Variable
# -----------------------------

df.to_csv("week1_cleaned_data.csv", index=False)
print("Updated dataset with SLA breach flag saved")
# ----------------------------
# Step 6: Encode Categorical Variables (memory-safe)

categorical_cols = [
    "carrier",
    "shipping_mode",
    "region",
    "origin_country",
    "destination_country"
]

print("Categorical columns selected for encoding:", categorical_cols)

df_encoded = pd.get_dummies(
    df,
    columns=categorical_cols,
    drop_first=True
)

print("Dataset after encoding:", df_encoded.shape)

df_encoded.to_csv("week1_encoded_data.csv", index=False)
print("Saved encoded dataset: week1_encoded_data.csv")
# Step 7: Final Data Validation

print("\nFinal Data Validation Checks")

# Check for negative values in critical numeric fields
numeric_checks = ["shipping_cost", "weight", "volume", "planned_delivery_days", "actual_delivery_days"]
existing_numeric_checks = [col for col in numeric_checks if col in df.columns]

for col in existing_numeric_checks:
    negatives = (df[col] < 0).sum()
    print(f"Negative values in {col}: {negatives}")

# Validate SLA breach flag
print("\nSLA Breach Flag Validation:")
print(df["sla_breach_flag"].value_counts())

# Final dataset shape
print("\nFinal dataset shape:", df.shape)

print("\nFinal data validation completed successfully.")

