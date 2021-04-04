import discord, json, datetime, random, os
from discord.ext import tasks, commands

class water_ping(commands.Cog):

	def __init__(self, cloff):
		self.client = cloff
		self.water.start()

	def cog_unload(self):
		self.water.cancel()
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('wet as fuck bro')

	@tasks.loop(seconds=600)
	async def water(self):
		try:
			with open(cloff_dict['path_to_file'] + f'/database/water.json', 'r+') as f:
				data = json.load(f)
				servers = data['servers_channels']
				last_poing = datetime.datetime.strptime(data["last_poing"], '%Y-%m-%d %H:%M:%S.%f')

				if (datetime.datetime.now()-last_poing).seconds >= 3600:

					file = discord.File(cloff_dict['path_to_file'] + f'/images/water_pics/{random.choice(os.listdir(cloff_dict["path_to_file"]+"/images/water_pics/"))}')
					
					for server in servers:

						server_instance = self.client.get_guild(server[0])
						
						if bool(server_instance):
							
							channel_instance = self.client.get_channel(server[1])				
							role_instance = self.client.get_guild(server[0]).get_role(server[2])
							
							if not bool(channel_instance):
								channel_instance = await server_instance.create_text_channel(name="water-ping")
								server[1] = channel_instance.id
							if not bool(role_instance):
								role_instance = await server_instance.create_role(name="water buddies", colour=discord.Colour(0x40dde6))
								server[2] = role_instance.id

							messages_instance = open(cloff_dict['path_to_file'] + "/database/water_messages.txt", "r")
							messages = messages_instance.read().split("\n")
							messages_instance.close()

							string = random.choice(messages)
							while not string:
								string = random.choice(messages)

							message = f'{string}\n<@&{role_instance.id}>'
							check_emoji = "\N{ballot box with check}"

							water_ping = await channel_instance.send(message, file = file)
							await water_ping.add_reaction(check_emoji)

					data['last_poing'] = str(datetime.datetime.now())

				f.seek(0)
				json.dump(data, f, indent="\t")
				f.truncate()

		except Exception as e:
			await self.client.get_channel(cloff_dict['error_channel_id']).send(e)

	@commands.command(aliases=['wp', 'wet', 'wet_me'])
	async def water_ping(self, ctx):
		try:
			with open(cloff_dict['path_to_file'] + f'/database/water.json', 'r+') as f:
				data = json.load(f)
				if ctx.guild.id in [servers[0] for servers in data["servers_channels"]]:
					guild_roles = await ctx.guild.fetch_roles()
					if ("water buddies" in [role.name for role in guild_roles]) or (data["servers_channels"][ctx.guild.id]):
						0
			#if not ()
			#await ctx.send(bool("water buddies" in [role.name for role in ctx.author.roles]))
		except Exception as e:
			await self.client.get_channel(cloff_dict['error_channel_id']).send(e)
		#check if server has agreed for waterping. if not, and the person who ran isnt admin, return "ask admin to enable"
		#if admin, add server to list and check if it has a waterping channel.
		#if not, add a channel and start sending waterpings to it. also create roll w blue colour.
		#after admin, whoever runs waterping, add them to the role of waterping and send that they have been added.
		#also tell them if they want to be removed from waterping, run ;water_ping or ;wp
		#ask for timezone in wp config. dont wanna ping them all night ykno.

		#waterping channel in bot server: 826193848476500019

def setup(cloff):
	cloff.add_cog(water_ping(cloff))
