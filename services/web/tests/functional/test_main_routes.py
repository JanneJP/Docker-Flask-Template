def test_index_route(test_client):
    response = test_client.get('/')
    assert response.status_code == 200

    response = test_client.get('/index')
    assert response.status_code == 200


def test_static_route(test_client):
    response = test_client.get('/static/test.txt')
    assert response.status_code == 200
    assert response.text == 'Hello, World!'
