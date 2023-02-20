import discord

async def scheduledEventCreate(event: discord.ScheduledEvent):
    return f'Event created: **{event.name}** in {event.channel} on {event.start_time.strftime("%a %d.%m.%Y at %H:%M")} UTC/GMT'
