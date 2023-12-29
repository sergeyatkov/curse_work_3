import pytest
from utils.functions import get_all_transaction_data, get_individual_transactions, sorts_transactions_by_date
import config


class TestFunctionsClass:
    @pytest.fixture
    def transactions(self):
        return filter(lambda t: len(t) != 0, get_all_transaction_data(config.OPERATIONS_PATH))

    @pytest.fixture
    def empty_transactions(self):
        return list()

    @pytest.fixture
    def invalid_transactions(self):
        return list({"stata": "EXECUTED"})

    @pytest.fixture
    def transactions_dict(self, transactions):
        out = dict()
        for t in transactions:
            out[t["id"]] = t
        return out

    def test_correct_txs(self, transactions, transactions_dict):
        operations = get_individual_transactions(transactions)

        # Проверяем что все транзакции в треубемом состоянии
        assert all(map(lambda i: i.state == "EXECUTED", operations))

        for o in operations:
            t = transactions_dict[o.tn]

            # Проверяем правильно ли мапятся поля (но только те которые не маскируются)
            assert t["id"] == o.tn
            assert t["state"] == o.state
            assert t["operationAmount"] == o.operation_amount
            assert t["description"] == o.description

    # Проверяем работу с пустыми листами
    def test_empty_txs(self, empty_transactions):
        operations = get_individual_transactions(empty_transactions)
        assert len(operations) == 0

    # Проверяем работу с невалидными данными (негативный тест)
    def test_invalid_txs(self, invalid_transactions):
        with pytest.raises(Exception) as exc_info:
            get_individual_transactions(invalid_transactions)

        assert type(exc_info.value) is TypeError

    def sorting_tests(self, transactions):
        operations = get_individual_transactions(transactions)
        sorted_operations = sorts_transactions_by_date(operations)
        assert all(sorted_operations[i] <= sorted_operations[i + 1] for i in range(len(sorted_operations) - 1))
