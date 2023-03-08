from datetime import datetime, timezone
from unittest.mock import MagicMock
import discord


def parseRawCommand(command: str):
    return command.split(" ")


def getRandomChoiceMock(i: int):
    return lambda choices: choices[i]


def getDatetimeFutureMock():
    return datetime(2023, 7, 7, 6, 30, 31, 47, timezone.utc)


def getGuildMock():
    mockGuild = MagicMock(spec=discord.Guild)
    mockGuild.name = "Murder Mittens Inc"
    mockGuild.created_at = datetime(2022, 11, 17, 3, 57, 36, 21, timezone.utc)
    return mockGuild


def getMemberMock():
    mockMember = MagicMock(spec=discord.Member)
    mockMember.name = "huuhaakettu"
    mockMember.discriminator = 2347
    mockMember.joined_at = datetime(2023, 1, 27, 22, 12, 36, 21, timezone.utc)
    mockMember.guild = getGuildMock()
    return mockMember


def getInviteMock():
    mockInvite = MagicMock(spec=discord.Invite)
    mockInvite.max_age = 87000
    mockInvite.inviter = getMemberMock()
    mockInvite.id = "abcDEF7"
    mockInvite.max_uses = 5
    return mockInvite


def getTemporaryInviteMock():
    mockTemporaryInvite = getInviteMock()
    mockTemporaryInvite.max_age = 143000
    mockTemporaryInvite.temporary = True
    return mockTemporaryInvite


def getKickedMemberMock():
    mockMember = getMemberMock()

    async def getAuditLogIterator(**kwargs):
        mockAuditLogEntries = [MagicMock(spec=discord.AuditLogEntry)]
        mockAuditLogEntries[0].action = discord.AuditLogAction.kick
        mockAuditLogEntries[0].target = getMemberMock()
        mockAuditLogEntries[0].reason = "Gallavanting around"

        for entry in mockAuditLogEntries:
            yield entry

    mockGuild = getGuildMock()
    mockGuild.audit_logs = getAuditLogIterator

    mockMember.guild = mockGuild

    return mockMember


def getBannedMemberMock():
    mockMember = getMemberMock()

    async def getAuditLogIterator(**kwargs):
        mockAuditLogEntries = [MagicMock(spec=discord.AuditLogEntry)]
        mockAuditLogEntries[0].action = discord.AuditLogAction.ban
        mockAuditLogEntries[0].target = getMemberMock()
        mockAuditLogEntries[0].reason = "Disrupting the duke's peace"

        for entry in mockAuditLogEntries:
            yield entry

    mockGuild = getGuildMock()
    mockGuild.audit_logs = getAuditLogIterator

    mockMember.guild = mockGuild

    return mockMember


def getRemovedMemberMock():
    mockMember = getMemberMock()

    async def getEmptyAuditLogIterator(**kwargs):
        for entry in []:
            yield entry

    mockGuild = getGuildMock()
    mockGuild.audit_logs = getEmptyAuditLogIterator

    mockMember.guild = mockGuild

    return mockMember


def getScheduledEventMock():
    mockEvent = MagicMock(spec=discord.ScheduledEvent)
    mockEvent.name = "Independence Day Celebrations"
    mockEvent.start_time = datetime(2023, 12, 6, 14, 30, 34, 9, timezone.utc)
    mockEvent.channel = "General"
    mockEvent.location = "Helsinki"
    return mockEvent
