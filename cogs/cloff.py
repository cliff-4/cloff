import discord
from discord.ext import commands
import os
import random
import datetime
import time

class cloff_the_bot(commands.Cog):

	def __init__(self, cloff):
		self.client = cloff
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('bitch im ready')

	@commands.command(aliases=['p'])
	async def ping(self, ctx):
		k = random.randint(1,100)
		if 1<=k<=80:
			await ctx.send("Fuck you.")
		elif 80<k<=99:
			await ctx.send(f'{round(self.client.latency*1000)}ms')
		elif k == 100:
			await ctx.send("Pong!")
		
	@commands.command()
	async def cursed(self, ctx):
		dir = path_to_file + "/images/cursedcomments"
		await ctx.send(file=discord.File(f"{dir}/{os.listdir(dir)[random.randint(0,len(os.listdir(dir))-1)]}"))

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

	@commands.command(aliases=['h'])
	async def help(self, ctx):
		author = None #ctx.message.author
		embed = discord.Embed(
			colour = discord.Colour(0xe08e00)
		)
		embed.set_author(name="Help")

		embed.add_field(name=';cursed', value='Sends a cursed image from the interwebs', inline=False)
		embed.add_field(name=';purge n', value='Purges last n messages.', inline=False)
		embed.add_field(name=';ping', value='returns Pong! I swear. Try it.', inline=False)
		embed.add_field(name=';ree n', value='When you just wanna express yourself', inline=False)
		embed.add_field(name=';REE n', value="Try ;REE 100, why don't you.", inline=False)
		embed.add_field(name=';help', value='Displays this help card', inline=False)

		await ctx.send(author, embed=embed)
	
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
	async def bully(self, ctx, argument="who do you want to bully, shithead"):
		list = """Some people just need a high five. In the face. With a chair.
It's a shame you can't Photoshop your personality.
I don't hate you, but I might unplug your life support to change my phone.
Don't you get tired of putting make-up on two faces every morning?
Oh you're talking to me, I thought you only talked behind my back.
My phone battery lasts longers than your relationships.
When karma comes back to punch you in the face, I want to be there in case it needs help.
I'm sorry you got offended that one time you were treated the way you treat everyone all the time. 
Maybe you should eat make-up so you'd be pretty on the inside too.
Whoever told you to be yourself gave you really bad advice.
I didn't change. I grew up. Maybe you should try it some time.
Where's your off button?
If I had a face like yours, I'd sue my parents.
90% of your "beauty" could be removed with a Kleenex.
Hey, I found your nose, it's in my business again!
I'm not an astronomer but I'm pretty sure the Earth revolves around the Sun, not you.        
Keep rolling your eyes. Maybe you'll find your brain back there.
I'd explain it to you, but I left my English-To-Dumbass Dictionary at home.
It looks like your face caught fire and someone tried to put it out with a fork.
Sometimes, I don't know whether I should hate you or pity you.
You're so fake Barbie's jealous.
Remember that time when you had an original comeback? Me neither!
Go step on a Lego.
Did it hurt when you fell from heaven? Because it looks like you landed on your face.
I bet you spent all night thinking of that one!
Some babies got dropped on their heads but you were clearly thrown against a wall.
Wanna know what makes me laugh? Not you!
Do you have bad luck when it comes to thinking?
Make-up might be doing a good job at covering your ugly face but we can still see your hideous personality.
Was that supposed to be offensive?
I've met fridges hotter than you.
Someday you'll go far... And I hope you'll stay there.
Aww, it's so cute when you try to talk about things you don't understand.
Brains aren't everything. In your case, they're nothing.
I'm sorry I didn't get that - I don't speak Idiot.
I'd slap you, but I don't want to make your face look any better.
You have the right to remain silent because whatever you say will be stupid anyway."""
		split_list = list.split("\n")
		await ctx.send(split_list[random.randint(0, len(split_list)-1)])

	@commands.command()
	async def spam(self, ctx, argument='', times=5):
		if times > 10:
			try:
				await ctx.send("Ew no not gonna spam that many")
			except Exception as e:
				await ctx.send(e)
		else:
			try:
				if not argument:
					await ctx.send('Okay, but spam WHAT')
				else:
					for i in range(times):
						await ctx.send(argument)
						time.sleep(0.69)
			except Exception as e:
				await ctx.send(e)

#    @commands.Cog.listener()
#    async def on_message(self, message):
#        if message.author == cloff.user:
#            return
#        else:
#            k = False
#            for term in ['boy', 'girl', 'boi', 'gorl', 'slave', 'cloffo', 'cloff']:
#                if (f"good {term}" in message.content):
#                    k = True
#            if k:
#                await message.channel.send(f"uwu thanks {str(message.author)[:-5]}")

	@commands.command()
	async def quote(self, ctx):
		k = None



def setup(cloff):
	cloff.add_cog(cloff_the_bot(cloff))
