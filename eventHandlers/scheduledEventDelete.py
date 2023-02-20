import discord


async def scheduledEventDelete(event: discord.ScheduledEvent):
    return f'Event deleted: **{event.name}**'
