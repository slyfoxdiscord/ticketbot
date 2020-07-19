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
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
            }
            channel = await ctx.guild.create_text_channel(args, overwrites=overwrites, topic=f"Ticket Owner: {ctx.author}\nTicket Owner ID: {ctx.author.id}\nTicket bot by editid#6714")
            embed=discord.Embed(title="New ticket!", description=f"Hey {ctx.author.name}, I've created a ticket just for you!\nHere's some info on how to close the ticket!\nReacting with \U0001f3ab = Close the ticket", color=0x00ff00)
            await channel.set_permissions(ctx.author, read_messages=True, send_messages=True)
            await ctx.send(f"I created a channel for you! ({channel.mention})")
            message = await channel.send(f"{ctx.author.mention}", embed=embed)
            await message.add_reaction('\U0001f3ab')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        user = self.bot.get_user(user.id)
        channel = self.bot.get_channel(reaction.message.channel.id)
        if not user.bot:
            if reaction.emoji == "\U0001f3ab":
                try:
                    await channel.delete(reason=f"Closed.")
                except:
                    await channel.send("Hey! I'm lacking permissions to delete this channel!")

def setup(bot):
    bot.add_cog(Tickets(bot))
