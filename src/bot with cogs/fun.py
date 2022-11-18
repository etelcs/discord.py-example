import asyncio
import json
import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
bot.remove_command('help')
print("fun - bot executing..")

with open('fun.json', 'r') as f:
    settings = json.loads(f.read())
    TOKEN = settings['TOKEN']

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())
