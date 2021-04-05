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
		if ctx.message.author.id in cloff_dict['devs']:
			await ctx.send("_adios_")
			exit()

	@commands.command()
	async def uptime(self, ctx):
		uptime = str(datetime.datetime.now()-cloff_dict['time_start']).split(":")
		await ctx.send(f"cloff has been online for {uptime[0]} hours, {uptime[1]} minutes and {round(float(uptime[2]))} seconds.")

	@commands.command(aliases=['t'])
	async def test(self, ctx, *args):
		try:
			if ctx.message.author.id in cloff_dict['devs']:
				
				###
				#list = []
				#await ctx.guild.fetch_roles()
				#await ctx.send(ctx.author.avatar_url)
				file = discord.File(f"{cloff_dict['path_to_file']}/images/.image_cache/hex_images/000000.png")
				
				e = discord.Embed()
				
				e.set_image(url=f"attachment://{cloff_dict['path_to_file']}/images/.image_cache/hex_images/000000.png")
				k='40dde6'
				await ctx.send('k')
				#emoji = self.client.get_emoji(emoji_id)
				#await ctx.message.add_reaction(emoji)
				#ids = []
				#for guild in self.client.guilds:
				#	ids.append(guild.id)
				#await ctx.send(ids)
				### server_id = ctx.message.channel.guild.id
		except Exception as e:
			await ctx.send(e) #dont wanna send this error to the error channel ykno

	@commands.command()
	async def quote(self, ctx):
		0

class youtube_uwu(commands.Cog):

	def __init__(self, cloff):
		info = ConfigParser()
		info.read(cloff_dict['path_to_file'] + '/conf.ini')
		self.client = cloff
		youtube_api_key = info["YOUTUBE"]["api_key"],
	
	@commands.Cog.listener()
	async def on_ready(self):
		0
		#print('youtube ready')

	@commands.command(aliases=['youtube'])
	async def yt(self, ctx):
		0

class le_memes(commands.Cog):

	def __init__(self, cloff):
		self.client = cloff
		import cv2 as cv
		path = "templates\\lisa.jpg"
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('memes ready')

	@commands.command(aliases=['youtube'])
	async def meme(self, ctx):
		cv.namedWindow("Processed", cv.WINDOW_AUTOSIZE)
		image = cv.imread(path) 
		font = cv.FONT_HERSHEY_SIMPLEX 

		a,b = 150,200

		org = (a,b) 
		argument = 'fuck off'
		fontScale = 1
		color = (255, 0, 0) 
		thickness = 2
		img2 = cv.putText(image, argument, org, font, fontScale, color, thickness, cv.LINE_AA) 
		cv.imshow("Processed", img2)

		k = cv.waitKey(2000)
		if k == ord('q'):
			cv.destroyAllWindows()

		print(image.shape)

def setup(cloff):
	cloff.add_cog(commands_under_development(cloff))
#	cloff.add_cog(youtube_uwu(cloff))
#	cloff.add_cog(le_memes(cloff))
