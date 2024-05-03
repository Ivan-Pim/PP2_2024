import psycopg2
from config import load_config
import csv

def insert_caller(caller_name, number):
    """ Insert a new caller into the vendors table """

    sql = """INSERT INTO phonebook(full_name, number)
             VALUES(%s, %s) RETURNING id;"""
    
    id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (caller_name, number))

                # get the generated id back              
                rows = cur.fetchone()
                if rows:
                    id = rows[0]
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return id



def insert_many_callers(caller_list):
    """ Insert multiple callers into the caller table  """

    sql = "INSERT INTO phonebook(full_name, number) VALUES(%s, %s) RETURNING *"
    config = load_config()
    rows = []

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.executemany(sql, caller_list)

                # obtain the inserted rows
                ## error here, and its unneccessary, so ignore this code
                #rows = cur.fetchall()

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    #finally:
    #    return rows

def csv_insert(fullpath):
    config = load_config()
    with  psycopg2.connect(**config) as conn:
        with  conn.cursor() as cur:
            sql = f'''COPY phonebook(full_name,number) 
            FROM '{fullpath}' 
            DELIMITER ',' 
            CSV HEADER;
            '''
            cur.execute(sql) 
            conn.commit()


# initial test insert
# preferable to comment after the first time
"""
if __name__ == '__main__':
    insert_caller("Test Dummyson", "+77777777777")

    insert_many_callers([
        ('Man Numberoner', "+11111111111"),
        ('Woman Numberoner', "+21212121212"),
        ('Child Numberoner', "+81818181818"),
    ])
"""

mode = input("Choose mode: ")
if mode == "csv":
    filename = input()
    csv_insert(filename)
elif mode == "by hand":
    name = input().replace(", ", ",")
    name = name.replace(" ,", ",")
    name = name.split(',')
    while name != ["0", "0"]:
        insert_caller(name[0], name[1])
        name = input().split(',')