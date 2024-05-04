import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    command = """
        CREATE TABLE WHERE NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(255) NOT NULL unique,
            number VARCHAR(20) NOT NULL
        )
        """
    
    extra = """
        ALTER TABLE phonebook
        ADD CONSTRAINT correct_number
        CHECK (
            number ~ '\\+[0-9]{1,14}'
        );
        """

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(extra)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()