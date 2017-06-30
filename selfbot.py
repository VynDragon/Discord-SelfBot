#!/bin/env python3
import discord
import asyncio
import argparse
import traceback
import subprocess
import sys
from io import StringIO


client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
    
stack = ""
@client.event
async def on_message(message):
	global stack
	print('msg by ' + message.author.name + ": " + message.content)
	if (not message.author.name == "Vdragon"):
		return
	if message.content.startswith('::run'):
		if len(message.content[6:]) < 1:
			old_stdout = sys.stdout
			try:
				redirected_output = sys.stdout = StringIO()
				exec(stack)
				await client.send_message(message.channel, '```' + str(redirected_output.getvalue()) + '```')
			except Exception as e:
				await client.send_message(message.channel, '```' + str(traceback.format_exc()).replace("```", "\`\`\`") + '```')
			finally:
				sys.stdout = old_stdout
		else:
			try:
				await client.send_message(message.channel, '```' + str(eval(message.content[6:])) + '```')
			except Exception as e:
				await client.send_message(message.channel, '```' + str(traceback.format_exc()).replace("```", "\`\`\`") + '```')
	if message.content.startswith('::stack'):
		stack +=  "\n" + message.content[8:]
		
	if message.content.startswith('::unstack'):
		try:
			stack = stack[:stack.rfind('\n')]
		except Exception as e:
			await client.send_message(message.channel, '```' + str(traceback.format_exc()).replace("```", "\`\`\`") + '```')
	if message.content.startswith('::cleanstack'):
		stack = ""
		await client.send_message(message.channel, '```' + str("stack cleaned") + '```')
	if message.content.startswith('::pstack'):
		await client.send_message(message.channel, '```' + str(stack) + '```')
#	if message.content.startswith('::bash'):



bashing = None

#async def check_bash():
	
	

parser = argparse.ArgumentParser(description='selfbot')
parser.add_argument('user')
parser.add_argument('password')
args = parser.parse_args()
client.run(args.user, args.password)

