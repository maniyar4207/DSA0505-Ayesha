import pandas as pd

# Create DataFrame
data = {
    "school_code": ["S001", "S002", "S001", "S003", "S002", "S001"],
    "class": ["V", "VI", "V", "VII", "VI", "VII"],
    "student_name": ["Alex", "John", "Martha", "Steve", "Lucy", "David"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Group by school_code
grouped = df.groupby("school_code")

print("\nData grouped by School Code:")
for name, group in grouped:
    print(f"\nSchool Code: {name}")
    print(group)

# Check type of GroupBy object
print("\nType of GroupBy object:")
print(type(grouped))
