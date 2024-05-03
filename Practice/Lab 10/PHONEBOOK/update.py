import psycopg2
from config import load_config


def update_caller_name(caller_id, caller_name):
    """ Update caller name based on the caller id """
    
    updated_row_count = 0

    sql = """ UPDATE phonebook
                SET full_name = %s
                WHERE id = %s"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (caller_name, caller_id))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count
    
def update_caller_number(caller_id, caller_number):
    """ Update caller number based on the caller id """
    
    updated_row_count = 0

    sql = """ UPDATE phonebook
                SET number = %s
                WHERE id = %s"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (caller_number, caller_id))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count
    
def update_caller_full(caller_id, caller_name, caller_number):
    """ Update caller based on the caller id """
    
    updated_row_count = 0

    sql = """ UPDATE phonebook
                SET full_name = %s,
                number = %s
                WHERE id = %s"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (caller_name, caller_number, caller_id))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

typ = input()
data = input().split(',')
done = False
while not done:
    if typ == "name":
        update_caller_name(data[0], data[1])
    elif typ == "number":
        update_caller_number(data[0], data[1])
    elif typ == "full":
        update_caller_full(data[0], data[1], data[2])
    
    typ = input()
    data = input().split(',')
    if data == ["0", "0", "0"] or typ == "0":
        done = True