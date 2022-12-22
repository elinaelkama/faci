import json
import discord
import requests
import random
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", intents=intents)
intents.members = True

#Gives a greeting when "Hi" is typed
@bot.command()
async def Hi(ctx):
    greetings = ["Hello :smile:", "Hi :wave:", "Greetings friend :hugging:"]
    await ctx.send(f"{random.choice(greetings)}")

#Sends a direct message to the person who joined
@bot.event
async def on_member_join(member):
    await member.send(f"Welcome {member.name} to {member.guild}!")

#Choses a random item from the list given
@bot.command()
async def choose(ctx, *args):
    arguments = " ".join(args).split(",")
    choices = list(map(lambda choice: choice.strip().capitalize(), arguments))
    flavor = ["is by far the best choice", "and if you pick anything else I'll never talk to you again", "try it, you'll love it", "is clearly the only choice here", "is best by all measures"]
    await ctx.send(f'**{random.choice(choices)}** {random.choice(flavor)}.')

@bot.command()
async def joke(ctx):
    response = requests.get("https://v2.jokeapi.dev/joke/Any?safe-mode&type=single")
    try:
        body = response.json()
        joke = body["joke"]
    except Exception as error:
        print(f"failed to get joke: {error}")
        return
    await ctx.send(f"{joke}")


# Read your bot token from the txt file in your project root:
Secret = open("api.secret", 'r')
Secret = Secret.read()

# Run the bot in an event loop:
bot.run(Secret)
