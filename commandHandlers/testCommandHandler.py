import unittest
from unittest.mock import patch

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
        self.assertEqual(await guildCreated.guildCreated(testHelper.getGuildMock()),
            "Murder Mittens Inc was created on 27.01.2023 UTC/GMT\nServer has been in existence for 3 weeks, 3 days and 14 hours"
            )

    async def testUserJoined(self):
        self.assertEqual(await userJoined.userJoined(testHelper.getMemberMock()),
            "huuhaakettu, you joined on Fri 27.01.2023 at 22:12 UTC/GMT\nYou have been on the server for 3 weeks, 3 days and 14 hours"
            )