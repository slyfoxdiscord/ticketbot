from discord import Webhook, RequestsWebhookAdapter
import asyncio
import random
import discord
from discord.ext import commands
import re, time, datetime, sys
import yaml

a = open("config.yaml", 'r')
x = yaml.load(a)
Jchannel = x['JOINS']
Lchannel = x['LEAVES']

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        created = str(guild.created_at.strftime("%#d %B %Y"))
        discord_webhook = Lchannel
        webhook_id = int(re.search(r"\d+", discord_webhook).group())
        webhook_token = re.search(r"(?!.*\/)+(.*)", discord_webhook).group()
        embed = discord.Embed(title = 'Left guild', description = f'Guild name: {guild.name}\nGuild id: {guild.id}\nGuild owner: {guild.owner}\nMembers: {guild.member_count}', color=0xff0000)
        embed.set_footer(text=f"Guild created: {created}")
        embed.set_image(url=str(guild.icon_url))
        webhook = Webhook.partial(webhook_id, webhook_token, adapter=RequestsWebhookAdapter())
        webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        created = str(guild.created_at.strftime("%#d %B %Y"))
        discord_webhook = Jchannel
        webhook_id = int(re.search(r"\d+", discord_webhook).group())
        webhook_token = re.search(r"(?!.*\/)+(.*)", discord_webhook).group()
        embed = discord.Embed(title = 'New guild', description = f'Guild name: {guild.name}\nGuild id: {guild.id}\nGuild owner: {guild.owner}\nMembers: {guild.member_count}', color=0x00ff00)
        embed.set_image(url=str(guild.icon_url))
        embed.set_footer(text=f"Created at {created}")
        webhook = Webhook.partial(webhook_id, webhook_token, adapter=RequestsWebhookAdapter())
        webhook.send(embed=embed)

def setup(bot):
    bot.add_cog(Owner(bot))
