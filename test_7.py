"""
Реализовать решение для генерации случайных данных в формат csv. 
На входе:
N - количество строк необходимое для генерации;
header - словарь ключом которого является название колонки, а значением один из типов: int, str или bool. 
Файл обязательно должен содержать заголовок.

Кол-во строк ограничено: 10**9.
Для генерации типа str длина текста не должна превышать > 100.
Для генерации типа int: диапазон значений от 0 до 100, целочисленные.
"""


from string import ascii_letters
import random as rn


def create_csv(count_rows: int, header: dict):
    records = []
    if count_rows > 10**9:
        count_rows = 10**9

    for _ in range(count_rows):
        current_row = []
        for value in header.values():
            if value == "int":
                element = str(rn.randint(0, 100))
            elif value == "str":
                element = str("".join(rn.choices(ascii_letters, k=rn.randint(1, 100))))
            elif value == "bool":
                element = str(rn.choice([True, False]))
            current_row.append(element)
        records.append(current_row)
    try:
        with open("file.csv", "w") as file:
            file.write(";".join(header.keys()) + "\n")

            for row in records:
                file.write(";".join(row) + "\n")
    except Exception:
        print("Проблемы с записью в файл")


N = 1000
header = {
    "column_int": "int",
    "column_str": "str",
    "column_bool": "bool",
    "column_int1": "int",
}

create_csv(N, header)
