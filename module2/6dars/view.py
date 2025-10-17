from random import randint
from id import products


def generate_product_id():
    return str(randint(1000,9999)) 

def product_list():
    product_values = products.values()
    for product in product_values:
        print(f'{product['product_id']} - {product['name']} - ${product['price']}')
    
result=product_list
print(result)