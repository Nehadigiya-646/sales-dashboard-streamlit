import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Date range
dates = pd.date_range(start="2024-01-01", end="2024-12-31")

products = {
    "Electronics": ["Laptop", "Mobile", "Tablet", "Monitor", "Headphones", "Keyboard", "Mouse", "Printer"],
    "Furniture": ["Chair", "Table", "Sofa", "Desk"],
    "Stationery": ["Books", "Notebook", "Pen"]
}

regions = ["North", "South", "East", "West"]

data = []

for _ in range(3000):  # Change to 5000 or 10000 if you want bigger
    category = np.random.choice(list(products.keys()))
    product = np.random.choice(products[category])
    quantity = np.random.randint(1, 20)
    price = np.random.randint(100, 50000)
    date = np.random.choice(dates)
    region = np.random.choice(regions)

    data.append([date, product, category, quantity, price, region])

df = pd.DataFrame(data, columns=["Date", "Product", "Category", "Quantity", "Price", "Region"])

df.to_csv("sales_data.csv", index=False)

print("Bigger dataset created successfully!")