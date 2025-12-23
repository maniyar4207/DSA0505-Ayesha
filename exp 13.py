import pandas as pd
import numpy as np

# Create sample DataFrame
df = pd.DataFrame({
    "A": [10, 20, np.nan, 40],
    "B": [5, np.nan, 15, 20],
    "C": [np.nan, 8, 12, 16]
})

# Detect missing values
missing_values = df.isna()

# Display result
print(missing_values)
