class Player:
    def __init__(self, name: str):
        self.name = name
        self.used_words = []

    def add_used_word(self, user_word: str):
        self.used_words.append(user_word)

    def used_words_length(self):
        return len(self.used_words)

    def is_used(self, user_word: str):
        return user_word in self.used_words

    def __repr__(self):
        return f'Использованные слова {self.used_words}'
