import discord
from discord.ext import tasks, commands

class water_ping(commands.Cog):

	def __init__(self, cloff):
		self.client = cloff
		self.water.start()

	def cog_unload(self):
		self.water.cancel()
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('tasts ready')

	@tasks.loop(seconds=2)
	async def water(self):
		k = None
		#import channel list
			#check if channel exists
			#if not and server has agreed for water ping, create channel and add to list
			#send water ping

def setup(cloff):
	cloff.add_cog(water_ping(cloff))
