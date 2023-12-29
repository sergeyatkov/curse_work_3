import pytest

from utils.functions import get_all_transaction_data
from utils.operation import Operation
import config


class TestOperationClass:

    @pytest.fixture
    def transactions(self):
        return filter(lambda t: len(t) != 0, get_all_transaction_data(config.OPERATIONS_PATH))

    def test_encrypts_details(self, transactions):
        for t in transactions:
            if len(t.get("from", "")) == 0:
                assert Operation.encrypts_details("") == ""
                continue

            assert Operation.encrypts_details(t.get("from", "")) != t.get("from", "")
            assert "*" in Operation.encrypts_details(t.get("from", ""))

    def test_formats_the_date(self, transactions):
        for t in transactions:
            # Проверяем с помощью обратной операции
            assert Operation.formats_the_date(t["date"]).isoformat() == t["date"]
