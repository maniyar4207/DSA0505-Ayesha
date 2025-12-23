import pandas as pd
import numpy as np

# Create sample DataFrame
df = pd.DataFrame({
    "A": [10, np.nan, np.nan, 40, np.nan],
    "B": [np.nan, np.nan, 15, 20, np.nan],
    "C": [np.nan, 8, np.nan, 16, np.nan],
    "D": [5, np.nan, 12, np.nan, 25]
})

print("Original DataFrame:")
print(df)

# Keep rows with at least 2 NaN values
result = df[df.isna().sum(axis=1) >= 2]

print("\nRows with at least 2 NaN values:")
print(result)
