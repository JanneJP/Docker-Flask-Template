def test_api_ping_route(test_client):
    response = test_client.get('/api/ping')

    assert response.status_code == 200
    assert 'pong' in response.text
