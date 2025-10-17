from datetime import datetime
import json
from database import load_data, save_detail

def product_list():
    products: dict[str, dict] = load_data()
    for values in products.values():
        print(json.dumps(values, indent=4, default=str)) 

def create_products(
    name: str,
    description: str | None = None,
    price: float = 0.0,
    product_id: str = "",
    protection: str = "",
    OS: str = "",
    color: str = "",
    material: str = "",
    created_at: datetime=datetime.now()
):
    products = load_data()

    if product_id in products:
        return 'This product already exists'
    
    characters = {
        "OS": OS,
        "color": color,
        "material": material,
        "protection": protection
    }

    products[product_id] = {
        "name": name,
        "description": description,
        "price": price,
        "product_id": product_id,
        "created_at": created_at.isoformat(),  
        "characters": characters
    }

    save_detail(products)
    return "Product created"

def get_product(product_id:str):
    products = load_data()
    if product_id not in products:
        return 'Not found'
    
    return products[product_id]

def delete_product(product_id:str):
    products = load_data()
    if product_id not in products:
        return 'Not found'
    
    products.pop(product_id)

def update_product(product_id, **info):
    products = load_data()
    if product_id not in products:
        return 'Not found'
    for key, value in info.items():
        if key in products[product_id]:
            products[product_id][key] = value
        elif key in products[product_id]['characters']:
            products[product_id]['characters'][key]=value
        else:
            return f'{key} not found'
    
    save_detail(products)
    return "product updated"

    
