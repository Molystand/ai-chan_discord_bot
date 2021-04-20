import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='%')


@bot.command()
async def beam(ctx):
    await ctx.send('AI-CHAN BEAM!')


@bot.command(name='баг')
async def bugs(ctx, *, bug_note: str):
    print(bug_note)
    await ctx.send('Ваше сообщение о баге передано в службу поддержки! В качестве извинений примите от нас 108 примогемов и крестом по ебалу')


@bot.command(aliases=['кушац', 'еда'])
async def eat(ctx, user: discord.User):
    author = ctx.author.mention
    await ctx.send(f'{user.mention}, вас съел {author}')


@bot.command()
async def pat(ctx, user: discord.User):
    catalog = './media/gif/pat/'
    files = os.listdir(catalog)
    file = random.choice(files)
    abspath = os.path.abspath(f'{catalog}{file}')

    await ctx.send(f'{user.mention}, вас погладил {ctx.author.mention}', file=discord.File(abspath))


@bot.command(name='прогноз')
# Вывод шутливого прогноза с gif
async def predict(ctx):
    # открыть файл с предсказаниями
    # разбить файл на список строк
    # choise рандомную строку
    await ctx.send()


@bot.command()
# Вывод окна помощи бота
async def bot_help(ctx):
    await ctx.send()


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(TOKEN)
