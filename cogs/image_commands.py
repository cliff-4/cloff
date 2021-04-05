import discord, json, datetime, random, os
from discord.ext import tasks, commands
import numpy as np, cv2 as cv #for hex colour thingy

class images_uwu(commands.Cog):

	def __init__(self, cloff):
		self.client = cloff
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('image commands ready')

	@tasks.loop(hours=5)
	async def delete_cache(self, ctx):
		try:
			with open(cloff_dict['path_to_file'] + f'/database/last_done.json', 'r+') as f:
				data = json.load(f)
				last_clear = datetime.datetime.strptime(data['last_image_cache_clear'], '%Y-%m-%d %H:%M:%S.%f')
				
				if (datetime.datetime.now() - last_clear).days >= 1:
					path = cloff_dict['path_to_file'] + "/images/.image_cache/hex_images/"
					full_path_list = []
					for file in os.listdir(path):
						full_path_list.append(path+file)
					for file in full_path_list:
						os.remove(file)
					data['last_image_cache_clear'] = str(datetime.datetime.now())

				f.seek(0)
				json.dump(data, f, indent="\t")
				f.truncate()

		except Exception as e:
			await self.client.get_channel(cloff_dict['error_channel_id']).send(e)

	@commands.command(aliases = ['color', 'c', 'Color', 'Colour', 'C'])
	async def colour(self, ctx, *arguments):
		try:
			if not arguments: arguments = ['000000']
			arguments = list(arguments)

			m = ctx.message.mentions
			r = ctx.message.role_mentions
			
			mentions = {hex(mention.colour.value)[2:].lower() : mention.id for mention in m}
			role_mentions = {hex(mention.colour.value)[2:].lower() : mention.id for mention in r}

			if '0' in mentions:
				mentions['000000'] = mentions['0']
				mentions.pop('0')
			if '0' in role_mentions:
				role_mentions['000000'] = role_mentions['0']
				role_mentions.pop('0')

			for mention in m: 
				if hex(mention.colour.value)[2:] == '0': arguments.append('000000')
				else: arguments.append(hex(mention.colour.value)[2:])
				arguments.remove(f"<@!{mention.id}>")
			for mention in r: 
				if hex(mention.colour.value)[2:] == '0': arguments.append('000000')
				else: arguments.append(hex(mention.colour.value)[2:])
				arguments.remove(f"<@&{mention.id}>")


			for argument in arguments:
				argument = argument.lower()

				men=''
				if argument in mentions: men = f"For member <@!{mentions[argument]}>"
				elif argument in role_mentions: men = f"For role <@&{role_mentions[argument]}>"

				with open(cloff_dict['path_to_file'] + f'/database/common_colours.json', 'r') as f: common_colours = json.load(f)
				common_colours_reversed = {v: k for k, v in common_colours.items()}
				
				com = ''
				if argument.upper() in common_colours_reversed: com = f"Common name: **{common_colours_reversed[argument.upper()].capitalize()}**"

				if argument.lower() in common_colours: argument = common_colours[argument.lower()]

				R = int(argument[:2], 16)
				G = int(argument[2:4], 16)
				B = int(argument[4:], 16)
				img = np.full([140,140,3], np.array([B,G,R]), dtype=np.uint8)

				image_path = cloff_dict['path_to_file']+f"/images/.image_cache/hex_images/{argument.upper()}.png"

				cv.imwrite(image_path, img)
				file = discord.File(image_path)

				message_instance = await self.client.get_channel(cloff_dict['error_channel_id']).send(file = file)
				url = str(((message_instance).attachments)[0].url)
				embed = discord.Embed(title=f";colour {argument.upper()}", colour=discord.Colour(int(f"0x{argument}", 16)))
				embed.set_image(url = url)
				embed.add_field(name = 'Colour', value=f"{men}\nHEX: 0x**{argument.upper()}**\nRGB: **{(R,G,B)}**\n{com}")
				await ctx.send(embed = embed)
				await message_instance.delete(delay=1)
		except Exception as e:
			await self.client.get_channel(cloff_dict['error_channel_id']).send(f"{e} for [{ctx.message.content}]")

	@commands.command(aliases = ['Flag', 'f'])
	async def flag(self, ctx, *args):
		try:
			argument = "_".join([arg.capitalize() for arg in args])
			if argument+".png" in os.listdir(cloff_dict['path_to_file'] + "/images/flags/"):
				file = discord.File(cloff_dict['path_to_file'] + "/images/flags/" + argument+".png")
			
			country_name = argument.replace('_', ' ')

			message_instance = await self.client.get_channel(cloff_dict['error_channel_id']).send(file = file)
			url = str(((message_instance).attachments)[0].url)
			await message_instance.delete(delay=1)

			name = "name"

			embed = discord.Embed(title="Country Flag", value='k', colour=discord.Colour(0x808080))
			embed.set_image(url = url)
			embed.add_field(name=country_name.capitalize(), value=f"""Name: {name}""")
			

			await ctx.send(embed=embed)
		
		except Exception as e:
			await self.client.get_channel(cloff_dict['error_channel_id']).send(f"{e} for [{ctx.message.content}]")

def setup(cloff):
	cloff.add_cog(images_uwu(cloff))

