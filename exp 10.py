import pandas as pd
import numpy as np

# Create a DataFrame with random values
df = pd.DataFrame(
    np.random.randint(1, 100, size=(10, 4)),
    columns=["A", "B", "C", "D"]
)

# Convert some values to NaN
df.iloc[2, 1] = np.nan
df.iloc[5, 3] = np.nan
df.iloc[7, 0] = np.nan

# Function to highlight NaN values
def highlight_nan(val):
    if pd.isna(val):
        return 'background-color: yellow'
    return ''

# Display DataFrame with highlighted NaN values
df.style.map(highlight_nan)
