import psycopg2

config = {'database' : 'snake_base', 'user' : 'postgres', 'host' : 'localhost', 'password' : 'Illu143m1serable$', "port" : 5432}
dsn = "postgresql://postgres:Illu143m1serable$@localhost:5432/snake_base"

def create_table():
    command1 = """
            CREATE TABLE IF NOT EXISTS "user" (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL unique,
                level INTEGER,
                exp INTEGER
            )
            """
    command2 = """
            CREATE TABLE IF NOT EXISTS user_score (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL unique,
                score INTEGER
            )
            """

    with psycopg2.connect(dsn) as conn:
        with conn.cursor() as cur:
            cur.execute(command1)
            cur.execute(command2)

def insert_user(username, level, exp, score):
    command1 = """ 
                INSERT INTO "user"(username, level, exp) VALUES(%s, %s, %s)
                ON CONFLICT DO NOTHING
            """
    command2 = """
                INSERT INTO user_score(username, score) VALUES(%s, %s)
                ON CONFLICT DO NOTHING   
            """

    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(command1, (username, level, exp))
            cur.execute(command2, (username, score))

            conn.commit()

def query_data(username):
    command1 = """SELECT level, exp FROM "user" WHERE username = %s"""
    command2 = "SELECT score FROM user_score WHERE username = %s"

    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(command1, (username, ))
            personal = cur.fetchone()

            cur.execute(command2, (username, ))
            multi = cur.fetchone()

            return personal, multi
        
def update(username, level, exp, score):
    command1 = """UPDATE "user"
                SET level = %s, exp = %s 
                WHERE username = %s 
            """
    command2 = """UPDATE user_score
                SET score = %s
                WHERE username = %s
            """
    
    with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command1, (level, exp, username))
                cur.execute(command2, (score, username))

                conn.commit()    