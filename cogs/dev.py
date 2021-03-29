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
	async def uptime(self, ctx):
		uptime = str(datetime.datetime.now()-time_start).split(":")
		await ctx.send(f"cloff has been online for {uptime[0]} hours, {uptime[1]} minutes and {round(float(uptime[2]))} seconds.")

	@commands.command()
	async def test(self, ctx):
		await ctx.send(ctx.message.content[1:3])

#    @commands.Cog.listener()
#    async def on_message(self, message):
#        if message.author == cloff.user:
#            return
#        else:
#            k = False
#            for term in ['boy', 'girl', 'boi', 'gorl', 'slave', 'cloffo', 'cloff']:
#                if (f"good {term}" in message.content):
#                    k = True
#            if k:
#                await message.channel.send(f"uwu thanks {str(message.author)[:-5]}")

	@commands.command()
	async def quote(self, ctx):
		k = None

	@commands.command(aliases=['wp'])
	async def water_ping(self, ctx):
		k = None
		#check if server has agreed for waterping. if not, and the person who ran isnt admin, return "ask admin to enable"
		#if admin, add server to list and check if it has a waterping channel.
		#if not, add a channel and start sending waterpings to it. also create roll w blue colour.
		#after admin, whoever runs waterping, add them to the role of waterping and send that they have been added.
		#also tell them if they want to be removed from waterping, run ;water_ping or ;wp


def setup(cloff):
	cloff.add_cog(commands_under_development(cloff))
