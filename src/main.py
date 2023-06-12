from utils import load_operations, format_date, x_card_number, x_bank_number


file = "../operations.json"


def main():
    operations = load_operations(file)
    for operation in operations:
        operation['date'] = format_date(operation['date'])

        try:
            if "Счет" in operation['from']:
                operation['from'] = x_bank_number(operation['from'])
            else:
                operation['from'] = x_card_number(operation['from'])
        except LookupError:
            operation['from'] = "Непонятный формат"

        if "Счет" in operation['to']:
            operation['to'] = x_bank_number(operation['to'])
        else:
            operation['to'] = x_card_number(operation['to'])

        print(f"""
{operation['date']} {operation['description']}
{operation['from']} -> {operation['to']}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}""")


if __name__ == '__main__':
    main()
