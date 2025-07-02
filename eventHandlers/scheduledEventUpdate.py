import discord


async def scheduledEventUpdate(
    before: discord.ScheduledEvent, after: discord.ScheduledEvent
):
    match after.status:
        case discord.EventStatus.active:
            return f"Event **{before.name}** has started"
        case discord.EventStatus.ended | discord.EventStatus.completed:
            return f"Event **{before.name}** has ended"
        case discord.EventStatus.cancelled | discord.EventStatus.canceled:
            return f"Event **{before.name}** has been cancelled"
    updatedName = after.name if after.name != before.name else "event"
    return f"Event **{before.name}** has been **updated**. Please check {updatedName} for more info"
