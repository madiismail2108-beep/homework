from utils import Response, match_password, hash_password
from db import cur, commit
from models import User
from session import Session

session = Session()

def login(username : str, password : str):
    user = session.check_session()
    if user:
        return Response('You already logged in' , 404)
    
    get_user_by_username = '''select * from users where username = %s;'''
    cur.execute(get_user_by_username,(username,))
    
    user_data = cur.fetchone()
    if not user_data:
        return Response('User not found',404)
    
    
    user = User.from_tuple(user_data)
    
    
    if not match_password(password,user.password):
        return Response('Password wrong',404)
    
    session.add_session(user)
    return Response('You successfully logged in.')
    
def register(username: str, password:str, full_name:str):
    check_user_query = '''SELECT * FROM users WHERE username = %s;'''
    cur.execute(check_user_query, (username,))
    if cur.fetchone():
        return Response('Username already exists', 400)

    hashed_password = hash_password(password)

    insert_user_query = '''
        INSERT INTO users (username, password, fullname)
        VALUES (%s, %s, %s)
        RETURNING *;
    '''
    cur.execute(insert_user_query, (username, hashed_password, full_name))
    new_user_data = cur.fetchone()
    commit()

    new_user = User.from_tuple(new_user_data)
    session.add_session(new_user)

    return Response('User registered sucssesfully')

def logout():
    user = session.check_session()
    if not user:
        return Response('You are not logged in', 404)
    
    session.clear_session()
    return Response('You successfully logged out.')

