import psycopg2
import os
from dotenv import load_dotenv
from utils import hash_password
from models import UserRole

load_dotenv() 

db_info = {
    "database":os.getenv("n70"),
    "user":os.getenv("postgres"),
    "host":os.getenv("localhost"),
    "password":os.getenv("1234"),
    "port":os.getenv("5432")
}

conn = psycopg2.connect(**db_info)
cur = conn.cursor()

def commit(func):
    def wrapper(*args,**kwrags):
        result = func(*args,**kwrags)
        conn.commit()
        return result
    return wrapper

def create_user_table():
    user_query = """create table users(
            id serial primary key,
            username varchar(255) not null unique,
            password varchar(255) not null,
            role varchar(15) default 'user',
            email varchar(255) ,
            created_at timestamptz default now()     
    );    
    """
    cur.execute(user_query)

def create_todo_table():
    todo_query = """create table todos(
            id serial primary key,
            title varchar(255) not null,
            description text,
            todo_type varchar(20) default 'personal',
            user_id int references users(id),
            created_at timestamptz default now()    
        );    
    """
    cur.execute(todo_query)
    
@commit
def init():
    create_user_table()
    create_todo_table()

@commit
def insert_admin():
    insert_admin_query = '''insert into users(username,password,role)
    values(%s,%s,%s);
    '''
    data = ('admin',hash_password('admin123'),UserRole.ADMIN.value)
    cur.execute(insert_admin_query,data)