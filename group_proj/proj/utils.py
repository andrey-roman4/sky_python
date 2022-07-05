import requests
import random
from classes.basicwords import BasicWords


def get_data_from_url(link: str) -> list:
    """
    Ф-ция возвращает данные загруженные по ссылке
    :param link:
    :return: list
    """
    response = requests.get(link)
    return response.json()


def return_random_element(data: list) -> list:
    """
    Ф-ция возвращает случайный элемент из списка
    :param data:
    :return: list
    """
    return random.choice(data)


def load_random_word(data: list):
    """
    Ф-ция возвращает Объект класса BasicWords
    :param data:
    :return: Объект класса BasicWords
    """
    element = return_random_element(data)
    word = element['word']
    words = list(set(element['subwords']))
    game_word = BasicWords(word, words)
    return game_word
