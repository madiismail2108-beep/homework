import datetime
try:
 from cddd  import users
except ImportError:
  raise Exception('Modul cddd yoki undagi users topilmadi!')




def get_user_by_username(username: str) -> str:
  for user in users:
    if user['username'] == username:
      return user
  return None

def loggin(username : str, password : str) ->str:
  try:
   username=input('username: ')
   password=input('password: ')

   user=get_user_by_username(username)
   if user is None:
    raise Exception( f'{username.title()} not found')
  
   if user ['loggin try count'] >= 3:
     raise Exception( 'you blocked due to too many attepts.')
  
   if user ['password']!= password:
     user ['loggin try count'] += 1
     raise Exception( 'password did not matched')
   user['is_active'] = True
   print( 'you successfully loggin') 
  except Exception as e:
   print(f"Error: {e}")

def register(username : str, password : str) -> str:
  try:
   username=input('username: ')
   password=input('password: ')
   if get_user_by_username(username)is not None:
    raise Exception('user is alredy here')
   new_user = {
    'username': username,
    'password': password,
    'is_active': False,
    'login_try_count': 0,
    'created_at': str(datetime.datetime.now())
   } 
   

   users.append(new_user)
   print(f'User {username} registered successfully')
  except Exception as e:
   print(f"Error: {e}")
  

def logout() -> None:
 try:
   username=input('username: ')
   user = get_user_by_username(username)
   if user is None:
      raise Exception(f'User{username} not found')
   
   users.remove(user) 
   print( 'user logout')
 except Exception as e:
   print(f'Error:{e}')
 
 
 
