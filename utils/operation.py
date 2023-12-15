from datetime import datetime


class Operation:
    """
    Класс для обработки данных по операциям
    """

    def __init__(self,
                 tn: int,
                 date: str,
                 state: str,
                 operation_amount: dict,
                 description: str,
                 from_: str,
                 to: str
                 ):
        self.tn = tn
        self.date = self.formats_the_date(date)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = self.encrypts_details(from_)
        self.to = self.encrypts_details(to)

    def encrypts_details(self, details: str) -> str:
        """
        Метод класса приводит номера реквизитов для переводов
        в заданный зашифрованный формат
        :param details: строка с данными счета
        :return: зашифрованный номер счета
        """
        prop_number_list = []
        for symbol in details:
            if symbol.isdigit():
                prop_number_list.append(symbol)
        prop_number_str = "".join(prop_number_list)
        if len(prop_number_str) > 16:
            return f"****************{prop_number_str[16:]}"
        elif len(prop_number_str) == 16:
            return f"{prop_number_str[0: 4]} {prop_number_str[4: 6]}** **** {prop_number_str[12:]}"
        else:
            return prop_number_str

    def formats_the_date(self, date: str) -> datetime:
        """
        Метод класса переводит дату в нужный формат
        :param date: дата из файла в виде строки
        :return: дата в формате исо
        """
        return datetime.fromisoformat(date)

    def __str__(self):
        return (f"{datetime.strftime(self.date, '%d%m%Y')} Перевод организации\n"
                f"{self.from_} -> {self.to}\n"
                f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}.")
