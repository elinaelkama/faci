import discord


async def memberRemoved(member: discord.Member):
    async for entry in member.guild.audit_logs(limit=1):
        if entry.action != discord.AuditLogAction.kick:
            continue
        if str(entry.target) == f'{member.name}#{member.discriminator}':
            return f'{member.name} was kicked from the server for: {entry.reason}'
        else:
            return f'{member.name} has left the server'
