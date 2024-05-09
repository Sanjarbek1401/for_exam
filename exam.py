#Baxodirov Sanjarbek
# Birinchi misol
import psycopg2
from colorama import Fore
host = 'localhost'
user = 'postgres'
password = '1425'
database = 'n42'
port = 5432

conn = psycopg2.connect(host = host,
                        user = user,
                        password = password,
                        database= database,
                        port = port)
curr = conn.cursor()

def print_response(message: str):
    print(Fore.GREEN + message + Fore.RESET)

create_table = '''
    CREATE TABLE if not exists test.product(
    id serial primary key,
    name varchar(30) not null,
    price integer not null,
    color varchar (30) not null,
    image TEXT); '''
curr.execute(create_table)
conn.commit()

#Ikkinchi misol
def insert_product():
    name = str(input("Enter product name:"))
    price = int(input("Enter product's price:"))
    color = str(input("Enter product's color:"))
    image = str(input("Enter product's image:"))
    insert_into_query = 'INSERT INTO test.product(name,price,color,image) values (%s,%s,%s,%s);'
    insert_into_params = (name,price,color,image)
    curr.execute(insert_into_query,insert_into_params)
    conn.commit()
    print_response( 'insert 0 1')
#insert_product()

def select_all_products():
    select_product = 'SELECT * FROM test.product;'
    curr.execute(select_product)
    rows = curr.fetchall()
    for row in rows:
        print_response(str(row))
#select_all_products()

def update_product():
    select_all_products()
    _id = int(input("Enter your product id:"))
    name = str(input("Enter your new product:"))
    price = int(input("Enter your product's price:"))
    color = str("Enter your product's color:")
    image = str("Enter your product's url :")
    update_query = 'update test.product set name = %s, price = %s,color =%S,image =%s where id = %s;'
    update_params = (_id,name,price,color,image)
    curr.execute(update_query,update_params)
    conn.commit()
    print_response('Succesfully updated')
#update_product()

def delete_product():
    select_all_products()
    _id = int(input('Enter product id:'))
    delete_query = 'delete from test.product where id = %s;'
    curr.execute(delete_query,(_id,))
    conn.commit()
    print_response('Succesfully deleted product')
#delete_product()  

# Uchinchi misol

class Alphabet:
    def __init__(self):
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUYWXZ'  

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.letters):
            letter = self.letters[self.index]
            self.index += 1
            return letter
        else:
            raise StopIteration

alphabet = Alphabet()

for letter in alphabet:
    print(letter) 

# to'rtinchi misol
import threading
import time 
def print_number():
    for  i in range (1,5):
        print(i)
        time.sleep(1)
        
#print_number()
def print_letters():
    for char in 'ABCDE':
        print(char)
        time.sleep(1)
       
print_number_threads =threading.Thread(target=print_number)
print_letters_threads = threading.Thread(target=print_letters)

print_number_threads.start()
print_letters_threads.start()

print_number_threads.join()
print_letters_threads.join()

# oltinchi misol
import psycopg2

database_db = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '1425',
    'database': 'n42',
    'port': 5432
}
class DbConnect:
    def __init__(self, database_db):
        self.database_db = database_db
        self.conn = None
        self.cur = None

    def __enter__(self):
        self.conn = psycopg2.connect(**self.database_db)
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
 # Beshinchi misol
import psycopg2

database_db = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '1425',
    'database': 'n42',
    'port': 5432
}

class DbConnect:
    def __init__(self, database_db):
        self.database_db = database_db
        self.conn = None
        self.cur = None

    def __enter__(self):
        self.conn = psycopg2.connect(**self.database_db)
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()



class Product:
    def __init__(self, id: int|None= None, name:str|None =None, price:int|None =None, color:str|None=None,image:str|None=None):
        self.id = id
        self.name = name
        self.price  = price
        self.color = color
        self.image = image
        
    def save(self):
        with DbConnect(database_db) as cursor:
            insert_query = 'INSERT INTO test.product(name, price, color, image) values (%s, %s,%S, %s);'
            insert_params = (self.name, self.price, self.color,self.image,)
            cursor.execute(insert_query, insert_params

        

        
        
