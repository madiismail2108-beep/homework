import json
from datetime import datetime

file_path = 'products.json'


def product_list():
    try:
        with open(file_path, 'r') as f:
            return json.load(f)   
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def create_product(name, description, price, created_at=datetime):
    
    products = product_list() 
    product = {
        "name": name,
        "description": description,
        "price": price,
        "created_at": str(created_at)
    }
    products.append(product)
    with open(file_path, 'a+') as f:
        json.dump(products, f, indent=4)
        
    return products

def read_products():
    with open(file_path, 'r') as f:
        json.dump(product_list, f, indent=4)

def delete_product(name=input):
    products = product_list()
    updated = [p for p in products if p["name"] != name]

    if len(products) == len(updated):
        return f"Product '{name}' not found"

    with open(file_path, 'a+') as f:
       json.dump(updated, f, indent=4)

    return f"Product '{name}' deleted"
 

def update_product(name, new_description, new_price, created_at=datetime):
    products = product_list()
    found = False

    for product in products:
        if product["name"] == name:
            if new_description:
                product["description"] = new_description
            if new_price:
                product["price"] = new_price
            found = True
            break

    if not found:
        return f"Product '{name}' not found"

    with open(file_path, 'a+') as f:
        json.dump(products, f, indent=4)

    return f"Product '{name}' updated"

