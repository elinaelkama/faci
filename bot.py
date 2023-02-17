from ast import arg
import discord
from discord.ext import commands
from decouple import config
from commands import randomChoice
from events import onScheduledEventCreate, onScheduledEventUpdate, onScheduledEventDelete, onMemberJoin, onMemberBan, onMemberRemove, onMemberUnban, onInviteCreate, onMemberTimeout
from helpers import getAuditChannel, getEventChannel, listTextChannels

DISCORD_TOKEN = config('DISCORD_TOKEN', cast=str)

"""required permissions for bot:
    manage_channels
    view_audit_log
#required intents:
    Intents.invites
    Intents.members
    Intents.bans
    Intents.guild_scheduled_events"""
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
intents.members = True


# commands and events
@bot.command()
async def choose(ctx: commands.Context, *args: str):
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

"""only handles timeout"""
@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    channel = getAuditChannel(before.guild)
    if after.timed_out_until is not None and channel is not None:
        await channel.send(await onMemberTimeout.memberTimeout(before,after))

@bot.event
async def on_invite_create(invite):
    channel = getAuditChannel(invite.guild)
    if channel is not None:
        await channel.send(await onInviteCreate.inviteCreated(invite))

@bot.event
async def on_ready():
    pass

bot.run(str(DISCORD_TOKEN))

# Sends a direct message to the person who joined
# bot.add_listener(event.event)
"""@bot.event
async def on_member_join(member):
    await member.send(f"Welcome {member.name} to {member.guild}!")"""
