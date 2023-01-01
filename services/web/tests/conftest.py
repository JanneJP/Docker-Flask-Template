import pytest

from project import create_app, db


@pytest.fixture(scope='module')
def test_client():
    app = create_app(config_class='pytest')

    assert app.config['TESTING'] is True
    # print(app.config['SQLALCHEMY_DATABASE_URI'])

    with app.test_client() as testing_client:

        with app.app_context():
            db.drop_all()
            db.create_all()
            db.session.commit()

            yield testing_client
