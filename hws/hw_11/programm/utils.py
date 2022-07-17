import json


def load_candidates():
    """
    Ф-ция открывает и распаковывает json файл и возвращает список
    :return: list
    """
    with open('candidates.json', mode='r', encoding='utf-8') as file:
        file_data = json.load(file)
        return file_data


def get_candidate(pk: int) -> dict:
    """
    которая вернет кандидата по pk
    :return:
    """
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate


def get_candidates_by_skill(skill_name: str):
    """
    Ф-ция которая вернет кандидатов по навыку
    :return:
    """
    skilled_candidates = []
    for candidate in load_candidates():
        if skill_name.title() in candidate['skills'] or skill_name.lower() in candidate['skills']:
            skilled_candidates.append(candidate)
    return skilled_candidates


def get_candidates_by_name(candidate_name: str):
    """

    :param candidate_name:
    :return:
    """
    result_candidates = []
    for candidate in load_candidates():
        if candidate['name'] == candidate_name:
            result_candidates.append(candidate)
        return result_candidates
