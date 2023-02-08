import discord


async def eventDeleted(event: discord.ScheduledEvent):
    return f'Event deleted: **{event.name}**'
