import discord
import humanfriendly
from datetime import timedelta


async def inviteCreate(invite: discord.Invite):
    delta = timedelta(seconds=invite.max_age)
    if invite.temporary == True:
        return f'{invite.inviter.name}#{invite.inviter.discriminator} created a temporary invite {invite.id}, for {invite.max_uses if invite.max_uses != 0 else "unlimited"} use(s) that expires in {humanfriendly.format_timespan(delta)}'
    return f'{invite.inviter.name}#{invite.inviter.discriminator} created an invite {invite.id}, for {invite.max_uses if invite.max_uses != 0 else "unlimited"} use(s) that expires in {humanfriendly.format_timespan(delta)}'
