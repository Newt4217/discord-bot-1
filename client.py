# bot.py
import os
import discord
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()
bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='test')
async def test1(ctx):

    test_collection = [
        '1',
        '2',
        (
            '3.1, '
            '3.2'
        ),
    ]
    response = random.choice(test_collection)
    await ctx.send(response)

bot.run(TOKEN)
