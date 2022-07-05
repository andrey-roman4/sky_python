class BasicWords:
    def __init__(self, word: str, words_collection: list):
        self.main_words = word
        self.words_collection = words_collection

    def __repr__(self):
        return f'Исходное слово {self.main_words}'

    def is_present(self, user_word: str):
        return user_word in self.words_collection

    def values_number(self):
        return len(self.words_collection)
