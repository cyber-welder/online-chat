"""
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
 Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
 (использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
"""

from task_2 import host_range_ping
from tabulate import tabulate


def magic_action_for_data(data: tuple):
    """
    Функция заполняет недостающие данные пустыми строками
    """
    result = []
    rows = len(data[0]) if len(data[0]) > len(data[1]) else len(data[1])
    for i in range(rows):
        try:
            left_col = data[0][i]
        except IndexError:
            left_col = ''
        try:
            right_col = data[1][i]
        except IndexError:
            right_col = ''
        result.append((left_col, right_col))
    return result


def host_range_ping_tab(ip_range):
    reachable_list = []
    unreachable_list = []

    ping_result = host_range_ping(ip_range)

    for k, v in ping_result.items():
        if v == "Узел недоступен":
            unreachable_list.append(k)
        else:
            reachable_list.append(k)
    return reachable_list, unreachable_list


if __name__ == "__main__":
    ping_result = host_range_ping_tab("8.8.8.8-9")
    COLUMNS = ['Reachable', 'Unreachable']
    ROWS = magic_action_for_data(ping_result)
    print(tabulate(ROWS, headers=COLUMNS, tablefmt="grid"))
