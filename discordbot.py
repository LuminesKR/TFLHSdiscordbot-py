from cmath import log
from discord.ext import commands
from distutils.sysconfig import PREFIX
import discord
import random
from dotenv import load_dotenv
import os
load_dotenv()


PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("외고생들의 이야기를 들어주는중"))

@client.event
async def on_message(message):
    if message.content == "!안녕":
        await message.channel.send ("반가워요!")
    
    if message.content == "!내신 등급":
        await message.channel.send ("1등급 4등 2등급 13등 3등급 27등 4등급 48등 5등급 72등 6등급 92등 7등급 106등 8등급 115등 9등급 120등")
    
    
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
