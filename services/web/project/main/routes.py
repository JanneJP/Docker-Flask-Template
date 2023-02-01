from flask import render_template, send_from_directory, current_app

from project.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html')


@bp.route("/static/<path:filename>")
def static(filename):
    return send_from_directory(current_app.config["STATIC_FOLDER"], filename)
