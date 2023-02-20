import discord


async def memberJoin(member: discord.Member):
    return f'{member.name}#{member.discriminator} joined {member.guild}'
