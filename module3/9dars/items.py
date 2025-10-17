import json

def save(data,file_path = None):
    with open(file_path,'w') as f:
        json.dump(data,f,indent=4)

def load(file_path):
    with open(file_path) as f:
        return json.load(f)
    
def generate_user_id(users : dict[str,dict]):
    max_id = max(user["user_id"] for user in users.values())
    return max_id + 1

def generate_chat_id(chats : dict[str,dict]):
    max_id = max(chat["chat_id"] for chat in chats.values())
    return max_id + 1