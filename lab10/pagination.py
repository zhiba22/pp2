import psycopg2
from config import load_config
import keyboard

def query_pagination():
    config = load_config()
    limit = 2
    pointer = 0
    running = True
    try:
        while running:
            key_pressed = keyboard.read_event(suppress=True)  # Ждем, пока не будет нажата клавиша
            if key_pressed.event_type == keyboard.KEY_DOWN:
                if key_pressed.name == "left":
                    pointer -= 2
                    if pointer < 0:
                        pointer = 0
                elif key_pressed.name == "right":
                    pointer += 2
                elif key_pressed.name == 'esc':
                    print('Exiting...')
                    break
                
                with psycopg2.connect(**config) as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(f"SELECT * FROM phone_book ORDER BY person_id LIMIT {limit} OFFSET {pointer}")
                        print(cursor.fetchall())
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)



if __name__ == "__main__":
    query_pagination()
                        
                        


