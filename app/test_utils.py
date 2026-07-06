from app.utils import format_response


def test_format_response():
    result = format_response("Hello")

    assert result == "\nAI: Hello\n"