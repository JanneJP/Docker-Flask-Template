from project.models import Placeholder


def test_placeholder_model():
    model = Placeholder('test test')

    assert model.test_string == 'test test'
