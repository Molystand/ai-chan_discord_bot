import os
import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='%')


@bot.command()
async def beam(ctx):
    await ctx.send('AI-CHAN BEAM!')


@bot.command(name='баг')
async def bugs(ctx, bug_note: str):
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


token_file_name = 'token.txt'
with open(token_file_name) as tf:
    bot_token = tf.readline().strip()

bot.run(bot_token)
