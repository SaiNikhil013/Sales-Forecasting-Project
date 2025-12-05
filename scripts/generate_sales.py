import pandas as pd
import numpy as np
import json
import os
from datetime import datetime, timedelta

today = datetime.now().strftime("%Y-%m-%d")
folder = f"../data/raw/{today}/"

with open(folder + "products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

df_products = pd.DataFrame(products)

# Generate 90 days of sales data
dates = pd.date_range(end=datetime.now(), periods=90)

sales_data = []
for _, row in df_products.iterrows():
    for d in dates:
        sales_data.append({
            "product_code": row.get("code"),
            "date": d,
            "units_sold": np.random.randint(0, 50),
            "price": np.random.uniform(50, 300),
        })

df_sales = pd.DataFrame(sales_data)
df_sales.to_csv(folder + "sales.csv", index=False)

print("Dynamic sales data generated.")
