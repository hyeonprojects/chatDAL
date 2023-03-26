import openai

from app.service.secret import get_secret

openai.api_key = get_secret("openai_api_key")


class ChatGptApi:
    def __init__(self):
        self._model = 'gpt-3.5-turbo'
    @property
    def model(self):
        return self.model

    async def answer_message(self, message: str) -> str:
        response = openai.Completion.create(
            model=self._model,
            message=message,
        )

    async def num_tokens_from_messages(self, messages, model='gpt-3.5'):
        pass