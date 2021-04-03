import discord
from discord.ext import commands
import json
from spellchecker import SpellChecker

class dictionaryyy(commands.Cog):

	def __init__(self, cloff):
		self.client = cloff

		self.entire_dictionary = {}

		for i in range(1, 27):
			A = chr(96+i).upper()
			with open(cloff_dict['path_to_file'] + f'/database/dictionary/D{A}.json', 'r') as myfile: self.entire_dictionary[A] = json.loads(myfile.read())
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('dictionary ready')

	@commands.command(aliases=['d', 'D', 'dict', 'Dict'])
	async def dictionary(self, ctx, word):
		try:
			word = word.upper()
			tip = ''
			if word[-1] == 'S': tip='\n_Tip: If the argument is plural, try passing the argument in singular form._'
			definition = self.entire_dictionary[word[0]][word]["MEANINGS"]
			if not definition:
				await ctx.send(f"Sorry, but I don't know the meaning of **{word.lower()}** :({tip}")
			else:
				verbs = []
				nouns = []
				for i in list(definition):
					if definition[i][0].lower() == 'verb': verbs.append(f"_{definition[i][0]}_ {chr(8226)} {definition[i][1].capitalize()}")
					if definition[i][0].lower() == 'noun': nouns.append(f"_{definition[i][0]}_ {chr(8226)} {definition[i][1].capitalize()}")
				verbs = "\n".join(verbs[:min(3, len(verbs))])
				nouns = "\n".join(nouns[:min(3, len(nouns))])
				embed = discord.Embed(colour= discord.Colour(0xff0000))
				embed.set_author(name='Definition')
				embed.add_field(name=f'"{word.capitalize()}"', value=f"\n{nouns}\n{verbs}")
				await ctx.send(embed=embed)

		except KeyError:
			try:
				if bool(SpellChecker().known([word])):
					await ctx.send(f"Sorry, but I don't know the meaning of **{word.lower()}** :( Perhaps the archives are incomplete.{tip}")
				else:
					if word in SpellChecker().candidates(word):
						await ctx.send(f"Sorry, but I don't know the meaning of **{word.lower()}** :({tip}")
					else:
						await ctx.send(f"That word might be wrong. Did you instead mean any of these:\n**{', '.join(SpellChecker().candidates(word))}**{tip}")
			except Exception as e:
				await self.client.get_channel(cloff_dict['error_channel_id']).send(e)

		except Exception as e:
			await self.client.get_channel(cloff_dict['error_channel_id']).send(e)

def setup(cloff):
	cloff.add_cog(dictionaryyy(cloff))
