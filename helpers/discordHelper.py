import discord


def listTextChannels(guild: discord.Guild | None):
    if guild is None:
        return
    list = []
    for channel in guild.text_channels:
        if str(channel.type) != "text":
            continue
        list.append(channel.name)
    return "\n".join(list)


def getEventChannel(guild: discord.Guild | None):
    if guild is None:
        return
    for channel in guild.text_channels:
        if str(channel.type) == "text" and channel.name.startswith("event"):
            return channel
    return None


def getAuditChannel(guild: discord.Guild | None):
    if guild is None:
        return
    for channel in guild.text_channels:
        if str(channel.type) == "text" and channel.name.startswith("audit"):
            return channel
    return None
