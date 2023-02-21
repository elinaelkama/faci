import unittest

from eventHandlers import inviteCreate, memberBan, memberJoin, memberRemove, memberTimeout, memberUnban, scheduledEventCreate, scheduledEventDelete, scheduledEventUpdate
from helpers import testHelper

class TestEventHandler(unittest.IsolatedAsyncioTestCase):
	async def testInviteCreate(self):
		output = await inviteCreate.inviteCreate(testHelper.getInviteMock())
		self.assertRegex(output, 'huuhaakettu#2347')
		self.assertRegex(output, 'abcDEF7')
		self.assertRegex(output, '5 use\(s\)')
		self.assertRegex(output, '1 day and 10 minutes')

	"""async def testInviteCreateTemporary(self):
		self.assertEqual(await inviteCreate.inviteCreate(testHelper.getTemporaryInviteMock()),
			"huuhaakettu#2347 created a temporary invite"
			)

	async def testMemberJoin(self):
		self.assertEqual(await memberJoin.memberJoin(testHelper.getMemberMock()),
			"huuhaakettu#2347 joined Murder Mittens Inc"
			)

	async def testMemberRemove(self):
		self.assertEqual(await memberRemove.memberRemove(testHelper.getMemberMock()),
			"huuhaakettu#2347 has left the server"
			)

	async def testMemberRemoveKick(self):
		self.assertEqual(await memberRemove.memberRemove(testHelper.getKickedMemberMock()),
			"huuhaakettu#2347 was kicked from the server for: reason"
			)

	async def testMemberTimeout(self):
		pass
	async def testMemberBan(self):
		pass
	async def testMemberUnban(self):
		pass
	async def testScheduledEventCreate(self):
		pass
	async def testScheduledEventDelete(self):
		pass
	async def testScheduledEventUpdate(self):
		pass"""
