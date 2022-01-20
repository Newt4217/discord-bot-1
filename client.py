# bot.py
import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
from main import price_calc

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()
bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='test', help='lediglich ein Testcommand, gibt eine zufällige Nummer von 1,2 oder 3.1 & 3.2 aus')
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

@bot.command(name='p', help='Preise von Kryptowährungen mit der Syntax p [Währung, dessen Preis gesucht ist] [Währung in der der Preis angegeben werden soll]')
async def p(ctx, *names):
#irgendwie bei vs currency = none aus usd setzen
    #if names[1] == None:
    #    names[1] = 'usd'
    price = price_calc(names[0], names[1])
    response = (f'The current price is {price} {names[1]}')
    await ctx.send(response)


bot.run(TOKEN)
