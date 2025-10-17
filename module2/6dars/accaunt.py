from my_pr import loggin
from my_pr import register
from my_pr import logout

def menu():
    print('loggin => 1')
    print('regisrter => 2')
    print('logout => 3')
    print('exit => ex')
    return input('your choice: ')

def run():
    while True:
        choice = menu()
        if choice == '1':
         message = loggin()
         print(message)
        elif choice == '2':
         message = register()
         print(message)
        elif choice == '3':
         message = logout()
         print(message)
        elif choice == 'q':
         print('Come back again.')
         return
        else:
            print('invalid choice')

if __name__ == '__main__':
 run()


