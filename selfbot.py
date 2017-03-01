#!/bin/env python3
import discord
import asyncio
import argparse
import traceback
import subprocess


client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
    
@client.event
async def on_message(message):
	print('msg by ' + message.author.name + ": " + message.content)
	if (not message.author.name == "Vdragon"):
		return
	if message.content.startswith('::run'):
		try:
			await client.send_message(message.channel, '```' + str(eval(message.content[6:])) + '```')
		except Exception as e:
			await client.send_message(message.channel, '```' + str(traceback.format_exc()).replace("```", "\`\`\`") + '```')
	if message.content.startswith('::bash'):



bashing = None

async def check_bash():
	
	

parser = argparse.ArgumentParser(description='selfbot')
parser.add_argument('user')
parser.add_argument('password')
args = parser.parse_args()
client.run(args.user, args.password)

