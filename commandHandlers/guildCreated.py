import discord
import datetime
import humanfriendly


async def guildCreated(guild: discord.Guild):
    timezone = guild.created_at.astimezone(datetime.timezone.utc)
    diff: datetime.timedelta = datetime.datetime.now(
        timezone) - guild.created_at
    return f'{guild.name} was created on {guild.created_at.strftime("%d.%m.%Y")}\nServer has been in existence for {humanfriendly.format_timespan(diff)}'
