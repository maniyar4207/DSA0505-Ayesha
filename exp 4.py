import pandas as pd
import matplotlib.pyplot as plt

# Sample historical stock price data for Alphabet Inc.
data = {
    "Date": ["2023-01-02", "2023-01-03", "2023-01-04",
             "2023-01-05", "2023-01-06"],
    "Close_Price": [88.73, 89.12, 87.85, 90.34, 92.01]
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

# Create line plot
plt.plot(filtered_df["Date"], filtered_df["Close_Price"])
plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.title("Alphabet Inc. Stock Prices")
plt.show()
