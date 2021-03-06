import discord, sqlite3, datetime
from discord.ext import commands

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
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
            conn = sqlite3.connect('mybot.db')
            cur = conn.cursor()
            cur.execute("Select channelID from WelcomeChannel where guildID = ?",(ctx.guild.id,))
            check = cur.fetchone()
            conn.close()
            embed=discord.Embed(title=f"Ticket opened!", description=f"Ticket opened by {ctx.author} ({ctx.author.mention} **|** {ctx.author.id})", color=0x00ff00, timestamp=datetime.datetime.utcnow())
            if check is None:
                pass
            else:
                try:
                    channel = self.bot.get_channel(check[0])
                    await channel.send(embed=embed)
                except:
                    pass

    @commands.command()
    @commands.guild_only()
    async def add(self, ctx, member:discord.Member):
        if not ctx.channel.topic.endswith("TicketPro by editid#6714"):
            await ctx.send("Sorry, this isn't a ticket, so I can't add a user to it!")
        else:
            overwrites = { member: discord.PermissionOverwrite(read_messages=True), member: discord.PermissionOverwrite(send_messages=True) }
            embed=discord.Embed(title="You were added to this ticket!", description=f"Hey {member.name}! You've been added to this ticket by {ctx.author}!", color=0x00ff00, timestamp=datetime.datetime.utcnow())
            await ctx.channel.set_permissions(member, read_messages=True, send_messages=True)
            await ctx.channel.send(f"{member.mention}", embed=embed)

    @commands.command()
    @commands.guild_only()
    async def close(self, ctx):
        try:
            if not ctx.channel.topic.endswith("TicketPro by editid#6714"):
                await ctx.send("Sorry, this isn't a ticket, so I can't close it!")
            else:
                try:
                    await ctx.channel.delete(reason=f"Closed by {ctx.author}")
                    conn = sqlite3.connect('mybot.db')
                    cur = conn.cursor()
                    cur.execute("Select channelID from WelcomeChannel where guildID = ?",(ctx.guild.id,))
                    check = cur.fetchone()
                    conn.close()
                    embed=discord.Embed(title=f"Ticket closed!", description=f"Ticket closed by {ctx.author} ({ctx.author.mention} **|** {ctx.author.id})", color=0xff0000, timestamp=datetime.datetime.utcnow())
                    if check is None:
                        pass
                    else:
                        try:
                            channel = self.bot.get_channel(check[0])
                            await channel.send(embed=embed)
                        except:
                            pass
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
                        conn = sqlite3.connect('mybot.db')
                        cur = conn.cursor()
                        cur.execute("Select channelID from WelcomeChannel where guildID = ?",(reaction.message.guild.id,))
                        check = cur.fetchone()
                        conn.close()
                        embed=discord.Embed(title=f"Ticket closed!", description=f"Ticket closed by {user} ({user.mention} **|** {user.id})", color=0xff0000, timestamp=datetime.datetime.utcnow())
                        if check is None:
                            pass
                        else:
                            try:
                                if not user.bot:
                                    if reaction.emoji == "\U0001f3ab":
                                        channel = self.bot.get_channel(check[0])
                                        await channel.send(embed=embed)
                                    else:
                                        pass
                                else:
                                    pass
                            except:
                                pass
                    except:
                        await channel.send("Hey! I'm lacking permissions to delete this channel!")
            elif reaction.emoji == "\U000023f1":
                if channel.topic.endswith("TicketPro by editid#6714"):
                    try:
                        await channel.edit(slowmode_delay=0)
                    except:
                        await channel.send("Hey! I'm lacking permissions to edit the slowmode!")

    @commands.group(invoke_without_command=True)
    @commands.guild_only()
    async def set(self, ctx):
        embed=discord.Embed(title="Set", description="What do you want to set? <:thonk:734511031036149800>", color=0x90caff)
        await ctx.send(embed=embed)

    @set.command()
    @commands.guild_only()
    async def slowmode(self, ctx, cooldown:int = 0):
        try:
            if ctx.channel.topic.endswith("TicketPro by editid#6714"):
                try:
                    await ctx.channel.edit(reason=f"Requested by {ctx.author}", slowmode_delay=cooldown)
                    await ctx.message.add_reaction('\U0001f44c')
                except Exception as e:
                    raise e
            else:
                await ctx.send("This isn't a ticket!")
        except Exception as e:
            await ctx.send(f"I'm having issues with checking this channel's topic")
            raise e

def setup(bot):
    bot.add_cog(Logs(bot))
