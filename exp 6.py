import pandas as pd
import matplotlib.pyplot as plt

# Sample Alphabet Inc. stock data
alphabet_stock_data = {
    "Date": ["2023-01-02", "2023-01-03", "2023-01-04",
             "2023-01-05", "2023-01-06"],
    "Close_Price": [88.73, 89.12, 87.85, 90.34, 92.01],
    "Volume": [22000000, 24500000, 23000000, 26000000, 28000000]
}

# Create DataFrame
df = pd.DataFrame(alphabet_stock_data)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Define date range
start_date = "2023-01-03"
end_date = "2023-01-06"

# Filter data between specific dates
filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

# Create scatter plot
plt.scatter(filtered_df["Close_Price"], filtered_df["Volume"])
plt.xlabel("Stock Price ($)")
plt.ylabel("Trading Volume")
plt.title("Alphabet Inc. Stock Price vs Trading Volume")
plt.show()
