import discord
import datetime
import humanfriendly


async def userJoined(member: discord.Member):
    joined = member.joined_at.astimezone(datetime.timezone.utc)
    timezone = datetime.timezone.utc
    diff: datetime.timedelta = datetime.datetime.now(
        timezone) - member.joined_at
    return f'{member.name}, you joined on {joined.strftime("%a %d.%m.%Y")}\nYou have been on the server for {humanfriendly.format_timespan(diff)}'
