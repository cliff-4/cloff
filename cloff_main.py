#!/usr/bin/env python3

import discord
from discord.ext import commands
import os
import datetime
from configparser import ConfigParser
import builtins
import traceback

#set path_to_file as a variable to be used across modules
__builtins__.cloff_dict = {
	'path_to_file' : str(os.path.dirname(os.path.abspath(__file__))),
	'devs' : [700376271355379823],
	'time_start' : datetime.datetime.now(),
	'error_channel_id' : 827694723555786772,
	'unnecessary_boolean_value_for_my_personal_water_pings' : False
} #prolly wanna keep this in json file with you (when hosting bot on other server)

#to get discord token from conf.ini
info = ConfigParser()
info.read(cloff_dict['path_to_file'] + '/conf.ini')
my_ass = info['DISCORD']['token']

cloff = commands.Bot(command_prefix=";")
cloff.remove_command('help')

def cog_update():
	global cog_list
	cog_list = []
	for cog in os.listdir(cloff_dict['path_to_file'] + "/cogs"):
		if cog.endswith(".py"):
			cog_list.append(cog[:-3])
	cog_list.sort()

cog_update()

print('\n'+43*'#')

@cloff.command(name='cogging', aliases=['unload', 'reload', 'l', 'ul', 'rl', 'load'])
async def load(ctx, extention=''):
	if ctx.message.author.id in cloff_dict['devs']:
		cog_update()
		keyword = str(ctx.message.content[1:2])
		
		loading, unloading = False, False
		if keyword == 'l': loading, to_do = True, 'loaded'
		elif keyword == 'u': unloading, to_do = True, 'unloaded'
		elif keyword == 'r': unloading, loading, to_do = True, True, 'reloaded'

		if not extention: #if extention is not given, itll cycle through all the extentions in the cog folder.
			for ext in cog_list:
				time1 = datetime.datetime.now()
				try:
					if unloading: cloff.unload_extension(f'cogs.{ext}')
					if loading: cloff.load_extension(f'cogs.{ext}')
					await ctx.send(f"{to_do} [{ext}]\t_executed in {str(datetime.datetime.now()-time1)[-8:-3]} s_")
					print(f"~{to_do} [{ext}]")
				except:
					try:
						if not (unloading and loading): 
							if loading: cloff.unload_extension(f'cogs.{ext}')
							if loading or unloading: cloff.load_extension(f'cogs.{ext}')
							if unloading: cloff.unload_extension(f'cogs.{ext}')
						else:
							cloff.load_extension(f'cogs.{ext}')
						await ctx.send(f"{to_do} [{ext}]\t_executed in {str(datetime.datetime.now()-time1)[-8:-3]} s_")
						print(f"~{to_do} [{ext}]")
					except Exception:
						await ctx.send(traceback.format_exc())
		else:
			time1 = datetime.datetime.now()
			try:
				if unloading: cloff.unload_extension(f'cogs.{extention}')
				if loading: cloff.load_extension(f'cogs.{extention}')
				await ctx.send(f"{to_do} [{extention}]\t_executed in {str(datetime.datetime.now()-time1)[-8:-3]} s_")
				print(f"~{to_do} [{extention}]")
			except:
				try:
					if not (unloading and loading): 
						if loading: cloff.unload_extension(f'cogs.{extention}')
						if loading or unloading: cloff.load_extension(f'cogs.{extention}')
						if unloading: cloff.unload_extension(f'cogs.{extention}')
					else:
						cloff.load_extension(f'cogs.{extention}')
					await ctx.send(f"{to_do} [{extention}]\t_executed in {str(datetime.datetime.now()-time1)[-8:-3]} s_")
					print(f"~{to_do} [{extention}]")
				except Exception:
					await ctx.send(traceback.format_exc())
	else:
		await ctx.send("You do not have the permission to run this command :pig_nose:")

for filename in cog_list:
	cloff.load_extension(f"cogs.{filename}")

cloff.run(my_ass)
