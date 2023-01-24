import random

async def randomChoice(*args):
	arguments = " ".join(args).split(",")
	choices = list(map(lambda choice: choice.strip().capitalize(), arguments))
	flavor = ["is by far the best choice", "and if you pick anything else I'll never talk to you again", "try it, you'll love it", "is clearly the only choice here", "is best by all measures"]
	return f'**{random.choice(choices)}** {random.choice(flavor)}.'