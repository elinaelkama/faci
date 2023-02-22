import unittest
from unittest.mock import patch
from datetime import datetime
import pytz

import discord
from eventHandlers import inviteCreate, memberBan, memberJoin, memberRemove, memberTimeout, memberUnban, scheduledEventCreate, scheduledEventDelete, scheduledEventUpdate
from test import testHelper

class TestEventHandler(unittest.IsolatedAsyncioTestCase):
	async def testInviteCreate(self):
		invite = testHelper.getInviteMock()
		output = await inviteCreate.inviteCreate(invite)
		self.assertRegex(output, invite.inviter.name)
		self.assertRegex(output, str(invite.inviter.discriminator))
		self.assertRegex(output, invite.id)
		self.assertRegex(output, f'{invite.max_uses} use\(s\)')
		self.assertRegex(output, '1 day and 10 minutes')

	async def testInviteCreateTemporary(self):
		invite = testHelper.getTemporaryInviteMock()
		output = await inviteCreate.inviteCreate(invite)
		self.assertRegex(output, invite.inviter.name)
		self.assertRegex(output, str(invite.inviter.discriminator))
		self.assertRegex(output, 'temporary')
		self.assertRegex(output, invite.id)
		self.assertRegex(output, f'{invite.max_uses} use\(s\)')
		self.assertRegex(output, '1 day, 15 hours and 43 minutes')

	async def testMemberJoin(self):
		member = testHelper.getMemberMock()
		output = await memberJoin.memberJoin(member)
		self.assertRegex(output, member.name)
		self.assertRegex(output, str(member.discriminator))
		self.assertRegex(output, "joined")
		self.assertRegex(output, member.guild.name)

	async def testMemberRemove(self):
		member = testHelper.getRemovedMemberMock()
		output = await memberRemove.memberRemove(member)
		self.assertRegex(output, member.name)
		self.assertRegex(output, str(member.discriminator))
		self.assertRegex(output, "left")		

	async def testMemberRemoveKick(self):
		member = testHelper.getKickedMemberMock()
		output = await memberRemove.memberRemove(member)
		self.assertRegex(output, member.name)
		self.assertRegex(output, str(member.discriminator))
		self.assertRegex(output, "kicked")		
		self.assertRegex(output, "Gallavanting around")		

	async def testMemberTimeout(self):
		before = testHelper.getMemberMock()
		after = testHelper.getMemberMock()
		after.timed_out_until = datetime(2024, 9, 14, 19, 52)
		output = await memberTimeout.memberTimeout(before, after)
		self.assertRegex(output, before.name)
		self.assertRegex(output, str(before.discriminator))
		self.assertRegex(output, "timeout")
		self.assertRegex(output, "19:52")
		self.assertRegex(output, "14.09.2024")

	async def testMemberBan(self):
		user = testHelper.getMemberMock()
		output = await memberBan.memberBan(testHelper.getGuildMock(), user)
		self.assertRegex(output, user.name)
		self.assertRegex(output, str(user.discriminator))
		self.assertRegex(output, "banned")

	async def testMemberUnban(self):
		user = testHelper.getMemberMock()
		output = await memberUnban.memberUnban(testHelper.getGuildMock(), user)
		self.assertRegex(output, user.name)
		self.assertRegex(output, str(user.discriminator))
		self.assertRegex(output, "unbanned")
	
	async def testScheduledEventCreate(self):
		with patch('datetime.datetime') as pachedDatetime:
			pachedDatetime.now.return_value = datetime(2023, 7, 3, 12, 00, 13, 34, pytz.UTC)
			event = testHelper.getScheduledEventMock()
			output1 = await scheduledEventCreate.scheduledEventCreate(event)
			self.assertRegex(output1, event.name)
			self.assertRegex(output1, event.channel)
			self.assertRegex(output1, '22 weeks and 2 days')
			self.assertRegex(output1, '06.12.2023')
			self.assertRegex(output1, '14:30')

			event2 = testHelper.getScheduledEventMock()
			event2.channel = None
			output2 = await scheduledEventCreate.scheduledEventCreate(event2)
			self.assertRegex(output2, event2.location)

	async def testScheduledEventDelete(self):
		event = testHelper.getScheduledEventMock()
		output = await scheduledEventDelete.scheduledEventDelete(event)
		self.assertRegex(output, event.name)
		self.assertRegex(output, 'deleted')

	async def testScheduledEventUpdate(self):
		before = testHelper.getScheduledEventMock()

		after1 = testHelper.getScheduledEventMock()
		after1.status = discord.EventStatus.active
		output1 = await scheduledEventUpdate.scheduledEventUpdate(before, after1)
		self.assertRegex(output1, before.name)
		self.assertRegex(output1, 'started')

		after2 = testHelper.getScheduledEventMock()
		after2.status = discord.EventStatus.ended
		output2 = await scheduledEventUpdate.scheduledEventUpdate(before, after2)
		self.assertRegex(output2, before.name)
		self.assertRegex(output2, 'ended')

		after3 = testHelper.getScheduledEventMock()
		after3.status = discord.EventStatus.canceled
		output3 = await scheduledEventUpdate.scheduledEventUpdate(before, after3)
		self.assertRegex(output3, before.name)
		self.assertRegex(output3, 'cancelled')

		after4 = testHelper.getScheduledEventMock()
		after4.name = "Pancake Day Eating Contest"
		output4 = await scheduledEventUpdate.scheduledEventUpdate(before, after4)
		self.assertRegex(output4, before.name)
		self.assertRegex(output4, after4.name)
		self.assertRegex(output4, 'updated')
