import discord


async def memberJoined(member: discord.Member):
    return f'{member.name}#{member.discriminator} joined {member.guild}'
