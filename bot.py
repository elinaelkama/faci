import discord
from discord.ext import commands
from decouple import config
from commands import randomChoice
from events import onScheduledEventCreate, onScheduledEventUpdate, onScheduledEventDelete, onMemberJoin, onMemberBan, onMemberRemove, onMemberUnban
from helpers import getAuditChannel, getEventChannel, listTextChannels

DISCORD_TOKEN = config('DISCORD_TOKEN', cast=str)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
intents.members = True


# commands and events
@bot.command()
async def choose(ctx: commands.Context, *args: list):
    await ctx.send(await randomChoice.randomChoice(*args))


@bot.command()
async def list(ctx: commands.Context):
    await ctx.send(listTextChannels(ctx.guild))


@bot.event
async def on_scheduled_event_create(event: discord.ScheduledEvent):
    channel = getEventChannel(event.guild)
    if channel is not None:
        await channel.send(await onScheduledEventCreate.eventCreated(event))


@bot.event
async def on_scheduled_event_delete(event: discord.ScheduledEvent):
    channel = getEventChannel(event.guild)
    if channel is not None:
        await channel.send(await onScheduledEventDelete.eventDeleted(event))


@bot.event
async def on_scheduled_event_update(before: discord.ScheduledEvent, after: discord.ScheduledEvent):
    channel = getEventChannel(after.guild)
    if channel is not None:
        await channel.send(await onScheduledEventUpdate.eventUpdated(before, after))


@bot.event
async def on_member_join(member: discord.Member):
    channel = getAuditChannel(member.guild)
    if channel is not None:
        await channel.send(await onMemberJoin.memberJoined(member))

# 2 options on_raw_member_remove and on_member_remove


@bot.event
async def on_member_remove(member: discord.Member):
    channel = getAuditChannel(member.guild)
    if channel is not None:
        await channel.send(await onMemberRemove.memberRemoved(member))


@bot.event
async def on_member_ban(guild: discord.Guild, user: discord.User):
    channel = getAuditChannel(guild)
    if channel is not None:
        await channel.send(await onMemberBan.memberBanned(guild, user))


@bot.event
async def on_member_unban(guild: discord.Guild, user: discord.User):
    channel = getAuditChannel(guild)
    if channel is not None:
        await channel.send(await onMemberUnban.memberUnbanned(guild, user))


@bot.event
async def on_ready():
    pass

bot.run(str(DISCORD_TOKEN))

# Sends a direct message to the person who joined
# bot.add_listener(event.event)
"""@bot.event
async def on_member_join(member):
    await member.send(f"Welcome {member.name} to {member.guild}!")"""
