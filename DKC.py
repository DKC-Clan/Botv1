import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    await client.change_presence(game=Game(name='Created by LordOfBots'))
    await client.send_message(member, 'Willkommen auf dem Discord des DynamikClans! Bei Fragen einfach an Owner oder Assistants wenden!')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!Rainbowpng':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/530128542474829829/530139272632860701/DYK_Rainbow_Six.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!LOLpng':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/530128542474829829/530139248863739914/DKC_League_of_Legends.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!RLpng':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/530128542474829829/530139296011649024/Rocket_League_DKC.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!CSGOpng':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/530128542474829829/530139219637698560/DKC_CSGO.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '!OWpng':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/530128542474829829/530139284980891652/Overwatch_LOGO.png')
        await client.send_message(message.channel, embed=em)
client.run('NTMwMTM2NjcyNzUxMzIxMTA2.Dw7Aug.q3Qkc6HOy5-U4mt7r0UMem9J9V8')
