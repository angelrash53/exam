import sqlite3 
import pandas as pd 

connection = connection = sqlite3.connect('company.db') 

def __init__():
    pass

def getCustomers():
    tables = pd.read_sql("SELECT * FROM customers", connection) 

def getCustomerById(id):
    tables = pd.read_sql("SELECT * FROM customers WHERE CustomerId ="+str(id), connection) 
    print(tables)


def createTables():
    c = connection.cursor() 
    c.execute( 
        '''
            CREATE TABLE IF NOT EXIST trainers(
                id integer PRIMARY KEY,
                name text,
                gender text
            )
        '''
    )

    tables = pd.read_sql("select * FROM sqlite_master where type='tables';", connection) 
    print(tables)

def create(trainers):
    sql = '''
        INSERT INTO trainers(id, name, gender) VALUES(?,?,?)
    '''
        
    cur = connection.cursor() 
    cur.execute(sql, trainers) 
    connection.commit()

    results = pd.read_sql("SELECT * FROM trainers", connection)
    print(results) 

def retrieveAll(): 
    pass

def retrieveById(id): 
    cur = connection.cursor() 
    cur.execute("SELECT id FROM trainers WHERE id="+str(id)) 

    results = cur.fetchall() 

    for x in results:
        print(x)

            
def update(id, data):
    sql = 'UPDATE trainers SET name = ?, gender = ? where id = '+str(id)
    cur = connection.cursor() 
    cur.execute(sql, data) 
    connection.commit()

    results = pd.read_sql("SELECT * FROM trainers", connection) 
    print(results)

def delete(id): 
    sql = 'DELETE FROM trainers where id = '+str(id)
    cur = connection.cursor()
    cur.execute(sql) 
    connection.commit()

    results = pd.read_sql("SELECT * FROM trainers", connection) 
    print(results)


retrieveAll(3)