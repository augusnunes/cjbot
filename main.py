import discord 
from discord.ext import commands
from discord.channel import CategoryChannel
import os 


description = '''Bot do CJ.

Só testando algumas coisas...
'''
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

default_category = None

@bot.command()
async def c(context):
    s = "Escolha alguma categoria:\n\n"
    categories = []
    for e in context.guild.channels:
        if type(e) == CategoryChannel:
            categories.append(e)
    for i in range(len(categories)):
        s += f"{i+1} - {categories[i]}\n"
    await context.send(s)

@bot.command()
async def category(context, numero: str = 0):
    categories = []
    for e in context.guild.channels:
        if type(e) == CategoryChannel:
            categories.append(e)
    global default_category 
    default_category = categories[int(numero)-1]
    await context.send(f"A Categoria padrão é {default_category.name}")

@bot.command()
async def verifica_category(context):
    if default_category == None:
        await context.send("Nenhuma Categoria selecionada")
    else:
        await context.send(f"A Categoria padrão é {default_category.name}")

@bot.command()
async def event(context, nome: str, anonimo: str):
    print(context)
    print(anonimo)
    print(type(context.guild))
    for i in default_category.channels:
        if i.name == nome:
            await context.send(f"Já existe um evento com o nome: {nome}")
            return False
    await context.send(f"Você está criando um evento: {nome}")
    await default_category.create_text_channel(nome)
    await default_category.create_voice_channel(nome)


@bot.command()
async def close(context):
    channel = context.channel.name
    for i in default_category.channels:
        if i.name == channel:
            await i.delete()


token = os.getenv('BOT_API_TOKEN_DISCORD')
bot.run(token)