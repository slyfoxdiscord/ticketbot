import discord
from discord.ext import commands
import asyncio

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Reload cog loaded")

    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def cgload(self, ctx, *, cog: str):
        try:
            self.bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"loaded `cogs.{cog}`")
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cgunload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(f"cogs.{cog}")
            await ctx.send(f"unloaded `cogs.{cog}`")
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def cgreload(self, ctx, *, cog: str):
        msg = await ctx.send("Processing")
        try:
            self.bot.unload_extension(f"cogs.{cog}")
            await msg.edit(content=f"unloaded `cogs.{cog}`")
            self.bot.load_extension(f"cogs.{cog}")
            await asyncio.sleep(1)
            await msg.edit(content=f"loaded `cogs.{cog}`")
        except Exception as e:
            await asyncio.sleep(1)
            await msg.edit(content=f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await asyncio.sleep(1)
            await msg.edit(content='**`SUCCESS`**')

def setup(bot):
    bot.add_cog(Reload(bot))
