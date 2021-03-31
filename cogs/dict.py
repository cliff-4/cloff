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
			with open(path_to_file + f'/database/dictionary/D{A}.json', 'r') as myfile: self.entire_dictionary[A] = json.loads(myfile.read())
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('dictionary ready')

	@commands.command(aliases=['d', 'D', 'dict', 'Dict'])
	async def dictionary(self, ctx, word): #2 modules loaded and one line of code in __init__()
		word = word.upper()
		definition = self.entire_dictionary[word[0]][word]["MEANINGS"]
		lines = []
		try:
			try:
				for i in range(min(4, len(definition)-1)):
					list = definition[str(i+1)]
					lines.append(f"{list[0]}: {list[1].capitalize()}")
					await ctx.send(f"""{list[0]}: {list[1].capitalize()}""")
			except KeyError:
				spell = SpellChecker()
				list = spell.candidates(word)
				await ctx.send(f"That word might be wrong. Did you instead mean any of these:\n\n**{', '.join(list)}**")
		except Exception as e:
			await ctx.send(e)


def setup(cloff):
	cloff.add_cog(dictionaryyy(cloff))
