import discord
import humanfriendly
from datetime import timedelta


async def inviteCreated(invite: discord.Invite):
	if invite.temporary == True:
		return f'{invite.inviter}#{invite.inviter.discriminator} created a temporary invite.'
	#age = await time()
	delta = timedelta(seconds = invite.max_age)
	return f'{invite.inviter}#{invite.inviter.discriminator} created an invite {invite.id}, for {invite.max_uses if invite.max_uses != 0 else "unlimited"} use(s) that expires in {humanfriendly.format_timespan(delta)}'
