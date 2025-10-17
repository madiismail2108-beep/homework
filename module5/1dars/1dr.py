import psycopg2 
from decimal import Decimal, getcontext

'''
class PERSON:
    def __init__(self, name, age):
        self.n=name
        self.a=age
    
    def connect():
        return psycopg2.connect(
            dbname="n70",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
    
    def save(self):
        con=self.connect()
        curs=con.cursor()
        curs.execute("INSERT INTO persons(name, age) VALUES(%S, %S)", (self.n, self.a))
        con.commit()
        curs.close()
        con.close()
        print('Persun is added')

    
    def get_all_person():
        con = PERSON.connect()
        curs = con.cursor()
        curs.execute("SELECT * FROM person")
        rows = curs.fetchall()
        curs.close()
        con.close()
        return rows
    
    def get_person(person_id):
        con = PERSON.connect()
        curs = con.cursor()
        curs.execute("SELECT * FROM person WHERE id = %s", (person_id,))
        person = curs.fetchone()
        curs.close()
        con.close()
        return person
'''  

usd = Decimal(input(" USD amount: "))
euro = Decimal(input("1 USD in EURO: "))

euro_a=usd*euro
print(f"{usd} USD = {euro_a} EUR")
