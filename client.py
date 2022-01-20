# bot.py
import os
import discord
import random
from main import price_calc
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
   
@bot.command(name='p')
async def p(ctx, currency_name, vs_currency)
#irgendwie bei vs currency = none aus usd setzen
    price = price_calc(currency_name, vs_currency)
    response = 'The current price of 1 '+currency name+' is '+price+' '+vs_currency

bot.run(TOKEN)
