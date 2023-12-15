import json


def get_all_transaction_data(path):
    """
    Функция берет данные из файла json
    :param path: путь к файлу
    :return: возвращает данные из файла
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)
