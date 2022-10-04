import json
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

#gives a prefix & grants all intents to the bot (important)
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

#gets file called template.json
with open('template.json', 'r') as f:
    settings = json.loads(f.read())
    #gets token value from template.json
    TOKEN = settings['TOKEN']

#removes default !help command
bot.remove_command('help')
print("bot executing..")

#on_ready is when the bot goes online
@bot.event
async def on_ready():
    #sets a status to the bot
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="You"))

@bot.command(invoke_without_command=True)
#checks if the command sender has administrator permissions
@has_permissions(administrator=True)
async def hey(ctx):
    #gets channel name from ctx (where !hey was executed) and sends a message
    await ctx.send("Hello!")

#runs the bot
bot.run(TOKEN)