"""
На вход подаётся массив слов зависимых от регистра, для которых необходимо произвести фильтрацию на основании дублей слов,
если в списке найден дубль по регистру, то все подобные слова вне зависимости от регистра исключаются.
На выходе должны получить уникальный список слов в нижнем регистре.

words = ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']

find_in_different_registers(words) -> ['папа', 'брат']
"""


def find_in_different_registers(words):
    uniq_words = []
    iterator_words = iter(words)

    for it_word in iterator_words:
        if words.count(it_word) > 1:
            words = [word for word in words if word.lower() != it_word.lower()]

    for word in words:
        if word.lower() not in uniq_words:
            uniq_words.append(word.lower())

    return uniq_words


words = [
    "Мама",
    "МАМА",
    "Мама",
    "папа",
    "ПАПА",
    "Мама",
    "ДЯдя",
    "брАт",
    "Дядя",
    "Дядя",
    "Дядя",
]

print(find_in_different_registers(words))
