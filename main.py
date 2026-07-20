import discord
from discord.ext import commands
import decouple
from commandHandlers import getFunHoliday, randomChoice, userJoined, guildCreated, rollDie
from eventHandlers import (
    inviteCreate,
    memberBan,
    memberJoin,
    memberRemove,
    memberTimeout,
    memberUnban,
    scheduledEventCreate,
    scheduledEventDelete,
    scheduledEventUpdate,
)
import healthCheck.server
from helpers.discordHelper import getAuditChannel, getEventChannel, listTextChannels
import datetime


DISCORD_TOKEN = decouple.config("DISCORD_TOKEN", cast=str)

intents = discord.Intents.default()
intents.members = True
intents.invites = True
intents.bans = True
intents.guild_scheduled_events = True

class SlashBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=".", intents=intents)

    async def setup_hook(self) -> None:
        # Global sync makes slash commands available in every guild the bot is in.
        await self.tree.sync()

bot = SlashBot()

@bot.tree.command(name="ping", description="...")
async def _ping(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("pong")


@bot.tree.command(name="choose", description="Choose from a list of options")
async def _choose(interaction: discord.Interaction, choices: str) -> None:
    await interaction.response.send_message(
        await randomChoice.randomChoice(choices)
    )


@bot.tree.command(name="joined", description="Get the date you joined the server")
async def _joined(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(
        await userJoined.userJoined(interaction.user)
    )


@bot.tree.command(name="created", description="Get the date the server was created")
async def _created(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(
        await guildCreated.guildCreated(interaction.guild)
    )


@bot.tree.command(name="list", description="List all text channels in the server")
async def _list(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(
        listTextChannels(interaction.guild)
    )


@bot.tree.command(name="holiday", description="Get a fun holiday for a given date")
async def _holiday(interaction: discord.Interaction, date: str = None) -> None:
    await interaction.response.send_message(
        await getFunHoliday.getFunHoliday(date) if date else await getFunHoliday.getFunHoliday()
    )

@bot.tree.command(name="roll", description="Roll a die")
async def _roll(interaction: discord.Interaction, args: str) -> None:
    await interaction.response.send_message(await rollDie.rollDie(args))

@bot.event
async def on_scheduled_event_create(event: discord.ScheduledEvent):
    channel = getEventChannel(event.guild)
    if channel is not None:
        await channel.send(await scheduledEventCreate.scheduledEventCreate(event))


@bot.event
async def on_scheduled_event_delete(event: discord.ScheduledEvent):
    channel = getEventChannel(event.guild)
    if channel is not None:
        await channel.send(await scheduledEventDelete.scheduledEventDelete(event))


@bot.event
async def on_scheduled_event_update(
    before: discord.ScheduledEvent, after: discord.ScheduledEvent
):
    channel = getEventChannel(after.guild)
    if channel is not None:
        await channel.send(
            await scheduledEventUpdate.scheduledEventUpdate(before, after)
        )


@bot.event
async def on_member_join(member: discord.Member):
    channel = getAuditChannel(member.guild)
    if channel is not None:
        await channel.send(await memberJoin.memberJoin(member))


@bot.event
async def on_member_remove(member: discord.Member):
    channel = getAuditChannel(member.guild)
    if channel is not None:
        await channel.send(await memberRemove.memberRemove(member))


@bot.event
async def on_member_ban(guild: discord.Guild, user: discord.User):
    channel = getAuditChannel(guild)
    if channel is not None:
        await channel.send(await memberBan.memberBan(guild, user))


@bot.event
async def on_member_unban(guild: discord.Guild, user: discord.User):
    channel = getAuditChannel(guild)
    if channel is not None:
        await channel.send(await memberUnban.memberUnban(guild, user))


# only handles timeout
@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    channel = getAuditChannel(before.guild)
    now = datetime.datetime.now()
    if after.timed_out_until is not None and after.timed_out_until > now and channel is not None:
        await channel.send(await memberTimeout.memberTimeout(before, after))


@bot.event
async def on_invite_create(invite: discord.Invite):
    channel = getAuditChannel(invite.guild)
    if channel is not None:
        await channel.send(await inviteCreate.inviteCreate(invite))


@bot.event
async def on_ready():
    pass


healthCheck.server.start()

bot.run(str(DISCORD_TOKEN))

healthCheck.server.stop()
