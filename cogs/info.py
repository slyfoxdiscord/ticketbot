import discord
from discord.ext import commands
import asyncio

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="info")
    @commands.guild_only()
    async def _info(self, ctx):
        embed=discord.Embed(title="Info", description=f"I heard you needed some info! React with <:redx:724951866412367882> to remove this embed.", color=0x90caff)
        embed.add_field(name=f"Data stored:", value="None!", inline=False)
        embed.add_field(name=f"Fact:", value="All embeds I send are removeable via a reaction!", inline=False)
        embed.add_field(name=f"Required permissions:", value="Send messages, Manage channels, Read messages, Add reactions\nIf I am missing one of these permissions, I will throw a 503 error", inline=False)
        embed.add_field(name=f"Other causes of 503 error:", value="503 is quite a common error, if you wish to report one, head over to my support server!", inline=False)
        message1 = await ctx.send(embed=embed)
        await message1.add_reaction('<:redx:724951866412367882>')
        def check1(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == "<:redx:724951866412367882>"

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=120.0, check=check1)
        except asyncio.TimeoutError:
            return
        else:
            await message1.delete()


def setup(bot):
    bot.add_cog(Info(bot))
