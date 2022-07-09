import json


def load_candidates(filename: str) -> list:
    """
    Ф-ция открывает и распаковывает json файл и возвращает список
    :param filename:
    :return: list
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        file_data = json.load(file)
        return file_data


def get_all() -> str:
    """
    :return:
    <pre>
    Имя кандидата -
    Позиция кандидата
    Навыки через запятую
    </pre>
    """
    raw_candidates = load_candidates('candidates.json')
    results = '<pre>\n'

    for candidate in raw_candidates:
        results += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'
    return results + '</pre>'


def get_by_pk(pk):
    """
    которая вернет кандидата по pk
    :return:
    """
    raw_candidates = load_candidates('candidates.json')
    results = '<pre>\n'
    pic_url = ''
    for candidate in raw_candidates:
        if candidate['pk'] == pk:
            pic_url = f'<img src="{candidate["picture"]}">\n'
            results += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'
    return pic_url + results + '</pre>'


def get_by_skill(skill_name):
    """
    которая вернет кандидатов по навыку
    :return:
    """
    raw_candidates = load_candidates('candidates.json')
    results = '<pre>\n'
    for candidate in raw_candidates:
        if skill_name.title() in candidate['skills'] or skill_name.lower() in candidate['skills']:
            results += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'
    return results + '</pre>'
