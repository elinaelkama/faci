import unittest
from unittest.mock import patch
from datetime import datetime
import pytz

import discord
from eventHandlers import inviteCreate, memberBan, memberJoin, memberRemove, memberTimeout, memberUnban, scheduledEventCreate, scheduledEventDelete, scheduledEventUpdate
from helpers import testHelper

class TestEventHandler(unittest.IsolatedAsyncioTestCase):
	async def testInviteCreate(self):
		output = await inviteCreate.inviteCreate(testHelper.getInviteMock())
		self.assertRegex(output, 'huuhaakettu#2347')
		self.assertRegex(output, 'abcDEF7')
		self.assertRegex(output, '5 use\(s\)')
		self.assertRegex(output, '1 day and 10 minutes')

	async def testInviteCreateTemporary(self):
		output = await inviteCreate.inviteCreate(testHelper.getTemporaryInviteMock())
		self.assertRegex(output, 'huuhaakettu#2347')
		self.assertRegex(output, 'temporary')
		self.assertRegex(output, 'abcDEF7')
		self.assertRegex(output, '5 use\(s\)')
		self.assertRegex(output, '1 day and 10 minutes')

	async def testMemberJoin(self):
		output = await memberJoin.memberJoin(testHelper.getMemberMock())
		self.assertRegex(output, 'huuhaakettu#2347')
		self.assertRegex(output, "joined")
		self.assertRegex(output, "Murder Mittens Inc")

	async def testMemberRemove(self):
		output = await memberRemove.memberRemove(testHelper.getRemovedMemberMock())
		self.assertRegex(output, "huuhaakettu#2347")		
		self.assertRegex(output, "left")		

	async def testMemberRemoveKick(self):
		output = await memberRemove.memberRemove(testHelper.getKickedMemberMock())
		self.assertRegex(output, "huuhaakettu#2347")		
		self.assertRegex(output, "kicked")		
		self.assertRegex(output, "Gallavanting around")		

	async def testMemberTimeout(self):
		before = testHelper.getMemberMock()
		after = testHelper.getMemberMock()
		after.timed_out_until = datetime(2024, 9, 14, 19, 52)
		output = await memberTimeout.memberTimeout(before, after)
		self.assertRegex(output, "huuhaakettu#2347")
		self.assertRegex(output, "timeout")
		self.assertRegex(output, "19:52")
		self.assertRegex(output, "14.09.2024")

	async def testMemberBan(self):
		output = await memberBan.memberBan(testHelper.getGuildMock(), testHelper.getMemberMock())
		self.assertRegex(output, "huuhaakettu#2347")
		self.assertRegex(output, "banned")

	async def testMemberUnban(self):
		output = await memberUnban.memberUnban(testHelper.getGuildMock(), testHelper.getMemberMock())
		self.assertRegex(output, "huuhaakettu#2347")
		self.assertRegex(output, "unbanned")
	
	async def testScheduledEventCreate(self):
		with patch('datetime.datetime') as pachedDatetime:
			pachedDatetime.now.return_value = datetime(2023, 7, 3, 12, 00, 13, 34, pytz.UTC)
			event = testHelper.getScheduledEventMock()
			output1 = await scheduledEventCreate.scheduledEventCreate(event)
			self.assertRegex(output1, 'Independence Day Celebrations')
			self.assertRegex(output1, 'General')
			self.assertRegex(output1, '22 weeks and 2 days')
			self.assertRegex(output1, '06.12.2023')
			self.assertRegex(output1, '14:30')

			event2 = testHelper.getScheduledEventMock()
			event2.channel = None
			output2 = await scheduledEventCreate.scheduledEventCreate(event2)
			self.assertRegex(output2, 'Helsinki')

	async def testScheduledEventDelete(self):
		output = await scheduledEventDelete.scheduledEventDelete(testHelper.getScheduledEventMock())
		self.assertRegex(output, 'Independence Day Celebrations')
		self.assertRegex(output, 'deleted')

	async def testScheduledEventUpdate(self):
		after1 = testHelper.getScheduledEventMock()
		after1.status = discord.EventStatus.active
		output1 = await scheduledEventUpdate.scheduledEventUpdate(testHelper.getScheduledEventMock(), after1)
		self.assertRegex(output1, 'Independence Day Celebrations')
		self.assertRegex(output1, 'started')

		after2 = testHelper.getScheduledEventMock()
		after2.status = discord.EventStatus.ended
		output2 = await scheduledEventUpdate.scheduledEventUpdate(testHelper.getScheduledEventMock(), after2)
		self.assertRegex(output2, 'Independence Day Celebrations')
		self.assertRegex(output2, 'ended')

		after3 = testHelper.getScheduledEventMock()
		after3.status = discord.EventStatus.canceled
		output3 = await scheduledEventUpdate.scheduledEventUpdate(testHelper.getScheduledEventMock(), after3)
		self.assertRegex(output3, 'Independence Day Celebrations')
		self.assertRegex(output3, 'cancelled')
