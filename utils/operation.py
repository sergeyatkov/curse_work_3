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

    @staticmethod
    def encrypts_details(details: str) -> str:
        """
        Метод класса приводит номера реквизитов для переводов
        в заданный зашифрованный формат
        :param details: строка с данными счета
        :return: зашифрованный номер счета
        """
        if details.startswith("Счет"):
            return f"{details[:5]}**{details[-4:]}"
        elif details == "":
            return details
        else:
            card_number = ""
            payment_system = ""
            for symbol in details:
                if symbol.isalpha():
                    payment_system = payment_system + symbol
                elif symbol == " ":
                    payment_system = payment_system + symbol
                else:
                    card_number = card_number + symbol
            return f"{payment_system}{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    @staticmethod
    def formats_the_date(date: str) -> datetime:
        """
        Метод класса переводит дату в нужный формат
        :param date: дата из файла в виде строки
        :return: дата в формате исо
        """
        return datetime.fromisoformat(date)

    def __str__(self):
        return (f"{datetime.strftime(self.date, '%d.%m.%Y')} {self.description}\n"
                f"{self.from_} -> {self.to}\n"
                f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}")
