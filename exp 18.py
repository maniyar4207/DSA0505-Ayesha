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

# Group by school code and class
grouped = df.groupby(["school_code", "class"])

print("\nData grouped by School Code and Class:")
for name, group in grouped:
    print(f"\nGroup: {name}")
    print(group)
