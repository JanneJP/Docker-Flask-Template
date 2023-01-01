from project import db
from project.models import Placeholder


def test_db_placeholder_model(test_client):
    model = Placeholder('test string')

    models = Placeholder.query.all()

    assert len(models) == 0

    db.session.add(model)
    db.session.commit()

    models = Placeholder.query.all()

    assert len(models) == 1
