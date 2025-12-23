import pandas as pd
import numpy as np

# Create sample DataFrame with missing values
df = pd.DataFrame({
    "A": [10, 20, np.nan, 40],
    "B": [5, np.nan, 15, 20],
    "C": [np.nan, 8, 12, 16]
})

print("Original DataFrame:")
print(df)

# Replace missing values with 0
df_filled = df.fillna(0)

print("\nDataFrame after replacing missing values:")
print(df_filled)
