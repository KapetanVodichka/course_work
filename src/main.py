from utils import load_operations, format_date, X_card_number, X_bank_number


FILE = "operations.json"


def main():
    operations = load_operations(FILE)
    for operation in operations:
        operation['date'] = format_date(operation['date'])

        try:
            if "Счет" in operation['from']:
                operation['from'] = X_bank_number(operation['from'])
            else:
                operation['from'] = X_card_number(operation['from'])
        except LookupError:
            operation['from'] = "Непонятный формат"

        if "Счет" in operation['to']:
            operation['to'] = X_bank_number(operation['to'])
        else:
            operation['to'] = X_card_number(operation['to'])

        print(f"""
{operation['date']} {operation['description']}
{operation['from']} -> {operation['to']}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}""")

        # print(operation['date'] + ' ' + operation['description'])
        # print(operation['from'] + ' -> ' + operation['to'])
        # print(operation['operationAmount']['amount'] + ' ' + operation['operationAmount']['currency']['name'], end="\n \n")


if __name__ == '__main__':
    main()