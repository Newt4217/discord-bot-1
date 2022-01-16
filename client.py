# bot.py
import os
import discord
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    test_collection = [
        '1',
        '2',
        (
            '3.1, '
            '3.2'
        ),
    ]

    if message.content == 'test_collection':
        response = random.choice(test_collection)
        await message.channel.send(response)

client.run(TOKEN)
