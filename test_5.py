"""
Реализуйте цепную функцию суммирования.

Примеры: 
chain_sum(5)() ➞ 5
chain_sum(5)(2)() ➞ 7
chain_sum(5)(100)(-10)() ➞ 95
"""


def chain_sum(num):
    def inner(sub_num=None):
        if sub_num is None:
            return num
        else:
            return chain_sum(num + sub_num)

    return inner


print(chain_sum(5)())
print(chain_sum(5)(2)())
print(chain_sum(5)(100)(-10)())
