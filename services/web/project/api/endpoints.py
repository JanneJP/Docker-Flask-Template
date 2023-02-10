from project.api import bp


@bp.route('/ping')
def ping():
    return 'pong'
