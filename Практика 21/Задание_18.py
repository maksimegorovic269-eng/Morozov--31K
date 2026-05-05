# Задание 18
# Класс Message со слотами и форматированием сообщения

class Message:
    __slots__ = ("text", "author")

    def __init__(self, text, author):
        self.text = text
        self.author = author

    def format_message(self):
        return f"{self.author}: {self.text}"


message = Message("Привет, как дела?", "Иван")

print(message.format_message())
