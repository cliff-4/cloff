#!/usr/bin/env python3

import discord
from discord.ext import commands
import os
import datetime
from configparser import ConfigParser
import builtins

#set path_to_file as a variable to be used across modules
__builtins__.path_to_file = str(os.path.dirname(os.path.abspath(__file__)))
__builtins__.devs = [700376271355379823]

#to get discord token from conf.ini
info = ConfigParser()
info.read(path_to_file + '/conf.ini')
my_ass = info['DISCORD']['token']

#time recorded at the start of bot to get ;uptime
time_start = datetime.datetime.now()

cloff = commands.Bot(command_prefix=";")
cloff.remove_command('help')

def cog_update(path_to_file):
	global cog_list
	cog_list = []
	for cog in os.listdir(path_to_file + "/cogs"):
		if cog.endswith(".py"):
			cog_list.append(cog[:-3])

cog_update(path_to_file)

print('\n'+43*'#')

@cloff.command(name='cogging', aliases=['unload', 'reload', 'l', 'ul', 'rl', 'load'])
async def load(ctx, extention=''):
	if ctx.message.author.id in devs:
		cog_update(path_to_file)
		keyword = str(ctx.message.content[1:2])
		
		loading, unloading = False, False
		if keyword == 'l': loading, to_do = True, 'loaded'
		elif keyword == 'u': unloading, to_do = True, 'unloaded'
		elif keyword == 'r': unloading, loading, to_do = True, True, 'reloaded'

		if not extention: #if extention is not given, itll cycle through all the extentions in the cog folder.
			for ext in cog_list:
				try:
					if unloading: cloff.unload_extension(f'cogs.{ext}')
					if loading: cloff.load_extension(f'cogs.{ext}')
					await ctx.send(f"{to_do} [{ext}]")
					print(f"~{to_do} [{ext}]")
				except:
					try:
						if not (unloading and loading): 
							if loading: cloff.unload_extension(f'cogs.{ext}')
							if loading or unloading: cloff.load_extension(f'cogs.{ext}')
							if unloading: cloff.unload_extension(f'cogs.{ext}')
						else:
							cloff.load_extension(f'cogs.{ext}')
						await ctx.send(f"{to_do} [{ext}]")
						print(f"~{to_do} [{ext}]")
					except Exception as e:
						await ctx.send(e)
		else:
			try:
				if unloading: cloff.unload_extension(f'cogs.{extention}')
				if loading: cloff.load_extension(f'cogs.{extention}')
				await ctx.send(f"{to_do} [{extention}]")
				print(f"~{to_do} [{extention}]")
			except:
				try:
					if not (unloading and loading): 
						if loading: cloff.unload_extension(f'cogs.{extention}')
						if loading or unloading: cloff.load_extension(f'cogs.{extention}')
						if unloading: cloff.unload_extension(f'cogs.{extention}')
					else:
						cloff.load_extension(f'cogs.{extention}')
					await ctx.send(f"{to_do} [{extention}]")
					print(f"~{to_do} [{extention}]")
				except Exception as e:
					await ctx.send(e)
	else:
		await ctx.send("You do not have the permission to run this command :pig_nose:")

@cloff.command()
async def uptime(ctx):
	uptime = str(datetime.datetime.now()-time_start).split(":")
	await ctx.send(f"cloff has been online for {uptime[0]} hours, {uptime[1]} minutes and {round(float(uptime[2]))} seconds.")

for filename in cog_list:
	cloff.load_extension(f"cogs.{filename}")

cloff.run(my_ass)
