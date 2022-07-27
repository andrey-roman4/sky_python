from flask import Blueprint, render_template

loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route('/post')
def page_index():
    return render_template('post_form.html')
