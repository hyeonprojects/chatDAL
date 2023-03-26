import logging

import discord
from discord.ext import commands

from app.service.secret import get_secret

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

description = '''
개발 집사 첫번쨰 테스트 모델
'''

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    logging.info('Logging in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('!안녕'):
        await message.channel.send('안녕하세요. 개발 집사 입니다.')


if __name__ == '__main__':
    bot.run(get_secret('discord_bot_token'))
