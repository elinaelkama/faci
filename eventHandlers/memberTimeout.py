import discord


async def memberTimeout(before: discord.Member, after: discord.Member):
    return f'{before.name}#{before.discriminator} is on a timeout until {after.timed_out_until.strftime("%H:%M %a %d.%m.%Y")}'
