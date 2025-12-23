import pandas as pd

# Sample sales data
sales_data = {
    "Item": ["Pen", "Pen", "Pencil", "Pencil", "Notebook", "Notebook"],
    "Region": ["East", "West", "East", "West", "East", "West"],
    "Units_Sold": [120, 150, 200, 180, 90, 110]
}

# Create DataFrame
df = pd.DataFrame(sales_data)

# Create pivot table for item-wise units sold
pivot_table = pd.pivot_table(
    df,
    index="Item",
    values="Units_Sold",
    aggfunc="sum"
)

# Display result
print(pivot_table)
