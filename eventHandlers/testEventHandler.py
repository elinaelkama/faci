import unittest

from eventHandlers import inviteCreate, memberBan, memberJoin, memberRemove, memberTimeout, memberUnban, scheduledEventCreate, scheduledEventDelete, scheduledEventUpdate
from helpers import testHelper

class TestEventHandler(unittest.IsolatedAsyncioTestCase):
	async def testInviteCreate(self):
		self.assertEqual(await inviteCreate.inviteCreate(testHelper.getInviteMock()),
			"huuhaakettu#2347 created an invite abcDEF7, for 5 use(s) that expires in 1 day and 10 minutes"
			)

	async def testInviteCreateTemporary(self):
		self.assertEqual(await inviteCreate.inviteCreate(testHelper.getTemporaryInviteMock()),
			"huuhaakettu#2347 created a temporary invite"
			)