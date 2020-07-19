import discord
from discord.ext import commands

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ticket(self,ctx):
        arg = f"{ctx.author.name}"
        argplus=arg.replace(" " , "-")
        args = str(ctx.author).replace(' ', '-').replace('#', '_').lower()
        if not discord.utils.get(ctx.guild.text_channels, name=args) == None:
            await ctx.send(f"{ctx.author.mention} You already have a ticket!")
        else:
            overwrites = { ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False), ctx.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True), ctx.author : discord.PermissionOverwrite(send_messages=True, read_messages=True) }
            channel = await ctx.guild.create_text_channel(args, overwrites=overwrites, topic=f"Ticket Owner: {ctx.author}\nTicket Owner ID: {ctx.author.id}\nTicketPro by editid#6714", slowmode_delay=1)
            embed=discord.Embed(title="New ticket!", description=f"Hey {ctx.author.name}, I've created a ticket just for you!\nHere's some info on how to use the reactions!\nReacting with \U0001f3ab = Close the ticket\nReacting with \U000023f1 = Set the slowmode to 0", color=0x00ff00)
            await ctx.send(f"I created a channel for you! ({channel.mention})")
            message = await channel.send(f"@everyone", embed=embed)
            await message.add_reaction('\U0001f3ab')
            await message.add_reaction('\U000023f1')

    @commands.command()
    async def close(self, ctx):
        try:
            if not ctx.channel.topic.endswith("TicketPro by editid#6714"):
                await ctx.send("Sorry, this isn't a ticket, so I can't close it!")
            else:
                try:
                    await ctx.channel.delete(reason=f"Closed by {ctx.author}")
                except:
                    await ctx.send("I couldn't delete this channel, please make sure I have all necessary permissions")
        except Exception as ex:
            await ctx.send(f"Sorry, I encountered an error! If this is repetitive report it to my support server!\nError: `{ex}`")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        user = self.bot.get_user(user.id)
        channel = self.bot.get_channel(reaction.message.channel.id)
        if not user.bot:
            if reaction.emoji == "\U0001f3ab":
                if channel.topic.endswith("TicketPro by editid#6714"):
                    try:
                        await channel.delete(reason=f"Closed.")
                    except:
                        await channel.send("Hey! I'm lacking permissions to delete this channel!")
            elif reaction.emoji == "\U000023f1":
                if channel.topic.endswith("TicketPro by editid#6714"):
                    try:
                        await channel.edit(slowmode_delay=0)
                    except:
                        await channel.send("Hey! I'm lacking permissions to edit the slowmode!")

    @commands.group()
    async def set(self, ctx):
        embed=discord.Embed(title="Set", description="What do you want to set? <:thonk:734511031036149800>", color=0x90caff)
        await ctx.send(embed=embed)

    @set.command()
    async def slowmode(self, ctx, slowmode:int):
        try:
            if ctx.channel.topic.endswith("TicketPro by editid#6714"):
                await ctx.channel.edit(slowmode_delay=slowmode, reason=f"Requested by {ctx.author}")
        except:
            await ctx.send(f"I'm having issues with checking this channel's topic")

def setup(bot):
    bot.add_cog(Tickets(bot))
