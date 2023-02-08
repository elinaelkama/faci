import discord


async def memberBanned(guild: discord.Guild, user: discord.User):
    return f'{user.name} was banned from {guild.name}'
