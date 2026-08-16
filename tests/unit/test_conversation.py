from radiolab_ai.app.conversation import get_response


def test_get_response_returns_mock_response():
    response = get_response("What is SDR?")

    assert response == "Mock response for: What is SDR?"