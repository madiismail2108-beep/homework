import datetime
from id  import users



def get_user_by_username(username):
  for user in users:
    if user['username'] == username:
      return user
  return None

def loggin():
  username=input('username: ')
  password=input('password: ')

  user=get_user_by_username(username)
  if user is None:
    return f'{username.title()} not found'
  
  if user ['loggin try count'] >= 3:
    return 'you blocked'
  
  if user ['password']!= password:
     user ['loggin try count'] += 1
     return 'password did not matched'
  user['is_active'] = True
  return 'you successfully loggin' 

def register():
  username=input('username: ')
  password=input('password: ')
  for user in users:
    if user['username'] == username:
      return 'user is alredy here'
    
    new_user={}
    new_user('username') == username
    new_user('password') ==  password
    new_user('is_active') == False
    new_user('login_try_count') == 0
    new_user('created_at') == str(datetime.now())
    

    users.append(new_user)
    return users
  

def logout():
 username=input('username: ')
 for user in users:
    if user['username'] == username:
      users.remove(user)
      return 'user logout'
 return f'user{username} not found'
 
 
 
