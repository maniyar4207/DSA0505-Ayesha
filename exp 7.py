import pandas as pd

# Sample sales data
sales_data = {
    "Item": ["Pen", "Pen", "Pencil", "Pencil", "Notebook", "Notebook"],
    "Region": ["East", "West", "East", "West", "East", "West"],
    "Sale_Value": [1200, 1500, 800, 950, 2000, 1800]
}

# Create DataFrame
df = pd.DataFrame(sales_data)

# Create pivot table to find max and min sale value
pivot_table = pd.pivot_table(
    df,
    index="Item",
    values="Sale_Value",
    aggfunc=["max", "min"]
)

# Display result
print(pivot_table)
