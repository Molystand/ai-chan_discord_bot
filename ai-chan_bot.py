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

    await ctx.message.delete()
    await ctx.send(
        'Ваше сообщение о баге передано в службу поддержки! В качестве извинений примите от нас 108 примогемов и крестом по ебалу')


# Вернуть абсолютный путь к рандомному файлу из каталога
def get_randfile_abspath(catalog: str) -> str:
    files = os.listdir(catalog)
    file = random.choice(files)
    path = os.path.abspath(f'{catalog}{file}')
    print(path)
    return path


@bot.command(aliases=['кушац', 'еда'])
async def eat(ctx, user: discord.User):
    file = discord.File(get_randfile_abspath('./media/gif/eat/'),
                        filename='image.gif')
    embed = discord.Embed(description=f'{user.mention}, вас съел {ctx.author.mention}')
    embed.set_image(url='attachment://image.gif')

    await ctx.message.delete()
    await ctx.send(file=file, embed=embed)


@bot.command(aliases=['кормить', 'покормить'])
async def feed(ctx, user: discord.User = None):
    embed = discord.Embed()

    if user == ctx.author or user is None:
        embed.description = f'{ctx.author.mention} покушал'
        file = discord.File(get_randfile_abspath('./media/gif/feed/self/'),
                            filename='image.gif')
    else:
        embed.description = f'{ctx.author.mention} накормил {user.mention}'
        file = discord.File(get_randfile_abspath('./media/gif/feed/'),
                            filename='image.gif')

    embed.set_image(url='attachment://image.gif')

    await ctx.message.delete()
    await ctx.send(file=file, embed=embed)


# @bot.command(aliases=['кормить', 'покормить'])
# async def feed(ctx):
#     feed(ctx, ctx.author)


@bot.command()
async def pat(ctx, user: discord.User):
    file = discord.File(get_randfile_abspath('./media/gif/pat/'),
                        filename='image.gif')
    embed = discord.Embed(description=f'{user.mention}, вас погладил {ctx.author.mention}')
    embed.set_image(url='attachment://image.gif')

    await ctx.message.delete()
    await ctx.send(file=file, embed=embed)


@bot.command(aliases=['потискать', 'обнять'])
async def hug(ctx, user: discord.User = None):
    await ctx.message.delete()
    embed = discord.Embed()

    if user == ctx.author or user is None:
        embed.description = f'Обнимите кто-нибудь {ctx.author.mention}'
        await ctx.send(embed=embed)
    else:
        file = discord.File(get_randfile_abspath('./media/gif/hug/'),
                            filename='image.gif')
        embed.description = f'{user.mention}, вас обнял {ctx.author.mention}'
        embed.set_image(url='attachment://image.gif')
        await ctx.send(file=file, embed=embed)
    # todo попробовать унифицировать await через file=None


@bot.command(aliases=['тык', 'ткнуть'])
async def poke(ctx, user: discord.User):
    file = discord.File(get_randfile_abspath('./media/gif/poke/'),
                        filename='image.gif')
    embed = discord.Embed(description=f'{ctx.author.mention} сделал тык {user.mention}')
    embed.set_image(url='attachment://image.gif')

    await ctx.message.delete()
    await ctx.send(file=file, embed=embed)


@bot.command(aliases=['флекс'])
async def flex(ctx):
    file = discord.File(get_randfile_abspath('./media/gif/flex/'),
                        filename='image.gif')
    embed = discord.Embed(description=f'{ctx.author.mention} сегодня флексит')
    embed.set_image(url='attachment://image.gif')

    await ctx.message.delete()
    await ctx.send(file=file, embed=embed)


# todo съесть, погладить, обнять, тькнуть себя
# @user вновь пытается гладить себя в общественном месте
# Обнимите кто-нибудь @user
# @user думает выбрать вилку (мб)
# todo бд для бота
# todo обработка исключений


@bot.command(name='прогноз')
# Вывод шутливого прогноза с gif
async def predict(ctx):
    # todo использовать бд, если нужно будет соответствие картинки и текста
    # открыть файл с предсказаниями
    # разбить файл на список строк
    # choise рандомную строку
    await ctx.message.delete()
    await ctx.send()


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(TOKEN)
