from app.llm import ask_gemini


class FakeResponse:
    text = "Hello from Mock!"


class FakeModels:
    def generate_content(self, model, contents):
        return FakeResponse()


class FakeClient:
    models = FakeModels()


def test_ask_gemini(mocker):
    mocker.patch("app.llm.client", FakeClient())

    result = ask_gemini("Hi")

    assert result == "Hello from Mock!"