import json


def x_card_number(card_number):
    """
    Маскирует номер карты под звездочки
    """
    old_card = card_number.split(' ')
    new_card = old_card[-1][:4] + ' ' + old_card[-1][4:6] + '**' + ' ' + '****' + ' ' + old_card[-1][-4:]
    old_card[-1] = new_card
    return " ".join(old_card)


def x_bank_number(bank_number):
    """
    Маскирует номер счёта под звёздочки
    """
    old_number = bank_number.split(" ")
    new_number = '**' + old_number[-1][-4:]
    old_number[-1] = new_number
    return " ".join(old_number)


def load_operations(file):
    """
    Загружает и сортирует данные из джейсона
    """
    with open(file, 'r', encoding='utf-8') as file:
        loaded = json.load(file)
        info_list = []
        for operation in loaded:
            try:
                if operation['state'] == 'EXECUTED':
                    info_list.append(operation)
            except LookupError:
                error = "Операция не выполнена"
        sorted_operations = sorted(info_list, key=lambda x: x["date"], reverse=True)
        last_operations = sorted_operations[:5]

        return last_operations


def format_date(data):
    """
    Конвертирует формат даты
    """
    formated_date = data[8:10] + '.' + data[5:7] + '.' + data[:4]
    return formated_date
