# Import library
import pandas as pd

# Load the dataset
file_path = "Dataset for Data Analytics.xlsx"
df = pd.read_excel(file_path)

# -----------------------------
# 1. Check Missing Values
# -----------------------------
print("Missing Values:")
print(df.isnull().sum())

# -----------------------------
# 2. Remove Duplicate Rows
# -----------------------------
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

# -----------------------------
# 3. Handle Missing Values
# -----------------------------
# Fill missing CouponCode values
if "CouponCode" in df.columns:
    df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# -----------------------------
# 4. Correct Data Formats
# -----------------------------
# Convert Date column to datetime
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])

# Convert numeric columns
numeric_columns = ["Quantity", "UnitPrice", "TotalPrice", "ItemsInCart"]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------
# 5. Final Check
# -----------------------------
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

# -----------------------------
# 6. Save Cleaned Dataset
# -----------------------------
output_file = "Cleaned_Dataset_for_Data_Analytics.xlsx"
df.to_excel(output_file, index=False)

print("\nDataset cleaned successfully!")
print("Saved as:", output_file)
