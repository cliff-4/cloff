import discord
from discord.ext import tasks, commands

class task_uwu(commands.Cog):

	def __init__(self, cloff):
		self.index = 0
		self.printer.start()

	def cog_unload(self):
		self.printer.cancel()
	
	@tasks.loop(seconds=2)
	async def printer(self):
		k = None

def setup(cloff):
	cloff.add_cog(task_uwu(cloff))