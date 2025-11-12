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
    print(bot.user.name)


@bot.command()
async def roll(ctx, dice: str):
    """formato esperado: NdN"""
    try:
        rolls, limit = map(int,dice.split('d'))
    except Exception:
        await ctx.send("o formato deve ser 'NdN'")
        return

    result = ', '.join(str(random.randint(1,limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command()
async def maior(ctx, dice: str):
    """formato esperado: NdN"""
    try:
        rolls, limit = map(int,dice.split('d'))
    except Exception:
        await ctx.send("o formato deve ser 'NdN'")
        return

    resultados = [random.randint(1, limit) for _ in range(rolls)]
    maior = max(resultados)

    # Mostra todas as rolagens e o maior valor
    await ctx.send(f"Rolagens: {', '.join(map(str, resultados))} Maior valor: {maior}")


bot.run(token, log_handler=handler,log_level=logging.DEBUG)
