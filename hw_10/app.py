from flask import Flask
from utils import get_all, get_by_pk, get_by_skill


def main():
    app = Flask(__name__)

    @app.route('/')
    def candidates_page():
        return get_all()

    @app.route('/candidates/<int:pk>')
    def candidate_page(pk):
        return get_by_pk(pk)

    @app.route('/skills/<skill>')
    def skills_page(skill):
        return get_by_skill(skill)

    app.run()


if __name__ == "__main__":
    main()
