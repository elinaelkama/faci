async def memberRemoved(member):
    member.guild.audit_logs()
    return f'{member.name} left the server or has been kicked from the server.'
