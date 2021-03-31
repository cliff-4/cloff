import discord
from discord.ext import commands
import os
import random
import datetime
import time

class commands_under_development(commands.Cog):

	def __init__(self, cloff):
		self.client = cloff
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('dev commands ready')

	@commands.command()
	async def kill(self, ctx):
		if ctx.message.author.id in devs:
			await ctx.send("_adios_")
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
			await ctx.guild.create_role(name="water buddies", colour = discord.Colour(0x40dde6))
			rollee = discord.utils.get(ctx.guild.roles, name="water buddies").id
			#await user.add_roles(rollee)
			await ctx.send(rollee)
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
