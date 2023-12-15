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

