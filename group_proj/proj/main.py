from classes.player import Player
from utils import get_data_from_url, load_random_word

URL = 'https://jsonkeeper.com/b/QUQK'
STOP_WORD = ['stop', 'стоп']


def main():
    url_data = get_data_from_url(URL)
    user_game_words = load_random_word(url_data)
    user_name = input('Введите имя игрока: ')

    user_game = Player(user_name)
    print(f'Привет, {user_game.name}!')
    print(f'Составьте {user_game_words.values_number()} слов из слова {user_game_words.main_words.upper()}')
    print('Слова должны быть не короче 3 букв')
    print(f'Чтобы закончить игру, угадайте все слова или напишите "{STOP_WORD[0]}" или "{STOP_WORD[1]}"')
    right_answer = 0
    print('Поехали, ваше первое слово? ')

    while right_answer != user_game_words.values_number():
        user_word = input()
        if user_word in STOP_WORD:
            break
        if len(user_word) < 3:
            print('слишком короткое слово')
        elif user_game_words.is_present(user_word):
            if not user_game.is_used(user_word):
                user_game.add_used_word(user_word)
                right_answer += 1
                print('верно')
            else:
                print('уже использовано')
        else:
            print('неверно')

    print(f'Игра завершена, вы угадали {user_game.used_words_length()} слов!')


if __name__ == "__main__":
    main()
