import discord
from discord.ext import commands
import yaml
from PIL import Image, ImageDraw, ImageFont
import io, time, asyncio
from discord import File

a = open("config.yaml", 'r')
x = yaml.load(a)
prefix = x['PREFIX']
bot=commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title = "Missing Required Argument.", colour = discord.Color.dark_red())
        embed.description = (f"`{error.param}`")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BotMissingPermissions):
        permissions = error.missing_perms
        embed = discord.Embed(title = "I Missing Required Permissions.", colour = discord.Color.dark_red())
        embed.description=(f"I don\'t have permissions to do that.\n{permissions}")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title = "Sorry, You can\'t use this Command.", colour = discord.Color.dark_red())
        permissions = error.missing_perms
        embed.description=(f"You Don't have required permissions.\n{permissions}")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(title = "Sorry, I can\'t proceed this command.", colour = discord.Color.dark_red())
        embed.description=(f"{error.original}")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="Cooldown",
        description=f'<:cross:719565512656289822> This command is on cooldown\nTry again in **{round(error.retry_after,2)}** seconds.<:cross:719565512656289822>',color = 0xff0000)
        embed.set_footer(text=f"{ctx.author.name} got stopped by cooldown",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        raise error
    error_channel = bot.get_channel(733066690031517726)
    embed=discord.Embed(title="Error", description=f"Author: {ctx.author}\nAuthor ID: {ctx.author.id}\nServer name: {ctx.guild.id}\nServer ID: {ctx.guild.id}\nError: {error}")
    embed.set_footer(text=f"channel ID: {ctx.channel.id}")
    embed.color=0xff0000
    await error_channel.send(embed=embed)


@bot.command()
async def support(ctx):
    embed=discord.Embed(title="Support server", description="Looks like you need assistance, feel free to join my support server [here](https://discord.gg/CXMpQAB)")
    await ctx.send(embed=embed)
    embed.set_footer(text="We're happy to help!")

@bot.command()
async def ping(ctx):
    start= time.time()
    async with ctx.message.channel.typing():
        end_time = time.time()
        result = end_time - start
        result1 = round(result * 1000)
        apiresult=round(bot.latency*1000)
        embed=discord.Embed(title="Pong!", description=f"My ping is `{result1}ms`\nApi ping is `{apiresult}ms`")
        embed.color=0xff4500
        await asyncio.sleep(0.1)
        await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    embed=discord.Embed(title="Invite me!", description="You can invite me by clicking [here](https://discordapp.com/oauth2/authorize?client_id=732939909026938911&scope=bot&permissions=347216)")
    await ctx.send(embed=embed)

extensions=["tickets","help","info","owner","reload"]
bot.load_extension("jishaku")
for extension in extensions:
    try:
        bot.load_extension(f"cogs.{extension}")
    except Exception as e:
        print(e)

a = open("config.yaml", 'r')
x = yaml.load(a)
token = x['TOKEN']
bot.run(token)
