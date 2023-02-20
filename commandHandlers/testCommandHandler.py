import unittest
from unittest.mock import patch

from commandHandlers import randomChoice
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
        self.assertEqual(await randomChoice.randomChoice(*testHelper.parseRawCommand("   ,  , , ,  ,,,  , , , , ")), "You have given me no choice")
