import requests
import json
import os
from datetime import datetime

def fetch_products(page_size=100, pages=5):
    base_url = "https://world.openfoodfacts.org/api/v2/search"
    all_products = []

    for page in range(1, pages + 1):
        params = {
            "page": page,
            "page_size": page_size,
            "fields": "code,product_name,brands,categories,nutriscore_grade,quantity,serving_size",
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        all_products.extend(data.get("products", []))

    return all_products

def save_json(data):
    today = datetime.now().strftime("%Y-%m-%d")
    folder = f"../data/raw/{today}/"
    os.makedirs(folder, exist_ok=True)

    with open(folder + "products.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Saved data to {folder}products.json")

if __name__ == "__main__":
    data = fetch_products()
    save_json(data)
