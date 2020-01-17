
# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')


client = discord.Client()

@client.event
async def on_ready():

        for guild in client.guilds:
                if guild == guild.name:
                        break
        print(
                f'\n\n{client.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})\n'
        )

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')



        TESTING TESTING

client.run(token)