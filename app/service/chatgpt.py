import openai

from app.service.secret import get_secret

openai.api_key = get_secret("openai_api_key")


class ChatGptApi:
    def __init__(self):
        self._model = 'gpt-3.5-turbo'

    @property
    def model(self):
        return self._model

    async def answer_message(self, message: str) -> str:
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "{}".format(message)}
        ]

        openai.ChatCompletion.create(
            model=self._model,
            messages=messages
        )
