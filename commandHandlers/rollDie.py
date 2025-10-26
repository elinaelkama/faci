#roll any number of any sided die
#example !roll d100
#!roll 3d6
#!roll 4d20+3
#!roll 2d10-2
import random
import regex
from simpleeval import simple_eval

async def rollDie(*args: str):
	if len(args) == 0:
		return
	
	input = ""
	includes_nat1 = False
	includes_nat20 = False

	for arg in args:
		input += arg.strip().lower()

	input = input if input else "d20"

	# Remove everything except digits, d, and arithmetic operators
	input = regex.sub(r'[^0-9d\+\-\*\/\(\)\^]', '', input)

	# Handle ^ as exponentiation (convert to **)
	input = input.replace('^', '**')

	# match and roll dices
	die_pattern = r'(\d*)d(\d+)'

	while True:
		match = regex.search(die_pattern, input)
		if not match:
			break
		
		num_dice_str = match.group(1)
		sides_str = match.group(2)
		
		num_dice = int(num_dice_str) if num_dice_str != '' else 1
		sides = int(sides_str)
		
		rolls = [random.randint(1, sides) for _ in range(num_dice)]
		roll_sum = sum(rolls)
		rolls_str = '+'.join(str(roll) for roll in rolls)

		if sides == 20:
			if 1 in rolls:
				includes_nat1 = True
			if 20 in rolls:
				includes_nat20 = True
		
		replacement = f'({rolls_str})' if num_dice > 1 else str(roll_sum)
		input = input[:match.start()] + replacement + input[match.end():]

	additional_info = ""
	if includes_nat1:
		additional_info += ", *Natural 1*"
	if includes_nat20:
		additional_info += ", *Natural 20*"

	
	try:
		result = simple_eval(input)
		input = input.replace('**', '^')
		return f"Rolled {input}:\n**{result}**{additional_info}"
	except:
		return "I have no idea what you want me to roll!"


