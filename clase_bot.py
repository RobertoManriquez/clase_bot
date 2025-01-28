import discord
import random
import os
import asyncio
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def números(ctx, cant: int, num: int):
    for i in range(cant):
        await ctx.send(random.randint(1, num))

@bot.command()
async def juego(ctx, valorgame: int):
    score = 0
    while True:
        if valorgame > 10 or valorgame < 1:
            await ctx.send("El valor del juego debe estar entre 1 y 10.")
            break
        else:
            await ctx.send(f"Puntuación: {score}")
            await asyncio.sleep(1)
            
            await ctx.send(f"¡Si sale {valorgame} pierdes!")
            await asyncio.sleep(1)
            
            intobtenido = random.randint(1, 10)
            await ctx.send(f"El número obtenido es: {intobtenido}")
            await asyncio.sleep(1)
            
            if intobtenido == valorgame:
                await ctx.send(f"¡Perdiste! El número obtenido es igual al número elegido ({valorgame})")
                await asyncio.sleep(1)
                break
            else:
                sumascore = abs(valorgame - intobtenido)
                await ctx.send(f"¡Obtienes {sumascore} puntos!")
                await asyncio.sleep(1)
                
                score += sumascore
    await ctx.send(f"¡Acabó el juego! Tu puntuación final es: {score}")

@bot.command()
async def meme(ctx):
    img_meme = random.choice(os.listdir('images'))
    with open(f'images/{img_meme}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run(token)
