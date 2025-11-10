import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import sys
import random

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
if token is None:
    sys.exit("DISCORD_TOKEN not found.")

handler = logging.FileHandler(filename='discord.log',encoding='utf-8',mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='*',intents=intents)


@bot.event
async def on_ready():
    print("Pronto para invocar horrores cósmicos")



@bot.command()
async def teste(ctx):
    await ctx.send(f"é negada...{ctx.author.mention}")

@bot.command()
async def roll(ctx, dice, sides):
    result =0
    for i in range(int(dice)+1):
        print(i,result)
        result += random.randint(1,int(sides))
    await ctx.channel.send(f"{dice}d{sides} resultado da rolagem:{result}")





bot.run(token, log_handler=handler,log_level=logging.DEBUG)
