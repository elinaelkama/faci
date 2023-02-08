import discord


async def memberUnbanned(guild: discord.Guild, user: discord.User):
    return f'{user.name} was unbanned from {guild.name}'
