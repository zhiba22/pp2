import psycopg2
from config import load_config

def delete_by_any_column(column, value):
    config = load_config()
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM phone_book WHERE {column} = '{value}'")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == "__main__":
    delete_by_any_column("name", "Артем")

    # Пресс Ф Артем