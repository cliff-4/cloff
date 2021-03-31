import discord
from discord.ext import commands
import os
import random
import datetime
import time
import json
from spellchecker import SpellChecker

class commands_under_development(commands.Cog):

	def __init__(self, cloff):
		self.client = cloff

		with open(path_to_file + '/database/webster_dictionary.json', 'r') as myfile: self.od_data = json.loads(myfile.read())
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('dev commands ready')

	@commands.command()
	async def kill(self, ctx):
		if ctx.message.author.id in devs:
			exit()

	@commands.command()
	async def uptime(self, ctx):
		uptime = str(datetime.datetime.now()-time_start).split(":")
		await ctx.send(f"cloff has been online for {uptime[0]} hours, {uptime[1]} minutes and {round(float(uptime[2]))} seconds.")

	@commands.command(aliases=['t'])
	async def test(self, ctx):
		try:	
			###
			user = ctx.message.author
			#await ctx.guild.create_role(name="water buddies", colour = discord.Colour(0x40dde6))
			rollee = discord.utils.get(ctx.guild.roles, name="water buddies")
			#await user.add_roles(rollee)
			await ctx.send(ctx.guild.roles)
			###
		except Exception as e:
			await ctx.send(e)

	@commands.command()
	async def quote(self, ctx):
		0

	@commands.command(aliases=['wp'])
	async def water_ping(self, ctx):
		0
		#check if server has agreed for waterping. if not, and the person who ran isnt admin, return "ask admin to enable"
		#if admin, add server to list and check if it has a waterping channel.
		#if not, add a channel and start sending waterpings to it. also create roll w blue colour.
		#after admin, whoever runs waterping, add them to the role of waterping and send that they have been added.
		#also tell them if they want to be removed from waterping, run ;water_ping or ;wp
		#ask for timezone in wp config. dont wanna ping them all night ykno.

		#waterping channel in bot server: 826193848476500019
	
	@commands.command(aliases=['wd', 'webster', 'Webster'])
	async def dictionary(self, ctx, word): #2 modules loaded and one line of code in __init__()
		try:
			word = word.lower()
			obj = self.od_data
			try:
				await ctx.send(f"**{word.capitalize()}**\n\n{obj[word]}")
				word_found = True
			except KeyError:
				spell = SpellChecker()
				list = spell.candidates(word)
				await ctx.send(f"That word might be wrong. Did you instead mean any of these:\n\n**{', '.join(list)}**")
		except Exception as e:
			await ctx.send(e)

class youtube_uwu(commands.Cog):

	def __init__(self, cloff):
		info = ConfigParser()
		info.read(path_to_file + '/conf.ini')
		self.client = cloff
		youtube_api_key = info["YOUTUBE"]["api_key"],
	
	@commands.Cog.listener()
	async def on_ready(self):
		0
		#print('youtube ready')

	@commands.command(aliases=['youtube'])
	async def yt(self, ctx):
		0

def setup(cloff):
	cloff.add_cog(commands_under_development(cloff))
#	cloff.add_cog(youtube_uwu(cloff))
