import discord
from datetime import datetime, timedelta
import humanfriendly

async def created(guild: discord.Guild):
	timezone = guild.created_at.tzinfo
	diff: timedelta = datetime.now(timezone) - guild.created_at
	return f'{guild.name} was created on {guild.created_at.strftime("%a %d.%m.%Y at %H:%M")} UTC/GMT\nServer has been in existence for {humanfriendly.format_timespan(diff)}'