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


# Вернуть абсолютный путь к рандомному файлу gif из каталога
def get_randgif_abspath(catalog: str) -> str:
    files = os.listdir(catalog)
    gif_files = [gif for gif in files if gif.endswith('.gif')]
    file = random.choice(gif_files)
    path = os.path.abspath(f'{catalog}{file}')
    print(path)
    return path


@bot.command(aliases=['кушать', 'еда', 'кусь'])
async def eat(ctx, user: discord.User = None):
    embed = discord.Embed()
    file = None

    if user == ctx.author or user is None:
        embed.description = f'{ctx.author.mention} очень голоден и требует еды'
    else:
        file = discord.File(get_randgif_abspath('./media/gif/eat/'),
                            filename='image.gif')
        embed.description = f'{user.mention}, вас съел {ctx.author.mention}'
        embed.set_image(url='attachment://image.gif')

    await ctx.message.delete()
    await ctx.send(file=file, embed=embed)


@bot.command(aliases=['кормить', 'покормить'])
async def feed(ctx, user: discord.User = None):
    embed = discord.Embed()

    if user == ctx.author or user is None:
        embed.description = f'{ctx.author.mention} покушал'
        file = discord.File(get_randgif_abspath('./media/gif/feed/self/'),
                            filename='image.gif')
    else:
        embed.description = f'{ctx.author.mention} накормил {user.mention}'
        file = discord.File(get_randgif_abspath('./media/gif/feed/'),
                            filename='image.gif')

    embed.set_image(url='attachment://image.gif')

    await ctx.message.delete()
    await ctx.send(file=file, embed=embed)


@bot.command(aliases=['погладить', 'гладить'])
async def pat(ctx, user: discord.User = None):
    embed = discord.Embed()
    file = None

    if user == ctx.author or user is None:
        embed.description = f'{ctx.author.mention} гладит себя в общественном месте\nЯ отказываюсь это показывать'
    else:
        file = discord.File(get_randgif_abspath('./media/gif/pat/'),
                            filename='image.gif')
        embed.description = f'{user.mention}, вас погладил {ctx.author.mention}'
        embed.set_image(url='attachment://image.gif')

    await ctx.message.delete()
    await ctx.send(file=file, embed=embed)


@bot.command(aliases=['потискать', 'обнять'])
async def hug(ctx, user: discord.User = None):
    embed = discord.Embed()
    file = None

    if user == ctx.author or user is None:
        embed.description = f'Обнимите кто-нибудь {ctx.author.mention}'
    else:
        file = discord.File(get_randgif_abspath('./media/gif/hug/'),
                            filename='image.gif')
        embed.description = f'{user.mention}, вас обнял {ctx.author.mention}'
        embed.set_image(url='attachment://image.gif')

    await ctx.message.delete()
    await ctx.send(file=file, embed=embed)


@bot.command(aliases=['тык', 'ткнуть'])
async def poke(ctx, user: discord.User = None):
    embed = discord.Embed()

    if user == ctx.author or user is None:
        file = discord.File(get_randgif_abspath('./media/gif/poke/self/'),
                            filename='image.gif')
        embed.description = f'{ctx.author.mention} выбирает вилку и делает selfтык'
    else:
        file = discord.File(get_randgif_abspath('./media/gif/poke/'),
                            filename='image.gif')
        embed.description = f'{ctx.author.mention} сделал тык {user.mention}'

    embed.set_image(url='attachment://image.gif')

    await ctx.message.delete()
    await ctx.send(file=file, embed=embed)


@bot.command(aliases=['флекс'])
async def flex(ctx):
    file = discord.File(get_randgif_abspath('./media/gif/flex/'),
                        filename='image.gif')
    embed = discord.Embed(description=f'{ctx.author.mention} сегодня флексит')
    embed.set_image(url='attachment://image.gif')

    await ctx.message.delete()
    await ctx.send(file=file, embed=embed)


@bot.command(aliases=['аватар', 'ава'])
async def avatar(ctx, *, avamember: discord.Member = None):
    avatar_url = avamember.avatar_url
    embed = discord.Embed(description=f'Аватар пользователя {avamember.mention} по запросу {ctx.author.mention}')
    embed.set_image(url=avatar_url)

    await ctx.message.delete()
    await ctx.send(embed=embed)


@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send('Пользователь не найден')



# todo погладить себя
# @user вновь пытается гладить себя в общественном месте
# todo бд для бота
# todo обработка исключений


@bot.command(name='прогноз')
# Вывод шутливого прогноза с gif
async def predict(ctx):
    # todo использовать бд, если нужно будет соответствие картинки и текста
    # открыть файл с предсказаниями
    # разбить файл на список строк
    # choise рандомную строку
    await ctx.send('На улице +40, ты охуел? Я отказываюсь работать в такую жару. С уважением, Аи-чан >_<')

    await ctx.message.delete()
    await ctx.send()


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(TOKEN)
