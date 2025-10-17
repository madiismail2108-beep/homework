from items import load,save,generate_user_id,generate_chat_id
from medi import User,Chats,Message

current_user = None

def register(username,password):
    users = load('db/users.json')
    for user in users.values():
        if user['username'] == username:
            return 'User already exsits'
        
    user = User(username,password)
    user.user_id = generate_user_id(users)
    users[user.username] = user.__dict__
    save(users,'db/users.json')
    return 'User successfully created'

def login(username,password):
    users = load('db/users.json')
    global current_user

    for user in users.values():
        if user['username'] == username and user['password'] == password:
            current_user = user
            return f'User ({user['username']}) successfully logged in'
    
    print('User not found')
    return None

def add_contact(other_username):
    users = load('db/users.json')
    
    global current_user
    
    if not current_user:
        print('You must be login')
        return
    
    if other_username not in users:
        print(f'This {other_username} not exists in your APP')
        return 
    
    if other_username in current_user["contacts"]:
        return f'This {other_username} already exists'
    
    current_user["contacts"].append(other_username)
    users[current_user['username']] = current_user
    save(users,'db/users.json')
    return 'Successfulyy added contact'

def create_chat(other_username):
    users = load('db/users.json')
    chats = load('db/chats.json')
    global current_user
    
    if not current_user:
        print('You must be login')
        return
    
    if other_username not in users:
        print(f'This {other_username} not exists in your APP')
        return 
    
    chat_id = f"{current_user['username']}_{other_username}"
    
    if chat_id in chats:
        return f"This {chat_id} already exists"
    
    connect_user = [current_user["username"],other_username]
    
    chat = Chats(chat_id=chat_id,users=connect_user)
    chats[chat_id] = chat.__dict__
    save(chats,'db/chats.json')
    return f'Chat succesfully created with {other_username}'
    
def send_message(other_username):
    users = load('db/users.json')
    chats = load('db/chats.json')

    global current_user
    
    if not current_user:
        print('You must be login')
        return
    
    if other_username not in users:
        print(f'This {other_username} not exists in your APP')
        return 
    
    chat_id = f"{current_user['username']}_{other_username}"
   
    if chat_id not in chats:
        return "Chat not found"
    
    body = input(f"Message to {other_username} : ")
    message = Message(
        sender_id = current_user['username'],
        receiver_id = other_username,
        message = body
    )
    chats[chat_id]["messages"].append(message.__dict__)
    
    save(chats,'db/chats.json')
    return "Sent message"
    
def read_chat(other_username):
    users = load('db/users.json')
    chats = load('db/chats.json')
    
    global current_user
    
    if not current_user:
        print('You must be login')
        return
    
    
    if other_username not in users:
        print(f'This {other_username} not exists in your APP')
        return 
    
    chat_id = f"{current_user['username']}_{other_username}"
    
    if chat_id not in chats:
        return "Chat not found"
    
    chat = chats[chat_id]
    
    for message in chat["messages"]:
        print(message)

while True:
    choice = input('enter your choice : ')
    if choice == '1':
        username = input('username : ')
        password = input('password : ')
        response = register(username,password)
        print(response)
    
    elif choice == '2':
        username = input('username : ')
        password = input('password : ')
        response = login(username,password)
        print(response)
        
    elif choice == '3':
        other_username = input('add new user for your contact : ')
        response = add_contact(other_username)
        print(response)
        
    elif choice == '4':
        other_username = input('other username : ')
        response = create_chat(other_username)
        print(response)
    
    elif choice == '5':
        other_username = input('other username : ')
        response = send_message(other_username)
        print(response)
        
    elif choice == "6":
        other_username = input('other username : ')
        response = read_chat(other_username)
        print(response)
        
    elif choice == 'q':
        break