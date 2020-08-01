import discord
from discord.ext import commands
import asyncio

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def help(self, ctx):
        embed=discord.Embed(title="Help", description=f"If you want me to delete this embed, react with <:binDEFAULT:734381816714231888>!\nIf you want some more information/want to see my required permissions, please do `{ctx.prefix}info`", color=0x90caff)
        embed.add_field(name=f"{ctx.prefix}ticket", value="Opens a ticket, it will mention you, if you don't see it, look for a channel with this format: <your name>_<discriminator>", inline=False)
        embed.add_field(name=f"{ctx.prefix}help", value="Shows this menu!", inline=False)
        embed.add_field(name=f"{ctx.prefix}logs #channel", value="set the channel where ticket logs go!", inline=False)
        embed.add_field(name=f"{ctx.prefix}close", value="close a ticket!", inline=False)
        embed.add_field(name=f"{ctx.prefix}test", value="sends a message to the channel set via t.logs", inline=False)
        embed.set_footer(text=f"Check out my support server too!")
        message2 = await ctx.send(embed=embed)
        await message2.add_reaction('<:binDEFAULT:734381816714231888>')
        def check2(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == "<:binDEFAULT:734381816714231888>"

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=120.0, check=check2)
        except asyncio.TimeoutError:
            return
        else:
            await message2.delete()

    #@help.command(aliases=["polish"])
    #@commands.guild_only()
    #async def pl(self, ctx):
     #   embed=discord.Embed(title="Help", description=f"Jeśli chcesz usunąć tą wiadomość, użyj emotki <:binPL:734381894518702110>!\nJeśli chcesz dowiedzieć się więcej/zobaczyć permisji jakich wymagam wpisz `t.info`", color=0x90caff)
      #  embed.add_field(name=f"{ctx.prefix}ticket", value="Otwiera zgłoszenie, zostaniesz zaczepiony/a, jeśli go nie widzisz poszukaj kanału o nazwie: <Twój nick>_<Twój tag discord>", inline=False)
       # embed.add_field(name=f"{ctx.prefix}help", value="Pokazuje to menu", inline=False)
        #embed.set_footer(text="Translated by MrTalon63#1180")
        #message2 = await ctx.send(embed=embed)
        #await message2.add_reaction('<:binPL:734381894518702110>')
        #def check2(reaction, user):
        #    return user == ctx.message.author and str(reaction.emoji) == "<:binPL:734381894518702110>"

        #try:
        #    reaction, user = await self.bot.wait_for('reaction_add', timeout=120.0, check=check2)
        #except asyncio.TimeoutError:
        #    return
        #else:
        #    await message2.delete()

    #@help.command(aliases=["english"])
    #@commands.guild_only()
    #async def en(self, ctx):
    #    embed=discord.Embed(title="Help", description=f"If you want me to delete this embed, react with <:binEN:734381862260310146>!\nIf you want some more information/want to see my required permissions, please do `{ctx.prefix}info`", color=0x90caff)
    #    embed.add_field(name=f"{ctx.prefix}ticket", value="Opens a ticket, it will mention you, if you don't see it, look for a channel with this format: <your name>_<discriminator>", inline=False)
    #    embed.add_field(name=f"{ctx.prefix}help", value="Shows this menu!", inline=False)
    #    message2 = await ctx.send(embed=embed)
    #    await message2.add_reaction('<:binEN:734381862260310146>')
    #    def check2(reaction, user):
    #        return user == ctx.message.author and str(reaction.emoji) == "<:binEN:734381862260310146>"

     #   try:
      #      reaction, user = await self.bot.wait_for('reaction_add', timeout=120.0, check=check2)
       # except asyncio.TimeoutError:
        #    return
        #else:
         #   await message2.delete()

    #@help.command()
    #@commands.guild_only()
    #async def languages(self, ctx):
    #    embed=discord.Embed(title="Languages", description=f"Here are my supported languages for the help menu!", color=0x90caff)
     #   embed.add_field(name="pl", value="Polish", inline=False)
      #  embed.add_field(name="en", value="English", inline=False)
       # message2 = await ctx.send(embed=embed)
        #await message2.add_reaction('<:binLANGS:734382331191754773>')
    #    def check2(reaction, user):
     #       return user == ctx.message.author and str(reaction.emoji) == "<:binLANGS:734382331191754773>"
#
 #       try:
  #          reaction, user = await self.bot.wait_for('reaction_add', timeout=120.0, check=check2)
   #     except asyncio.TimeoutError:
    #        return
     #   else:
      #      await message2.delete()

def setup(bot):
    bot.add_cog(Help(bot))
