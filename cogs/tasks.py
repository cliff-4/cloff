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
		print('tasks ready')

	@tasks.loop(hours=1)
	async def water(self):
		try:
			channel = self.client.get_channel(826193848476500019)
			
			await channel.send('Remember to drink water yoo :sweat_drops:\n<@&826838004249264138>')
			#import channel list
				#check if channel exists
				#if not and server has agreed for water ping, create channel and add to list
				#send water ping
		except Exception as e:
			0

def setup(cloff):
	cloff.add_cog(water_ping(cloff))
