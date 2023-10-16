"""
Реализуйте контекст менеджер на основе класса, который создаёт временный файл с помощью библиотеки tempfile. 
В данном классе по мимо этого должны быть реализованы методы:
repeat() - Дублирует текущее содержание файла и добавляет в конец файла
write(msg) - Записывает текст в начало файла
show() - Выводит содержимое файла в консоль
При окончании работы менеджера, должно быть напечатано количество символов в файле и закрыт временный файл.
"""

import tempfile


class TempFileManager:
    def __init__(self):
        self.file = None

    def __enter__(self):
        self.file = tempfile.TemporaryFile(mode="w+")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.seek(0)
        text_file = self.file.read()
        print(f"Количество символов в файле: {len(text_file)}")
        self.file.close()

    def repeat(self):
        self.file.seek(0)
        text = self.file.read()
        self.file.write(text)

    def write(self, msg):
        self.file.seek(0)
        text = self.file.read()
        self.file.seek(0)
        self.file.write(msg + "\n" + text)

    def show(self):
        self.file.seek(0)
        text = self.file.read()
        print(text)


with TempFileManager() as file_manager:
    file_manager.write("First, but last Record")
    file_manager.show()
    file_manager.write("Second Record")
    file_manager.write("Third, but First Record")
    file_manager.repeat()
    file_manager.show()
