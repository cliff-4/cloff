import discord, json, datetime
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
			with open(cloff_dict['path_to_file'] + f'/database/water.json', 'r') as f:
				data = json.load(f)
				channels = data['servers']
			for channel in channels:
				channel_instance = self.client.get_channel(channel)
				await channel_instance.send('Remember to drink water yoo :sweat_drops:\n<@&826838004249264138>')
				#import channel list
				#check if channel exists
				#if not and server has agreed for water ping, create channel and add to list
				#send water ping
		except Exception as e:
			await self.client.get_channel(cloff_dict['error_channel_id']).send(e)

	@water.before_loop
	async def before_water(self):
		await self.client.wait_until_ready()

def setup(cloff):
	cloff.add_cog(water_ping(cloff))
