from servise import login,register,logout,add_todo

def login_page():
    username = input('Username : ')
    password = input('Password : ')
    response = login(username,password)
    print(response)

def register_page():
    username = input('Username : ')
    password = input('Password : ')
    email = input('Email : ')
    response = register(username,password)
    print(response)


def logout_page():
    response = logout()
    print(response)

def add_todo_page():
    response = add_todo()
    print(response)

def menu():
    print("""
          Login => 1
          Register => 2
          Logout => 3
          Todo Add => 4
          Exit => q 
          """)
    return input("?:")

def run():
    while True:
        choice = menu()
        if choice == '1':
            login_page()
            
        elif choice == '2':
            register_page()
            
        elif choice == '3':
            logout_page()
            
        elif choice == '4':
            add_todo_page()
            
            
            
        elif choice == 'q':
            break
            
        else:
            print('Invalid choice')
            continue
            
            
            
            
if __name__ == '__main__':
    run()