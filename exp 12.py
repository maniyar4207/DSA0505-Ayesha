import pandas as pd
import numpy as np

# Create DataFrame with random values
df = pd.DataFrame(
    np.random.randn(10, 4),
    columns=["A", "B", "C", "D"]
)

# Set background color black and font color yellow
styled_df = df.style.set_properties(
    **{
        "background-color": "black",
        "color": "yellow"
    }
)

styled_df
