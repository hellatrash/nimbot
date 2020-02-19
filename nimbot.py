import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command(name='coinflip')
async def coinflip(ctx):
    await ctx.send(random.choice(["heads", "tails"]))

@bot.command(name="average")
async def average(ctx, a, b):
    await ctx.send( (a+b)/2)

bot.run(token)

#allison

