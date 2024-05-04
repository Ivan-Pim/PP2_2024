import psycopg2
from config import load_config

def delete_by_id(caller_id):

    rows_deleted = 0
    config = load_config()
    command = "DELETE FROM phonebook WHERE id = %s"
    #try:
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(command, (caller_id, ))
            rows_deleted = cur.rowcount
        
        conn.commit()
    #except (Exception, psycopg2.DatabaseError) as error:
    #    print(error)
    #finally:
    #    return rows_deleted



def delete_by_name(caller_name):

    rows_deleted = 0
    config = load_config()
    command = "DELETE FROM phonebook WHERE full_name = %s"
    #try:
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(command, (caller_name, ))
            rows_deleted = cur.rowcount
        
        conn.commit()
    #except (Exception, psycopg2.DatabaseError) as error:
    #    print(error)
    #finally:
    #    return rows_deleted

def delete_by_number(caller_number):

    config = load_config()
    command = "DELETE FROM phonebook WHERE number = %s"
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(command, (caller_number, ))
        
        conn.commit()

done = False
while not done:
    mode = input("By which parameter to delete? ")
    if mode == "id":
        id = input()
        delete_by_id(id)
    elif mode == "name":
        name = input()
        delete_by_name(name)
    elif mode == "number":
        num = input()
        delete_by_number(num)
    else:
        done = True