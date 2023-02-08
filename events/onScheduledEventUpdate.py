async def eventUpdated(before, after):
    updatedName = after.name if after.name != before.name else "event"
    return f"Event **{before.name}** has been **updated**. Please check {updatedName} for more info."
