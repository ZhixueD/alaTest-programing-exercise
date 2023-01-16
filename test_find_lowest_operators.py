import pytest

from find_lowest_operators import FindOperator

# give some test examples, test different phone numbers
test_phone_number = [
    ("467326767677", [("A", 1.0), ("B", 1.0)]),
    ("467006767677", [("C", 0.15)]),
    ("55732777998", "Not found in operators list"),
    ("12345899989", [("A", 0.9)]),
    ("265787097989", "Not found in operators list"),
    ("1268789996775", [("B", 1.2)]),
    ("176778999555", [("B", 0.92)]),
]


# run multiple tests
@pytest.mark.parametrize("phone, expected_output", test_phone_number)
def test_find_lowest_price(phone, expected_output):
    """
    pytest function to test if the class FindOperator is correct.
    Run 'pytest test_find_lowest_operators.py' in terminal to perform test.
    """
    prices: dict = {
        "A": {
            "1": 0.9,
            "268": 5.1,
            "46": 0.17,
            "4620": 0.0,
            "468": 0.15,
            "4631": 0.15,
            "4673": 0.9,
            "46732": 1.0,
            "1767": 2.0,
            "1268": 1.3,
        },
        "B": {"1": 0.92, "44": 0.5, "46": 0.2, "467": 1.0, "48": 1.2, "1268": 1.2},
        "C": {"1": 2, "44": 2, "46": 0.15, "48": 2, "1268": 2, '46732': 2},
    }

    solution = FindOperator(prices)
    assert solution.find_lowest_price(phone) == expected_output
