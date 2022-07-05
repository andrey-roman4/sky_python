import requests
import random


def return_random_digit(start: int, end: int) -> int:
    """
    Ф-ция возвращает случайное число из заданного диапазона
    :param start:
    :param end:
    :return: int
    """
    return random.randint(start, end)


def return_random_word(raw_data: list, end: int) -> str:
    """
    Ф-ция возвращает случайное слово из списка
    :param raw_data:
    :param end:
    :return: str
    """
    return raw_data[return_random_digit(0, end)]['word']


def get_data_from_url(link: str) -> list:
    """
    Ф-ция возвращает данные загруженные по ссылке
    :param link:
    :return: list
    """
    response = requests.get(link)
    return response.json()


def return_subwords_count(raw_data: list, end: int) -> int:
    """
    Ф-ция возвращает число под слов для нахождения
    :param raw_data:
    :param end:
    :return:
    """
    return len(raw_data[return_random_digit(0, end)]['subwords'])
