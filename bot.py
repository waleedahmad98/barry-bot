import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')
words = ['BORK!', 'WOOF!', 'BORK BORK!', 'WOOF WOOF!', '*wags tail*', 'BARK!', '🦴', 'WOOF 🐶', '🐾🐶🐾']

@bot.event
async def on_ready():
    print(f'{bot.user.name} has rolled over into the server!')

@bot.command(name='talk')
async def _talk(ctx):
    await ctx.send(random.choice(words))


@bot.command(name='photo')
async def _photo(ctx):
    photos = os.listdir('photos')
    photo = random.choice(photos)
    fp = open(os.path.join('photos', photo),'rb')
    file = discord.File(fp)
    await ctx.send(random.choice(words),file=file)

bot.run(TOKEN)