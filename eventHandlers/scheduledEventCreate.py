import discord
import datetime
import humanfriendly

async def scheduledEventCreate(event: discord.ScheduledEvent):
    timezone = event.start_time.tzinfo
    diff: datetime.timedelta = event.start_time - datetime.datetime.now(timezone)
    arrangement = event.channel
    if event.channel is None:
        arrangement = event.location
    return f'Event created: **{event.name}** in {arrangement} on {event.start_time.strftime("%a %d.%m.%Y at %H:%M")} UTC/GMT\nEvent starts in {humanfriendly.format_timespan(diff, max_units=2)}'
