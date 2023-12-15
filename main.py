from config import OPERATIONS_PATH
from utils.functions import get_all_transaction_data, get_individual_transactions, sorts_transactions_by_date
from utils.operation import Operation


def main():
    all_transaction_data: list[dict] = get_all_transaction_data(OPERATIONS_PATH)
    individual_transactions: list[Operation] = get_individual_transactions(all_transaction_data)
    sorts_transactions: list[Operation] = sorts_transactions_by_date(individual_transactions)
    for transaction in sorts_transactions[:5]:
        print(transaction)
        print()


if __name__ == "__main__":
    main()
