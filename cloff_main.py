#!/usr/bin/env python3

import discord
from discord.ext import commands
import os
import datetime
from configparser import ConfigParser
import builtins

#set path_to_file as a variable to be used across modules
__builtins__.path_to_file = str(os.path.dirname(os.path.abspath(__file__)))

#to get discord token from conf.ini
info = ConfigParser()
info.read(path_to_file + '/conf.ini')
my_ass = info['DISCORD']['token']

#time recorded at the start of bot to get ;uptime
time_start = datetime.datetime.now()

cloff = commands.Bot(command_prefix=";")
cloff.remove_command('help')

cog_list = []

def cogging():
	cog_list = []
	for cog in os.listdir(path_to_file + "/cogs"):
		if cog.endswith(".py"):
			cog_list.append(cog[:-3])

cogging()

print('\n'+43*'#')

@cloff.command()
async def reload(ctx, extention=''):
	cogging()
	if ctx.message.author.id != 700376271355379823:
		await ctx.send("You do not have permission to run this command :pig_nose:")
	else:
		if not extention:
			for ext in cog_list:
				try:
					if ctx.message.author.id == 700376271355379823:
						cloff.unload_extension(f'cogs.{ext}')
						cloff.load_extension(f'cogs.{ext}')
						await ctx.send(f"reloaded {ext}")                    
				except Exception as e:
					await ctx.send(e)
			print("cogs reloaded")
		else:
			try:
				cloff.unload_extension(f'cogs.{extention}')
				cloff.load_extension(f'cogs.{extention}')
				await ctx.send(f"{extention} reloaded")
				print(extention, "reloaded")
			except Exception as e:
				await ctx.send(e)

@cloff.command()
async def load(ctx, extention=''):
	cogging()
	if ctx.message.author.id != 700376271355379823:
		await ctx.send("You do not have permission to run this command :pig_nose:")
	else:
		if not extention:
			for ext in cog_list:
				try:
					cloff.load_extension(f'cogs.{ext}')
					await ctx.send(f"loaded {ext}")                    
				except Exception as e:
					await ctx.send(e)
			print("cogs loaded")
		else:
			try:
				cloff.load_extension(f'cogs.{extention}')
				await ctx.send(f"{extention} loaded")
				print(extention, "loaded")
			except Exception as e:
				await ctx.send(e)

@cloff.command()
async def unload(ctx, extention=''):
	cogging()
	if ctx.message.author.id != 700376271355379823:
		await ctx.send("You do not have permission to run this command :pig_nose:")
	else:
		if not extention:
			for ext in cog_list:
				try:
					cloff.unload_extension(f'cogs.{ext}')
					await ctx.send(f"reloaded {ext}")                    
				except Exception as e:
					await ctx.send(e)
			print("cogs unloaded")
		else:
			try:
				cloff.unload_extension(f'cogs.{extention}')
				await ctx.send(f"{extention} unloaded")
				print(extention, "unloaded")
			except Exception as e:
				await ctx.send(e)

@cloff.command()
async def uptime(ctx):
	uptime = str(datetime.datetime.now()-time_start).split(":")
	await ctx.send(f"cloff has been online for {uptime[0]} hours, {uptime[1]} minutes and {round(float(uptime[2]))} seconds.")

for filename in cog_list:
	cloff.load_extension(f"cogs.{filename}")

cloff.run(my_ass)
