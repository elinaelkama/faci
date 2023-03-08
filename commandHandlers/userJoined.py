import discord
import datetime
import humanfriendly


async def userJoined(member: discord.Member):
    timezone = member.joined_at.tzinfo
    diff: datetime.timedelta = datetime.datetime.now(
        timezone) - member.joined_at
    return f'{member.name}, you joined on {member.joined_at.strftime("%a %d.%m.%Y at %H:%M")} UTC/GMT\nYou have been on the server for {humanfriendly.format_timespan(diff)}'
