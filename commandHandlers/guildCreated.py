import discord
from datetime import datetime, timedelta
import humanfriendly

async def guildCreated(guild: discord.Guild):
	timezone = guild.created_at.tzinfo
	diff: timedelta = datetime.now(timezone) - guild.created_at
	return f'{guild.name} was created on {guild.created_at.strftime("%d.%m.%Y")} UTC/GMT\nServer has been in existence for {humanfriendly.format_timespan(diff)}'