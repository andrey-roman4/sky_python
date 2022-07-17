from flask import Flask, render_template
from utils import get_candidate, get_candidates_by_skill, load_candidates, get_candidates_by_name


CANDIDATES = load_candidates()


def main():
    app = Flask(__name__)

    @app.route('/')
    def candidates_page():
        return render_template('list.html', candidates=CANDIDATES)

    @app.route('/candidate/<int:pk>')
    def candidate_page(pk):
        return render_template('single.html', candidate=get_candidate(pk))

    @app.route('/skills/<skill>')
    def skills_page(skill):
        return render_template('skill.html', candidates=get_candidates_by_skill(skill), skill=skill)

    @app.route('/search/<candidates_name>')
    def search_page(candidates_name):
        return render_template('search.html', candidates=get_candidates_by_name(candidates_name))

    app.run(debug=True)


if __name__ == "__main__":
    main()
