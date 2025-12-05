from configparser import ConfigParser

def load_config(filename=r"C:/Users/zibek/Documents/Codes/pp2/lab10/database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)  # Читаем конфигурационный файл
    
    config = {}
    
    # Проверяем, что секция существует
    if parser.has_section(section):
        params = parser.items(section)  # Получаем все параметры из секции
        for param in params:
            config[param[0]] = param[1]  # Добавляем параметры в словарь config
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    
    return config

if __name__ == "__main__":
    config = load_config()  # Загружаем конфигурацию
    print(config)  # Печатаем конфиг (можно удалить, если не нужно)
