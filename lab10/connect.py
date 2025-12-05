import psycopg2
from config import load_config

def connect(config):
    try:
        # Использование данных из конфигурации для подключения
        with psycopg2.connect(**config) as conn:
            conn.set_client_encoding('UTF8')
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    config = load_config()  # Загружаем конфигурацию
    connect(config)  # Подключаемся с использованием конфигурации
