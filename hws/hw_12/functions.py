import json


def open_file():
    with open('posts.json', mode='r', encoding='utf-8') as file:
        file_data = json.load(file)
        return file_data


def get_all_posts():
    return open_file()


def get_posts_by_value(value):
    result = []
    for post in get_all_posts():
        if value.lower() in post['content']:
            result.append(post)
    return result


def add_post_to_file(url, text):
    picture = {
        'pic': url,
        'content': text,
    }

    with open('posts.json', mode='r', encoding='utf-8') as file:
        file_data = json.load(file)
        file_data.append(picture)
        file_data = json.dumps(file_data)

    with open('posts.json', mode='w', encoding='utf-8') as file:
        file.write(f'{file_data}')
