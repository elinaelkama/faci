import discord


async def memberUnban(guild: discord.Guild, user: discord.User):
    return f'{user.name}#{user.discriminator} was unbanned from {guild.name}'
