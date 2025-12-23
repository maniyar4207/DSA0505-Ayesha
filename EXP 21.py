import pandas as pd

# Create DataFrame
data = {
    "Name": ["Alex", "mArThA", "JOHN", "luCy"],
    "City": ["New York", "LoNDoN", "PaRiS", "BeRlIn"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Swap case of the 'Name' column
df["Name"] = df["Name"].str.swapcase()

print("\nDataFrame after swapping case of Name column:")
print(df)
