import discord
from discord.ext import commands
import os
import random
import datetime
import time
import numpy as np, cv2 as cv #for hex colour thingy

class cloff_the_bot(commands.Cog):

	def __init__(self, cloff):
		self.client = cloff
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('bitch im ready')

	@commands.command(aliases=['h'])
	async def help(self, ctx, *args):
		all_commands = ['hello', 'reddit', 'purge', 'ping','cuss', 'bully', 'spam', 'echo', 'ree', 'REE', 'AAA', 'good', 'help', 'dictionary', 'dict', 'colour', 'color']
		if not args: args = all_commands
		if len(set(args).intersection(all_commands)) == 0:
			await ctx.send("The command doesn't exist. Please try ;help")
		else:
			author = None #ctx.message.author
			embed = discord.Embed(colour = discord.Colour(0xe08e00))
			embed.set_author(name="Help")
			if 'hello' in args: embed.add_field(name=';hello', value='Why not greet this friendly bot!', inline=False)
			if 'reddit' in args: embed.add_field(name=';reddit subreddit', value='Sends a random image from that subreddit', inline=True)
			if ('dictionary' in args) or ('dict' in args): embed.add_field(name=';dictionary word', value='Gives the definition of the **word**', inline=False)
			if ('colour' in args) or ('color' in args): embed.add_field(name=';colour hexcode(without # or 0x)', value='Sends a visual of the hex code', inline=False)
			if 'purge' in args: embed.add_field(name=';purge n', value='Purges last **n** messages. Default **n** = **1**', inline=True)
			if 'ping' in args: embed.add_field(name=';ping', value='returns Pong! I swear. Try it.', inline=False)
			if 'cuss' in args: embed.add_field(name=';cuss @user', value='Sends a _not so cheerish_ message', inline=True)
			if 'bully' in args: embed.add_field(name=';bully @user', value='Basically **;cuss**, but better.', inline=True)
			if 'spam' in args: embed.add_field(name=';spam arg n', value='Spams the **arg** **n** times, of course. For example, if you wanna spam 3, do **;spam 3 10**', inline=True)
			if 'echo' in args: embed.add_field(name=';echo arg', value='Just returns the **arg**. Nothing too fancy.', inline=True)
			if 'ree' in args: embed.add_field(name=';ree n', value='When you just wanna express yourself', inline=False)
			if 'REE' in args: embed.add_field(name=';REE n', value="Try **;REE 100**, why don't you.", inline=True)
			if 'AAA' in args: embed.add_field(name=';AAA n', value="You get the point.", inline=True)
			if 'good' in args: embed.add_field(name=';good bot', value='If you ever wanna appreciate this good-for-nothing ~~slave~~ bot.', inline=False)
			if 'help' in args: embed.add_field(name=';help', value='Displays this **help** card', inline=False)

			await ctx.send(author, embed=embed)	

	@commands.command()
	async def ping(self, ctx):
		if ctx.message.author.id in cloff_dict['devs']:
			await ctx.send(f'{round(self.client.latency*1000)}ms')
		else:
			k = random.randint(1,100)
			if 1<=k<=80:
				await ctx.send("Fuck you.")
			elif 80<k<=99:
				await ctx.send(f'{round(self.client.latency*1000)}ms')
			elif k == 100:
				await ctx.send("Pong!")
		
	@commands.command(aliases=["yeet", "yeetus", "dismiss", "remove", "rm", "clear"])
	async def purge(self, ctx, n=1):
		if n>=100:
			await ctx.send("Fuck no")
		else:    
			#await ctx.send(ctx.log_froms(ctx.get_channel(discord.utils.get(ctx.guild.channels, name=given_name).id), 100))
			await ctx.channel.purge(limit=n+1)


	@commands.command()
	async def ree(self, ctx, n=50):
		await ctx.send('r'+int(n)*'e')

	@commands.command()
	async def REE(self, ctx, n=50):
		await ctx.send('R'+int(n)*'E')

	@commands.command()
	async def hmm(self, ctx, n=20):
		await ctx.send('h'+int(n)*'m')
	
	@commands.command()
	async def AAA(self, ctx, n=50):
		await ctx.send(int(n)*"A")

	@commands.command()
	async def cuss(self, ctx, argument):
		cusses = ["Fuck you", "Fuck you too", "Nobody loves you", "You're going to die alone", "You got cooties"]
		phrase = cusses[random.randint(0, len(cusses)-1)]
		await ctx.send(f"{phrase} {argument}")
	
	@commands.command(aliases = ['hi', 'sup', 'yo'])
	async def hello(self, ctx):
		list = ["Hi", "Hello", "Sup", "How's it going", "Yo"]
		name = ' '
		if random.randint(0,1) == 1:
			name = str(ctx.message.author)[:-5]
		await ctx.send(f'{list[random.randint(0, len(list)-1)]} {name}')
		print(ctx.message.author.id)

	@commands.command(aliases=['say'])
	async def echo(self, ctx, *, arg):
		await ctx.send(arg)

	@commands.command(aliases=['good'])
	async def good_boy(self, ctx, arg):
		list = ["boy", "girl", "boi", "gorl", "bot", "cloff", "cloffo"]
		if arg in list:
			await ctx.send("uwu themk :orange_heart:")

	@commands.command(aliases=["roast"])
	async def bully(self, ctx, argument=""):
		if argument:	
			list = open(cloff_dict['path_to_file']+"/database/bullying.txt").read()
			split_list = list.split("\n")
			bully_quote = random.choice(split_list)
			while not bully_quote:
				bully_quote = random.choice(split_list)
			await ctx.send(f"{argument}\n{bully_quote}")
		else: await ctx.send("Who do you wanna bully, shithead")
		
	@commands.command()
	async def spam(self, ctx, *argument):
		argument = list(argument)
		times = 10
		try:
			if type(int(argument[-1])) is int:
				times = int(argument[-1])
				argument.pop()
		except Exception as e:
			print(e)
		if times > 10:
			try:
				await ctx.send("Ew no not gonna spam that many")
			except Exception as e:
				print(e)
		else:
			try:
				if not argument:
					await ctx.send('Okay, but spam WHAT')
				else:
					for i in range(times):
						await ctx.send(" ".join(argument))
						time.sleep(0.5)
			except Exception as e:
				print(e)

	@commands.command(aliases = ['color'])
	async def colour(self, ctx, hex_string):
		try:
			R = int(hex_string[:2], 16)
			G = int(hex_string[2:4], 16)
			B = int(hex_string[4:], 16)
			img = np.full([100,100,3], np.array([B,G,R]), dtype=np.uint8)

			image_path = cloff_dict['path_to_file']+f"/images/hex_images/{hex_string}.png"

			cv.imwrite(image_path, img)
			file = discord.File(image_path)
			await ctx.send(f"HEX: {hex_string}\nRGB: {[R,G,B]}", file=file)
		except Exception as e:
			await self.client.get_channel(cloff_dict['error_channel_id']).send(e)


def setup(cloff):
	cloff.add_cog(cloff_the_bot(cloff))
