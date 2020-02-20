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

@bot.command(name="surprise")
async def surprise(ctx):
    await ctx.sent(random.choice(["Do you live in a corn field, cause I'm stalking you.",
                          "I’m not a hoarder but I really want to keep you forever.",  
                          "You're so beautiful that you made me forget my pickup line.",
                          "Are you lost ma'am? Because heaven is a long way from here.", 
                          "Four plus four equals eight, but you plus me equals fate.", 
                          "I must be a snowflake, because I've fallen for you.", 
                          "You must be a hell of a thief because you stole my heart from across the room.",
                          "If you were a booger I'd pick you first.", 
                          "If you were a chicken, you'd be impeccable.",
                          "Life without you would be like a broken pencil... pointless,"]))





bot.run(token)

#allison

