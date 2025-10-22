from session import Session
from utils import Response, match_password,validate_user, hash_password,login_required,is_admin
from db import cur, commit
from models import User, UserRole
from serializers import UserRegister

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

@commit
def register(username : str | None = None, password : str | None = None,email : str | None = None):
    dto = UserRegister(username,password)
    validate_user(dto)
    get_user_by_username = '''select * from users where username = %s;'''
    cur.execute(get_user_by_username,(username,))
    user_data = cur.fetchone()
    if user_data:
        return Response(message='User already exists',status_code=404)
    
    insert_user_query = '''insert into users(username,password,email,role)
        values (%s,%s,%s,%s);
    '''
    
    data = (dto.username,hash_password(dto.password),email, UserRole.USER.value)
    cur.execute(insert_user_query,data)
    return Response('User created',201)

    
def logout():
    if session.session:
        session.session = None
        return Response('You logged out !',204)
    
    return Response('You must be login.',404)

@commit
@login_required
@is_admin
def add_todo(title: str, description: str):
    insert_todo_query='''insert into todos 
    (title, description) values(%s, %s);'''
    user = session.check_session()
    data = (title, description, user.id)
    cur.execute(insert_todo_query, data)
    return Response('Todo successfully added', 201)
    