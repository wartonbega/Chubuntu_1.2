import discord
from discord.ext import commands

TOKEN = 'NzI5NjY4MjA0MDY2MjQyNTYw.XwMTBQ.fsUeSdrJgms7NCluxNZOYL483zo'

description = '''Anton's replacement'''
bot = commands.Bot(command_prefix='*', description=description)

a=True

@bot.event
async def on_ready():
    print('-------------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------------')


@bot.command()
async def debut(ctx):
    await ctx.channel.purge(limit=1)
    while a:
        try:
            message=input('Message : ')
            await ctx.send(message)
        except discord.errors.HTTPException:
            print('ne pas envoyer de message vide')
            continue

@bot.command()
async def dogme(ctx):
    channel = bot.get_channel(12324234183172)
    await channel.send('hello')

bot.run(TOKEN)
