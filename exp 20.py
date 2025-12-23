import pandas as pd

# Create DataFrame
data = {
    "Country": ["Viet Nam", "Uruguay", "Cte d'Ivoire", "Colombia", "Saint Kitts and Nevis"],
    "Beverage": ["Wine", "Other", "Wine", "Beer", "Beer"]
}

df = pd.DataFrame(data)

# Find index of rows containing substring 'Beer' in Beverage column
substring_index = df[df["Beverage"].str.contains("Beer")].index

print("Index of rows containing substring 'Beer':")
print(list(substring_index))
