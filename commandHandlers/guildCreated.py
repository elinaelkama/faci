import discord
import datetime
import humanfriendly


async def guildCreated(guild: discord.Guild):
    created = guild.created_at.astimezone(datetime.timezone.utc)
    timezone = datetime.timezone.utc
    diff: datetime.timedelta = datetime.datetime.now(
        timezone) - guild.created_at
    return f'{guild.name} was created on {created.strftime("%d.%m.%Y")}\nServer has been in existence for {humanfriendly.format_timespan(diff)}'
