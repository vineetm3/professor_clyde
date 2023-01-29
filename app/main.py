import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)
load_dotenv()
token = os.getenv('token')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
# Ignore messages from the bot itself so that there's no conflict.
    if message.author == client.user:
        return

    if message.content == '$hello':
        await message.channel.send('Hello!')

client.run(token)