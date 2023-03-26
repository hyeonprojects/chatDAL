import openai


class ChatGptApi:
    def __init__(self):
        self.chat_api = openai.ChatCompletion.create(
            model='gpt-4',
            message=[

            ]
        )

    async def answer_chat(self, message: str) -> str:
        pass
