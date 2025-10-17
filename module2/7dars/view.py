from random import randint
from cddd import products

def generate_product_id():
    return str(randint(1000,9999))

def product_list():
    try:
     for product in products.values() :
        print(f'{product['product_id']} - {product['name']} - ${product['price']}')
    except Exception as e:
        print(f'Error:{e}')

def get_product(product_id):
    try:
     if product_id not in products:
        raise Exception("Product not found!")
     return products[product_id]
    except Exception as e:
        return f'Error:{e}'

def create_product():
    try:
     product_id = generate_product_id()
     if product_id in products:
       raise Exception('Product already exists')
     name = input('Name: ')
     description = input('Description: ')
     color = input('Color: ')
     try:
         price = float(input('Price: '))
     except ValueError:
        raise Exception("Price must be a number!")

     products[product_id] = {
        'name':name,
        'description':description,
        'color':color,
        'price':price,
        'product_id':product_id
       }
     return 'Product successfully created'
    except Exception as e:
        return f"Error: {e}"



def delete_product(product_id):
    try:
     if product_id not in products:
       raise Exception(f"Product with ID {product_id} not found!")
     products.pop(product_id)
     return 'Product is deleted'
    except Exception as e:
        return f"Error: {e}"




def update_products():
    try:
     product_id=input('enter product id:')
     if product_id not in products:
        raise Exception('there is nothing with this id')
    
     product = products[product_id]

     print(f'{products} information')
     for key, value in product.items():
        print(f'{key} : {value}')

        print("what you want to update?")
     print("name => 1")
     print("description => 2")
     print("color => 3")
     print("price => 4")
     print("all information => 5")
     print("exit => ex")

     choise = input('choose one option: ')

     if choise == '1':
        product['name'] = input('new name: ')
     elif choise == '2':
        product['description'] = input('new description: ')
     elif choise == '3':
        product['color'] = input('new color')
     elif choise == '4':
        try:
         product['price'] = int(input('new price: '))
        except ValueError:
           raise Exception('price must be number!') 
     elif choise == '5':
      product['name'] = input('new name: ')
      product['description'] = input('new description: ')
      product['color'] = input('new color')
      try:
         product['price'] = int(input('new price: '))
      except ValueError:
           raise Exception('price must be number!') 
     elif choise == 'ex':
      return
     else:
        raise Exception('this choise not avaliable')
     return 'updated successfully'
    except Exception as e:
       return f' Error: {e} '
  
    