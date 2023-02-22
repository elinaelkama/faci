import discord


async def memberBan(guild: discord.Guild, user: discord.User):
    return f'{user.name}#{user.discriminator} was banned'
