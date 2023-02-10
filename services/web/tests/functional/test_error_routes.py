def test_error_404_route(test_client):
    response = test_client.get('/doesnotexist')

    assert response.status_code == 404
