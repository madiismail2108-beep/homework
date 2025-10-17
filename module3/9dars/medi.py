from enum import Enum
from datetime import datetime

class Language(Enum):
    ENGLISH = 'en'
    RUSSIAN = 'ru'
    UZBEK   = 'uz'

class User:
    _id_user=1
    def __init__(self, username:str,
                 password : str,
                 user_id : int | None = None,
                 phone_number : str | None = None,
                 bio : str | None = None ,
                 created_at : datetime=datetime.now(),
                 language : Language | None = None,
                 is_premium : bool = False ):
         self.username = username
         self.password = password
         self.user_id = User._id_user
         self.phone_number = phone_number
         self.bio = bio
         self.created_at = created_at or str(datetime.now())
         self.language = language or Language.ENGLISH.value
         self.is_premium = is_premium
         self.contacts = []
         User._id_user += 1
    def __str__(self):
        return f'{self.user_id} - {self.username}'

class Message:
    def __init__(self,
                 sender_id : str,
                 receiver_id : str,
                 message : str | None = None,
                 messaged_at : datetime | None = None):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message = message
        self.messaged_at = messaged_at or str(datetime.now())
    
    def __str__(self):
        return f"{self.message}\n{self.messaged_at}"
    
class Chats:
    def __init__(self,
                 chat_id : str | None = None,
                 users : list[User] | None = None
                 ):
        self.chat_id = chat_id
        self.users = users 
        self.messages : list[Message] = []
        self.created_at = str(datetime.now())
        
        
    def __str__(self):
        return self.chat_id
