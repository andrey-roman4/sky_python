from flask import Flask, request, render_template, send_from_directory
from main.view import main_blueprint
from loader.view import loader_blueprint
from loader.utils import save_picture
from functions import get_posts_by_value, add_post_to_file
from json import JSONDecodeError
import logging

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

logging.basicConfig(filename='basic.log', level=logging.INFO)


@app.route('/search')
def search_page():
    s = request.args.get('s')
    logging.info(f'Выполняю поиск по запросу: {s}')
    try:
        all_posts = get_posts_by_value(s)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный JSON'
    return render_template('post_list.html', s=s, all_posts=all_posts)


@app.route("/post", methods=["POST"])
def page_post_upload():
    picture = request.files.get('picture')
    path = save_picture(picture)
    text = request.form.get('content')
    pic_format = picture.filename.split('.')[-1]
    if pic_format not in ['jpeg', 'png', 'jpg']:
        logging.info(f'Загруженный файл не картинка а формат "{pic_format}"')
        return 'Не верный формат файла'
    if not picture or not text:
        return 'Нет картинки или текста'
    try:
        add_post_to_file(path, text)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный JSON'
    return render_template('post_uploaded.html', picture=path, text=text)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

