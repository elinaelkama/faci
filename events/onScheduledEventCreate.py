import discord


async def eventCreated(event: discord.ScheduledEvent):
    return f'Event created: **{event.name}** in {event.channel} at {event.start_time} UTC/GMT'
