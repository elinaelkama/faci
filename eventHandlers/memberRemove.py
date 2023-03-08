import discord


async def memberRemove(member: discord.Member):
    async for entry in member.guild.audit_logs(limit=1):
        if entry.action == discord.AuditLogAction.kick:
            return f'{member.name}#{member.discriminator} was kicked from the server for: {entry.reason}'
    return f'{member.name}#{member.discriminator} has left the server'
