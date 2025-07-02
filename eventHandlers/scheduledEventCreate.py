import discord
import datetime
import humanfriendly


async def scheduledEventCreate(event: discord.ScheduledEvent):
    timezone = datetime.timezone.utc
    starttime = event.start_time.astimezone(timezone)
    diff: datetime.timedelta = starttime - datetime.datetime.now(timezone)
    arrangement = event.channel
    if event.channel is None:
        arrangement = event.location
    return f'Event created: **{event.name}** in {arrangement} on {starttime.strftime("%a %d.%m.%Y at %H:%M")} UTC/GMT\nEvent starts in {humanfriendly.format_timespan(diff, max_units=2)}'
