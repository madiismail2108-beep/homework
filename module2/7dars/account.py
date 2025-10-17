from pr import loggin, register, logout
from view import  product_list, get_product,create_product,delete_product, update_products

def menu():
    print('loggin => 1')
    print('regisrter => 2')
    print('logout => 3')
    print('exit => ex')
    return input('your choice: ')

def sub_menu():
    print('create product => 1')
    print('update product => 2')
    print('delete product => 3')
    print('back to home   => q')
    return input('?:')

def run():
    while True:
        choice = menu()
        if choice == '1':
            message = loggin()
            print(message)
            sub_choice = sub_menu()
            if sub_choice == '1':
                message = create_product()
                print(message)
            elif sub_choice == '2':
                message = update_products()
                print(message)
            
            elif sub_choice == '3':
                product_id = str(input('product ID : '))
                message = delete_product(product_id)
                print(message)
            
            elif sub_choice == 'q':
                continue
            
        elif choice == '2':
            message = logout()
            print(message)
        elif choice == '3':
            message = register()
            print(message)
        elif choice == '4':
            product_list()
        
        elif choice == '5':
            product_id = str(input('enter your product ID : '))
            message = get_product(product_id)
            print(message)
            
        elif choice == 'q':
            print('Come back again.')
            break
        
        else:
            print('invalid choice')
            
if __name__ == '__main__':
    run()




