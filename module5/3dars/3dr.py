from dataclasses import dataclass
import psycopg2

#@dataclass 
#class FileManager:
#    def __init__(self, 
#                 file_path : str,  
#                 mode : str = 'r', 
#                 file : str | None = None):
#        self.f_p=file_path
#        self.m=mode
#        self.f=file

#    def __enter__(self):
#        self.f=open(self.f_p,self.m)
#        return self.f

db_info = {
     "database":"n70",
     "user":"postgres",
     "password":"123",
     "host":"localhost",
     "port":5432
}

@dataclass
class Person:
    first_name : str
    last_name : str
    age : int
    email :  str | None = None
  
    def save(self):
        with psycopg2.connect(**db_info) as conn:
            with conn.cursor() as cur:
                insert_data_query = '''
                    insert into person(first_name,last_name,age,email) 
                    values (%s,%s,%s,%s);
                '''
                cur.execute(insert_data_query,(self.first_name,self.last_name,self.age,self.email))
                conn.commit()
                print('INSERT 0 1')
    
    @staticmethod
    def load():
        with psycopg2.connect(**db_info) as conn:
            with conn.cursor() as cur:
                person_list_query = '''select * from person;'''
                cur.execute(person_list_query)
                person_data = cur.fetchall()
                for person in person_data:
                    print(person)



def my_decorator(func):
    def wrapper(*args,**kwargs):
        print('Funksiya ishlashidan oldin ....')
        func(*args,**kwargs)
        print('Funksiya ishlagandan keyin ....')
    
    return wrapper

@my_decorator
def say_hello():
    print('Hello')

say_hello()