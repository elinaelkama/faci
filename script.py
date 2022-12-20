import discord

# Import the commands module:
from discord.ext import commands

# Initialize the bot instance and use a blank prefix:
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", intents=intents)


@bot.command()
async def Hi(ctx):
    await ctx.send("Hello :smile:")

# Read your bot token from the txt file in your project root:
Secret = open("secret.txt", 'r')
Secret = Secret.read()

# Run the bot in an event loop:
bot.run(Secret)
