import discord, json, datetime, random, os
from discord.ext import tasks, commands
import numpy as np, cv2 as cv #for hex colour thingy

class images_uwu(commands.Cog):

	def __init__(self, cloff):
		self.client = cloff
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('image commands ready')

	@tasks.loop(seconds=3600)
	async def delete_cache(self):
		try:
			os.listdir("")
		except Exception as e:
			await self.client.get_channel(cloff_dict['error_channel_id']).send(e)

	@commands.command(aliases = ['color', 'c'])
	async def colour(self, ctx, argument="000000"):
		try:
			
			with open(cloff_dict['path_to_file'] + f'/database/common_colours.json', 'r') as f: common_colours = json.load(f)
			if argument.lower() in common_colours: argument = common_colours[argument.lower()]

			R = int(argument[:2], 16)
			G = int(argument[2:4], 16)
			B = int(argument[4:], 16)
			img = np.full([140,140,3], np.array([B,G,R]), dtype=np.uint8)

			image_path = cloff_dict['path_to_file']+f"/images/.image_cache/hex_images/{argument}.png"

			cv.imwrite(image_path, img)
			file = discord.File(image_path)
			await ctx.send(f"HEX: {argument}\nRGB: {[R,G,B]}", file=file)
		except Exception as e:
			await self.client.get_channel(cloff_dict['error_channel_id']).send(e)

def setup(cloff):
	cloff.add_cog(images_uwu(cloff))

