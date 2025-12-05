import json
from psycopg2 import DatabaseError
from update import insert, update, select
from config import load_config

def main():
    config = load_config()

    with open("contacts.json", "r") as data:
        contacts = json.load(data)
    for contact in contacts:
        try:
            if select(contact["name"], contact["second_name"], contact["last_name"], config) == None:
                print(f"New data about {contact["name"]}")
                insert(contact["name"], contact["second_name"], contact["last_name"], contact["phone_number"], config)
            else:
                print(f"A person with these data \n{contact} \nalready exists \n")
                update(contact["name"], contact["second_name"], contact["last_name"], contact["phone_number"], config)
        except (DatabaseError, Exception) as error:
            print(error)

if __name__ == "__main__":
    main()