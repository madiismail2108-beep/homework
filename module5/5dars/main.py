from servise import login, register, logout

while True:
    print('Choose one:\n Log in --> 1,\n Register --> 2,\n log out --> 3,\n Exit--> q.')
    choice = input('choice : ')
    if choice == '1':
        username = input('username : ')
        password = input('password : ')
        
        result = login(username,password)
        
        print(result)

    elif choice =="2":
        username = input('your username: ')
        password = input('yourpassword: ')
        full_name = input('your full name: ')
        result = register(username, password, full_name)
        print(result)

    elif choice =="3":
        result = logout()
        print(result)

    elif choice == 'q':
        break
    else:
        print('Invalid choice, try again please')

