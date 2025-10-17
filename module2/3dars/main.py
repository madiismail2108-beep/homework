# def get_info(name, age, address, email):
#     print(get_info)
 
# name=input('ismu sharifingiz: ')
# age=int(input('yoshiz nechida: '))
# address=input('qayerda istiqomat qilasiz: ')
# email=input('emailizi kiriting: ')
# get_info(name, age, address, email)



def add(a,b):
    return a + b



# result = add(10,20)
# print(result)

def sub(a,b):
    return a - b


def mul(a,b):
    return a * b


def divide(a,b):
    return a/b

def menu():
    print('Add    => 1')
    print('Sub    => 2')
    print('Mul    => 3')
    print('Divide => 4')
    print('Exit   => q')
    return input('enter your choice?: ')

def calculator():
    while True:
        a = int(input('a : '))
        b = int(input('b : '))
        choice = menu()
        if choice == '1':
            result = add(a,b)
            print(result)
        elif choice == '2':
            result = sub(a,b)
            print(result)
        elif choice == '3':
            result = mul(a,b)
            print(result)
        elif choice == '4':
            result = divide(a,b)
            print(result)
        elif choice == 'q':
            return
    


if __name__ == '__main__':
    calculator()
   
        
    