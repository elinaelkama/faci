import re
from discord import VoiceChannel
from discord.ext import commands

def listTextChannels(bot: commands.Bot):
	list = []
	for channel in bot.get_all_channels():
		if str(channel.type) != "text":
			continue
		list.append(channel.name)
	return "\n".join(list)

def getEventChannel(bot: commands.Bot):
	for channel in bot.get_all_channels():
		if str(channel.type) == "text" and channel.name.startswith("event"):
			return channel
	return None

def getAuditChannel(bot: commands.Bot):
	for channel in bot.get_all_channels():
		if str(channel.type) == "text" and channel.name.startswith("audit"):
			return channel
	return None
