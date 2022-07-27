from flask import Flask, request, render_template, send_from_directory
from main.view import main_blueprint
from loader.view import loader_blueprint
from functions import get_all_posts, get_posts_by_value, add_post_to_file

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route('/search')
def search_page():
    s = request.args.get('s')
    return render_template('post_list.html', s=s, all_posts=get_posts_by_value(s))


@app.route("/list")
def page_tag():
    pass


# @app.route("/post", methods=["GET", "POST"])
# def page_post_form():
#     pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    picture = request.files.get('picture')
    filename = picture.filename
    picture.save(f"./uploads/images/{filename}")
    picture_url = f"./uploads/images/{filename}"
    text = request.form.get('content')
    add_post_to_file(picture_url, text)
    return render_template('post_uploaded.html', picture=picture_url, text=text)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

