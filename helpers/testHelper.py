from datetime import datetime
from unittest.mock import MagicMock
import discord
import pytz


def parseRawCommand(command: str):
	return command.split(" ")

def getRandomChoiceMock(i: int):
	return lambda choices: choices[i]

def getDatetimeFutureMock():
	return datetime(2023, 7, 7, 6, 30, 31, 47, pytz.UTC)


def getGuildMock():
	mockGuild = MagicMock(spec=discord.Guild)
	mockGuild.name = "Murder Mittens Inc"
	mockGuild.created_at = datetime(2022, 11, 17, 3, 57, 36, 21, pytz.UTC)
	mockAuditLog = MagicMock(spec=discord.Guild.audit_logs)
	mockAuditLogEntries = [MagicMock(spec=discord.AuditLogEntry)]
	mockAuditLogEntries[0].action = discord.AuditLogAction.ban
	mockGuild.audit_logs.return_value = mockAuditLog
	return mockGuild
	
def getMemberMock():
	mockMember = MagicMock(spec=discord.Member)
	mockMember.name = "huuhaakettu"
	mockMember.discriminator = 2347
	mockMember.joined_at = datetime(2023, 1, 27, 22, 12, 36, 21, pytz.UTC)
	mockMember.guild = getGuildMock()
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

def getKickedMemberMock():
	mockMember = MagicMock(spec=discord.Member)
	mockMember.name = "zoz"
	mockMember.discriminator = 9645

	mockGuild = MagicMock(spec=discord.Guild)
	mockMember.guild = mockGuild

	mockAuditLogEntries = [MagicMock(spec=discord.AuditLogEntry)]
	mockAuditLogEntries[0].action = discord.AuditLogAction.kick
	mockAuditLogEntries[0].target = getMemberMock()
	mockAuditLogEntries[0].reason = "Gallavanting around"

	mockAuditLog = MagicMock(spec=discord.Guild.audit_logs)
	mockAuditLog.entries = mockAuditLogEntries
	mockGuild.audit_logs.return_value = mockAuditLog

	return mockMember