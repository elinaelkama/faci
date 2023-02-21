from datetime import datetime
from unittest.mock import MagicMock
import discord
import pytz


def parseRawCommand(command: str):
	return command.split(" ")

def getRandomChoiceMock(i: int):
	return lambda choices: choices[i]

def getDatetimeNowMock():
	return datetime(2023, 5, 14, 13, 45, 20, 12)

def getDatetimeFutureMock():
	return datetime(2023, 7, 7, 6, 30, 31, 47, pytz.UTC)

def getDatetimePastMock():
	return datetime(2023, 1, 27, 22, 12, 36, 21, pytz.UTC)

def getGuildMock():
	mockGuild = MagicMock(spec=discord.Guild)
	mockGuild.name = "Murder Mittens Inc"
	mockGuild.created_at = getDatetimePastMock()
	return mockGuild
	
def getMemberMock():
	mockMember = MagicMock(spec=discord.Member)
	mockMember.name = "huuhaakettu"
	mockMember.discriminator = 2347
	mockMember.joined_at = getDatetimePastMock()
	return 	mockMember

def getInviteMock():
	mockInvite = MagicMock(spec=discord.Invite)
	mockInvite.max_age = 87000
	mockInvite.inviter = getMemberMock()
	mockInvite.id = "abcDEF7"
	mockInvite.max_uses = 5
	return 	mockInvite

def getTemporaryInviteMock():
	mockTemporaryInvite = MagicMock(spec=discord.Invite)
	mockTemporaryInvite.temporary = True
	mockTemporaryInvite.inviter = getMemberMock()
	return mockTemporaryInvite
