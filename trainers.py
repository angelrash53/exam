class Trainer:
    import sqlite3 
    import pandas as pd 


    def __init__():
        connection = sqlite3.connect('computer-pride.db') 
        pass



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