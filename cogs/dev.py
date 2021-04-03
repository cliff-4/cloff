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
	async def test(self, ctx):
		try:	
			###
			await ctx.send(ctx.message.channel.id)
			###
		except Exception as e:
			await ctx.send(e) #dont wanna send this error to the error channel ykno

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
		0
		#print('memes ready')

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
