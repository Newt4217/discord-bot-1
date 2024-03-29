# bot.py
import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
from pricecalc import price_calc
import mimcrvratioasync
import getdvb

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

    if len(names) < 2: #2 hier später mit der ID liste ersetzen
        price = price_calc(names[0], 'usd')
        response = (f'The current price is {price} usd')
        await ctx.send(response)
        return
    price = price_calc(names[0], names[1])
    response = (f'The current price is {price} {names[1]}.')
    await ctx.send(response)


@bot.command(name='ratio', help='gibt ratio zwischen mim und 3crv im main eth pool aus, sollte idealerweise 1 sein')
async def ratio(ctx):
    response = (f'MIM:3CRV {await mimcrvratioasync.ratio_calc()}')
    await ctx.send(response)

@bot.command(name="dvb", help="""dvb [Stadt] [Haltestelle] (optional: [Minuten in Zukunft, Standard 0, Maximal 99] [Anzahl Ergebnisse, Standard 10, Maximal 50])
Der command kann auch Abfahrten aus dem gesamten VVO-Verbund angeben (also Freital, Bad Schandau, Hoyerswerda, Bautzen etc). Dafür dann halt die Stadt ändern.""")
async def dvb(ctx, city, stop, *nums):
    h = 0
    nums = list(nums)

    for h in range(len(nums)):
        try:
            nums[h] = int(nums[h])
        except:
            continue
    h = 0
    try:
        while type(nums[h]) == str:
            city += f" {nums[h]}"
            h += 1
    except:
        pass
    try:
        mif = nums[h]
        limits = nums[h+1]
    except:
        mif = 0
        limits = 10

    response = getdvb.get_stop(city, stop, mif, limits)
    if limits == 0:
        response = "0 Ergebnisse digga ich glaubs auch"
    await ctx.send(response)


bot.run(TOKEN)