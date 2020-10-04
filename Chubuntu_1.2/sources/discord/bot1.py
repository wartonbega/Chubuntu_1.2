import discord
from discord.ext import commands
from discord.ext import tasks
import os

TOKEN = 'NzI5NjY4MjA0MDY2MjQyNTYw.XwMTBQ.fsUeSdrJgms7NCluxNZOYL483zo'

description = '''Anton's replacement'''
client = commands.Bot(command_prefix='__', description=description)

a=True

channel_ids = {'bot-anton':"729720674373074954",'général':"637259451153514499"}
all_channel = ['bot-anton','général']
def init():
    global channel
    channelinput = input("sur quel channel voulez vous discuter ? (si vous tapez c_g, vous obtenez la liste des channels) :")
    if channelinput == 'c_g':
        for i in range(len(all_channel)):
            print(all_channel[i])
        init()
    else:
        channel = channel_ids[channelinput]
        return
            
init()

@client.event
async def on_message(message):
    if str(message.channel.id) in str(channel):
        if message.author.name == 'anton chat bot':
            print('-----------------------------------')
            print("envoyé : #",str(message.channel),str(message.channel),"-- de vous :\n",str(message.content))
        else:
            file = open('./settings.txt','w')
            file.write(message.content)
            file.close()
            print('-----------------------------------')
            print("envoyé : #",str(message.channel),"#-- de : ",str(message.author.name),":\n",str(message.content))
            os.popen('espeak bip','r')
    
@client.event
async def on_ready():
    print('-------------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------------')




client.run(TOKEN)
