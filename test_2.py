"""
Реализовать декоратор, который позволяет кешировать результат вызова функции и выводит время выполнения.
Для вывода времени выполнения необходимо использовать модуль logging.
Также декоратор должен принимать необязательный аргумент, который отвечает за то 
через сколько вызовов вызываемая функция будет заново исполнена и значение в кеше обновиться,
значение по умолчанию для данного аргумента 3.
"""

import logging
import time

logging.basicConfig(level=logging.INFO)


def cache_dec(restart=3):
    def decorator(func):
        cache = {}

        def wrapper(*args):
            start_time = time.time()
            args = tuple(*args)

            if not cache.get(args) or cache.get(args)[1] == restart:
                result = func(args)
                cache[args] = [result, 1]
            else:
                cache[args][1] += 1
                result = cache[args][0]

            end_time = time.time()
            logging.info(f"Execution time: {end_time - start_time}")

            return result

        return wrapper

    return decorator


@cache_dec(4)
def duplicate_nums(lst):
    """Принимает список, возвращает отсортированный список дубликатов"""
    duplicates = sorted(set([num for num in lst if lst.count(num) == 2]))

    return duplicates if duplicates else None


print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([i for i in range(10000)]))
print(duplicate_nums([i for i in range(10000)]))
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
