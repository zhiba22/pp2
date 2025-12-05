import psycopg2
from config import load_config

def create_table():
    config = load_config() # read the connection parameters using the load_config() function of the config module:
    command = """CREATE TABLE phone_book(
                    person_id SERIAL PRIMARY KEY NOT NULL,
                    name VARCHAR(30) NOT NULL,
                    second_name VARCHAR(30) NOT NULL,
                    last_name VARCHAR(30) NOT NULL,
                    phone_number VARCHAR(30)
                )"""
    try:
        with psycopg2.connect(**config) as conn: # The connect() function returns a connection object
            with conn.cursor() as cursor: # The with statement will close the database connection automatically.
                cursor.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    create_table()