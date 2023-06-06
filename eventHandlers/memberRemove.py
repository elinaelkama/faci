import discord


async def memberRemove(member: discord.Member):
    async for entry in member.guild.audit_logs(limit=1):
        if entry.action == discord.AuditLogAction.kick:
            if entry.reason == None:
                return f'{member.name}#{member.discriminator} was kicked from the server'
            return f'{member.name}#{member.discriminator} was kicked from the server for: {entry.reason}'
        if entry.action == discord.AuditLogAction.ban:
            if entry.reason == None:
                return
            return f'They were banned from the server for: {entry.reason}'
    return f'{member.name}#{member.discriminator} has left the server'
