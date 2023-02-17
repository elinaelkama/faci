import discord

async def joined(member: discord.Member):
	return f'{member.name} joined on {member.joined_at.strftime("%a %d.%m.%Y at %H:%M")}'