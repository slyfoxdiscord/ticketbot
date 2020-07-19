import discord
from discord.ext import commands

class Links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        embed=discord.Embed(title="Invite me!", description="You can invite me by clicking [here](https://discordapp.com/oauth2/authorize?client_id=732939909026938911&scope=bot&permissions=347216)")
        await ctx.send(embed=embed)

    @commands.command()
    async def support(self, ctx):
        embed=discord.Embed(title="Support server", description="Looks like you need assistance, feel free to join my support server [here](https://discord.gg/CXMpQAB)")

def setup(bot):
    bot.add_cog(Links(bot))
