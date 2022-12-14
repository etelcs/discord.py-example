import discord
from discord.ext import commands

class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="fun"))

    @commands.command()
    async def status(self, ctx, message : str):
        if len(message) < 10:
            await ctx.send(f"`[status] changed status msg to: {message}`", delete_after=30)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=message))
        else:
            await ctx.send("`[status] limit of 10 chars exceeded!`", delete_after=12)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(Ready(bot))