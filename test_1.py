"""
Напишите функцию, которая будет принимать список nums, содержащий числа в диапазоне от 1 до 100,
и возвращать отсортированный список чисел, которые в списке nums встречались дважды.
 
Примеры:
 
duplicate_nums([1, 2, 3, 4, 3, 5, 6]) ➞ [3]
 
duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]) ➞ [72, 81, 99]
 
duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ None
 
Примечания:
— никакое число не будет встречаться в nums трижды и более раз,
— если никакое число в nums не встречалось дважды, функция должна вернуть None.
"""


def duplicate_nums(lst_nums):
    """Принимает список, возвращает отсортированный список дубликатов"""
    duplicates = sorted(
        list(set([num for num in lst_nums if lst_nums.count(num) == 2]))
    )

    return duplicates if duplicates else None


print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
