from discord.ext import commands


class ChatDalCog(commands.Cog, name='Chat GPT Cog'):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self._channel_id = None

    @property
    def last_member(self):
        return self._last_member

    @property
    def channel_id(self):
        return self._channel_id

    @commands.Cog.listener()
    async def answer_on_message(self, message):
        if (message.author != self.bot.user) and (message.channel == self._channel_id):
            pass