import json

from utils.operation import Operation


def get_all_transaction_data(path) -> list[dict]:
    """
    Функция берет данные из файла json
    :param path: путь к файлу
    :return: возвращает данные из файла
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_individual_transactions(transactions: list[dict]) -> list[dict]:
    """
    Функция приводит данные по операциям к нужному виду
    :param transactions: все данные по операциям
    :return: список с неодходимыми данными по каждой операции
    """
    correct_transactions = []
    for transaction in transactions:
        existing_transaction = Operation(
            tn=transaction["id"],
            date=transaction["date"],
            state=transaction["state"],
            operation_amount=transaction["operationAmount"],
            description=transaction["description"],
            from_=transaction["from"],
            to=transaction["to"]
        )
        correct_transactions.append(existing_transaction)
    return correct_transactions
