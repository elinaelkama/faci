import discord
from datetime import datetime, timedelta
import humanfriendly

async def scheduledEventCreate(event: discord.ScheduledEvent):
    timezone = event.start_time.tzinfo
    diff: timedelta = event.start_time - datetime.now(timezone)
    return f'Event created: **{event.name}** in {event.channel} on {event.start_time.strftime("%a %d.%m.%Y at %H:%M")} UTC/GMT\nEvent starts in {humanfriendly.format_timespan(diff, max_units=2)}'
