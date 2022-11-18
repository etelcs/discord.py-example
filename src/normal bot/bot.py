import json
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

#gives a prefix & grants all intents to the bot (important)
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

#gets file called template.json
with open('fun.json', 'r') as f:
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
    #syncs slash commands
    synced = await bot.tree.sync()
    print(f"slash commands total -> {len(synced)}...")

@bot.command(invoke_without_command=True)
#checks if the command sender has administrator permissions
@has_permissions(administrator=True)
async def hey(ctx):
    #gets channel name from ctx (where !hey was executed) and sends a message
    await ctx.send("Hello!")

#slash-command // change name="" & after async def to change the slash name /latency
@bot.tree.command(name="latency", description="shows the bot latency")
async def latency(interaction: discord.Interaction):
  #ephemeral=True - shows the message to the command sender only
  await interaction.response.send_message(f"`[latency] bot status: {round(bot.latency * 1000)}ms`", ephemeral=True)

#runs the bot
bot.run(TOKEN)
