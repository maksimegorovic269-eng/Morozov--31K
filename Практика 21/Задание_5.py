# Задание 5
# Класс Book со слотами и методом info()

class Book:
    __slots__ = ("title", "author")

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Книга: {self.title}, автор: {self.author}")


book = Book("Преступление и наказание", "Ф. М. Достоевский")
book.info()
