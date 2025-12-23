import pandas as pd
import matplotlib.pyplot as plt

# Sample trading volume data for Alphabet Inc.
data = {
    "Date": ["2023-01-02", "2023-01-03", "2023-01-04",
             "2023-01-05", "2023-01-06"],
    "Volume": [22000000, 24500000, 23000000, 26000000, 28000000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Define date range
start_date = "2023-01-03"
end_date = "2023-01-06"

# Filter data between specific dates
filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

# Create bar plot
plt.bar(filtered_df["Date"], filtered_df["Volume"])
plt.xlabel("Date")
plt.ylabel("Trading Volume")
plt.title("Alphabet Inc. Trading Volume")
plt.show()
