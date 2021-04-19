import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='%')


@bot.command()
async def beam(ctx):
    await ctx.send('AI-CHAN BEAM!')





tokenfile_name = 'token.txt'
with open(tokenfile_name) as tf:
    bot_token = tf.readline().strip()

bot.run(bot_token)
