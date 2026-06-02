import pandas as pd
import os

df = pd.read_csv("Data/Raw/nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"], dayfirst=True)

# Sort by date
df = df.sort_values("date")

# Remove duplicates
df = df.drop_duplicates()

# Create Processed folder
os.makedirs("Data/Processed", exist_ok=True)

# Save cleaned data
df.to_csv("Data/Processed/nav_cleaned.csv", index=False)

print("Cleaned dataset saved successfully")
print("Shape:", df.shape)
print(df.head())