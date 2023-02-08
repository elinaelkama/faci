import discord


async def memberJoined(member: discord.Member):
    return f'{member.name} joined {member.guild}'
