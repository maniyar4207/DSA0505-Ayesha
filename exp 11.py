import pandas as pd
import numpy as np

# Create DataFrame with random values
df = pd.DataFrame(
    np.random.randint(1, 100, size=(10, 4)),
    columns=["Col1", "Col2", "Col3", "Col4"]
)

# Convert some values to NaN
df.iloc[1, 2] = np.nan
df.iloc[4, 0] = np.nan
df.iloc[7, 3] = np.nan

# Function to highlight NaN values
def highlight_nan(value):
    if pd.isna(value):
        return 'background-color: yellow'
    return ''

# Highlight NaN values (updated method)
df.style.map(highlight_nan)
