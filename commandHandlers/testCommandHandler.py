from datetime import datetime
import unittest
from unittest.mock import patch

import pytz

from commandHandlers import guildCreated, randomChoice, userJoined
from helpers import testHelper
#, side_effects=["dog", "try it, you'll love it.", "everything everywhere all at once", "is by far the best choice."]
class CommandHandlerTest(unittest.IsolatedAsyncioTestCase):
    @patch('random.choice', testHelper.getRandomChoiceMock(1))
    async def testRandomChoiceHappy(self):
        self.assertEqual(await randomChoice.randomChoice(
            *testHelper.parseRawCommand("cat, dog, rat")),
            "**Dog** and if you pick anything else I'll never talk to you again."
            )
        self.assertEqual(await randomChoice.randomChoice(
            *testHelper.parseRawCommand("Lord of the Rings, everything everywhere all at once, friday the 13th, lion king")),
            "**Everything everywhere all at once** and if you pick anything else I'll never talk to you again."
            )


    async def testRandomChoiceSad(self):
        self.assertEqual(await randomChoice.randomChoice(), "You have given me no choice")
        self.assertEqual(await randomChoice.randomChoice(*testHelper.parseRawCommand("   ,  , , ,  ,,,  , , , , ")),
            "You have given me no choice"
            )

    async def testGuildCreated(self):
        with patch('datetime.datetime') as pachedDatetime:
            pachedDatetime.now.return_value = datetime(2023, 5, 14, 13, 45, 20, 12, pytz.UTC)
            output = await guildCreated.guildCreated(testHelper.getGuildMock())
            self.assertRegex(output, 'Murder Mittens Inc')
            self.assertRegex(output, '25 weeks, 3 days and 9 hours')
            self.assertRegex(output, '17.11.2022')

    async def testUserJoined(self):
        with patch('datetime.datetime') as pachedDatetime:
            pachedDatetime.now.return_value = datetime(2023, 3, 18, 23, 12, 20, 12, pytz.UTC)
            output = await userJoined.userJoined(testHelper.getMemberMock())
            self.assertRegex(output, 'huuhaakettu')
            self.assertRegex(output, '7 weeks, 1 day and 59 minutes')
            self.assertRegex(output, '27.01.2023')
            self.assertRegex(output, '22:12')