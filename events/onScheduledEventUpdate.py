import discord


async def eventUpdated(before: discord.ScheduledEvent, after: discord.ScheduledEvent):
    if after.status == discord.EventStatus.active:
        return f"Event **{before.name}** has started"
    if after.status == discord.EventStatus.completed:
        return f"Event **{before.name}** has ended"
    if after.status == discord.EventStatus.cancelled or after.status == discord.EventStatus.canceled:
        return f"Event **{before.name}** has been cancelled"
    updatedName = after.name if after.name != before.name else "event"
    return f"Event **{before.name}** has been **updated**. Please check {updatedName} for more info"
