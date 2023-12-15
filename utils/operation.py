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
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = from_
        self.to = to

    def encrypts_details(self, details: str) -> str:
        """
        Функция приводит номера реквизитов для переводов
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
