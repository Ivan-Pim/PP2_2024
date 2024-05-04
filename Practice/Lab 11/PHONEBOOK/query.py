import psycopg2
from config import load_config

def get_callers_simple():
    """ Retrieve data from the phonebook table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, full_name, number FROM phonebook ORDER BY full_name")
                print("Number of matches: ", cur.rowcount)
                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



def get_callers(orderby, given_name, given_number):
    """ Retrieve data from the vendors table """
    orders = ["id", "full_name", "number"]
    config  = load_config()
    command, part2, part3, part4 = "SELECT id, full_name, number FROM phonebook ", "", "", ""
    if given_name != 0:
        part2 = f"(phonebook.full_name LIKE '%{given_name}%') "
    if given_number != 0:
        part3 = f"(phonebook.number LIKE '%{given_number}%') "
    if orderby != 0:
        part4 = f"ORDER BY {orderby}"
    if part2 != "" or part3 != "":
        command += "WHERE " + part2
        if part2 != "" and part3 != "":
            command += "OR "
        command += part3
    command += part4

    #print(command)

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                rows = cur.fetchall()

                print("Number of matches: ", cur.rowcount)
                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def pagination_get(orderby, given_name, given_number, lim):
    orders = ["id", "full_name", "number"]
    config  = load_config()

    auxcommand = "SELECT count(*) from phonebook"

    command, part2, part3, part4 = "SELECT id, full_name, number FROM phonebook ", "", "", ""
    if given_name != 0:
        part2 = f"(phonebook.full_name LIKE '%{given_name}%') "
    if given_number != 0:
        part3 = f"(phonebook.number LIKE '%{given_number}%') "
    if orderby != 0:
        part4 = f"ORDER BY {orderby} "
    if part2 != "" or part3 != "":
        command += "WHERE " + part2
        if part2 != "" and part3 != "":
            command += "OR "
        command += part3
    command += part4

    command += "LIMIT %s OFFSET %s"
    off = 0
    #print(command)

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(auxcommand)
                full = cur.fetchone()[0]
                
                while off < full:
                    cur.execute(command, (lim, off))
                    off += lim
                    rows = cur.fetchall()
                    if rows == None:
                        break

                    print("Number of matches: ", cur.rowcount)
                    for row in rows:
                        print(row)
                    if input("Next Page? ") == "no":
                        break
                
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

options = ["sort by", "name", "number", "pages"]
done = False
while not done:
    settings = input("Specify settings? ")
    ordering, name_filter, number_filter = 0, 0, 0
    paged = False
    while settings in options:
        if settings == "sort by":
            ordering = input()
        if settings == "name":
            name_filter = input()
        if settings == "number":
            number_filter = input()
        if settings == "pages":
            lim = int(input("Limit: "))
            paged = True
        settings = input("Specify settings? ")
    if paged:
        pagination_get(ordering, name_filter, number_filter, lim)
    else:
        get_callers(ordering, name_filter, number_filter)
    if input("Go on?" ) != "Y":
        done = True