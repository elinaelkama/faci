async def eventCreated(event):
    return f'Event created: **{event.name}** in {event.channel} at {event.start_time} UTC/GMT'
