"""
Реализовать скрипт, который позволяет валидировать csv файл на корректность его заполнения. 
Валидация должна включать в себя такие параметры, как:
•	Отсутствие/Присутствие заголовка: по умолчанию присутствует
•	Выбор разделителя: по умолчанию запятая
Скрипт должен поддерживать передачу параметров через командную строку с использованием библиотеки argparse. (Путь к файлу обяз., остальные необязательные). 
Должен поддерживать вызов --help для описания передаваемых параметров.
Вызов скрипта является корректным, если он завершается со статусом 0, в случае нахождении ошибки в файле, должна быть выведена проблема и завершён со статусом 1.
"""


import argparse


def validate_csv(file_path, delimiter=",", has_header=True):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

            if delimiter not in lines[0]:
                if has_header:
                    raise ValueError("Заголовок содержит неправильный разделитель")
                else:
                    raise ValueError("Файл содержит неправильный разделитель")
            column_count = len(lines[0].strip().split(delimiter))
            for indx in range(1, len(lines)):
                row = lines[indx].strip().split(delimiter)
                if len(row) != column_count:
                    raise ValueError(f"Строка {indx} содержит {len(row)} колонок вместо {column_count}")

    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return 1

    except ValueError as error:
        print(f"Ошибка: {error}")
        return 1

    print("Файл прошёл валидацию")
    return 0


parser = argparse.ArgumentParser(description="Валидация CSV файлов")
parser.add_argument("file_path", type=str, help="Путь к CSV файлу")
parser.add_argument("-d", "--delimiter", type=str, default=",", help="Разделитель в CSV файле")
parser.add_argument("-nh", "--no-header", default=True, dest="has_header", action="store_false", help="Валидация без заголовка")

args = parser.parse_args()

validate_csv(args.file_path, args.delimiter, args.has_header)