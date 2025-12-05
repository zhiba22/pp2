import psycopg2
from config import load_config

def insert(user_name, second_name, last_name, phone_number, config):
    sql = """
        INSERT INTO phone_book(name, second_name, last_name, phone_number)
        VALUES (%s, %s, %s, %s)
        RETURNING person_id
    """

    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, (user_name, second_name, last_name, phone_number))
                row = cursor.fetchone()
                if row:
                    return row[0]
                return None
    except Exception as error:
        print("Insert error:", error)
        return None


def select(name, second_name, last_name, config):
    sql = """
        SELECT * FROM phone_book
        WHERE name = %s AND second_name = %s AND last_name = %s
    """

    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, (name, second_name, last_name))
                return cursor.fetchone()
    except Exception as error:
        print("Select error:", error)
        return None


def update(user_name, second_name, last_name, phone_number, config):
    sql = """
        UPDATE phone_book
        SET phone_number = %s
        WHERE name = %s AND second_name = %s AND last_name = %s
    """

    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, (phone_number, user_name, second_name, last_name))
    except Exception as error:
        print("Update error:", error)


def main():
    config = load_config()

    user_name = input("Enter name: ")
    second_name = input("Enter second name: ")
    last_name = input("Enter lastname: ")
    phone_number = input("Enter phone number: ")

    if select(user_name, second_name, last_name, config) is None:
        insert(user_name, second_name, last_name, phone_number, config)
        print("Inserted.")
    else:
        print("These data already exist. Let's update.")
        update(user_name, second_name, last_name, phone_number, config)


if __name__ == "__main__":
    main()
