import random


async def randomChoice(*args: str):
    arguments = " ".join(args).split(",")
    choices = list(
        filter(None, map(lambda choice: choice.strip().capitalize(), arguments))
    )
    if len(choices) == 0:
        return "You have given me no choice"
    flavor = [
        "is by far the best choice",
        "and if you pick anything else I'll never talk to you again",
        "try it, you'll love it",
        "is clearly the only choice here",
        "is best by all measures",
    ]
    return f"**{random.choice(choices)}** {random.choice(flavor)}."
