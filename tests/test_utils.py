from src.utils import load_operations, format_date, x_card_number, x_bank_number


def test_formar_date():
    assert format_date("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert format_date("2018-03-23T10:45:06.972075") == "23.03.2018"
    assert format_date("2019-08-26T10:50:58") == "26.08.2019"
    assert format_date("2019-11-05") == "05.11.2019"


def test_x_card_number():
    assert x_card_number("Visa Gold 7756673469642839") == "Visa Gold 7756 67** **** 2839"
    assert x_card_number("Maestro 7810846596785568") == "Maestro 7810 84** **** 5568"
    assert x_card_number("МИР 1582474475547301") == "МИР 1582 47** **** 7301"


def test_x_bank_number():
    assert x_bank_number("Счет 12189246980267075758") == "Счет **5758"
    assert x_bank_number("Счет 95473010446151855633") == "Счет **5633"
    assert x_bank_number("Счет 15574304810835774010") == "Счет **4010"


def test_load_operations():
    from_file = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]
    assert load_operations("test_operations.json") == from_file
