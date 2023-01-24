import asyncio
import json
import discord
import requests
import random
from discord.ext import commands
from decouple import config
from commands import randomChoice
from events import onScheduledEventCreate, onScheduledEventUpdate
from helpers import getAuditChannel, getEventChannel, listTextChannels

DISCORD_TOKEN = config('DISCORD_TOKEN', cast=str)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
intents.members = True


#commands and events
@bot.command()
async def choose(ctx, *args):
    await ctx.send(await randomChoice.randomChoice(*args))

@bot.command()
async def list(ctx):
    await ctx.send(listTextChannels(bot))

@bot.event
async def on_scheduled_event_create(event):
    channel = getEventChannel(bot)
    if channel is not None:
        await channel.send(await onScheduledEventCreate.eventCreated(event))

@bot.event
async def on_scheduled_event_update(before, after):
    channel = getEventChannel(bot)
    if channel is not None:
        await channel.send(await onScheduledEventUpdate.eventUpdated(before, after))

@bot.event
async def on_ready():
    pass

bot.run(DISCORD_TOKEN)

#Sends a direct message to the person who joined
#bot.add_listener(event.event)
"""@bot.event
async def on_member_join(member):
    await member.send(f"Welcome {member.name} to {member.guild}!")"""