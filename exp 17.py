import pandas as pd

# Create DataFrame
data = {
    "school_code": ["S001", "S002", "S001", "S003", "S002", "S001"],
    "class": ["V", "VI", "V", "VII", "VI", "VII"],
    "name": ["Alex", "John", "Martha", "Steve", "Lucy", "David"],
    "age": [11, 12, 10, 13, 12, 14]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Group by school code and calculate mean, min, max of age
result = df.groupby("school_code")["age"].agg(["mean", "min", "max"])

print("\nMean, Min and Max age for each school:")
print(result)
