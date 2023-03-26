from discord.ext import commands


class ChatDalCog(commands.Cog, name='Chat GPT Cog'):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            pass
