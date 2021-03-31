import json
from spellchecker import SpellChecker
import os
path_to_file = str(os.path.dirname(os.path.abspath(__file__)))

word = "plate".upper()
with open(path_to_file + f'/database/dictionary/D{word[0]}.json', 'r') as myfile: dict_data = json.loads(myfile.read())

definition = dict_data[word]["MEANINGS"]
try:
	try:
		for i in range(min(4, len(definition))):
			list = definition[str(i+1)]
			print(f"{list[0]}: {list[1].capitalize()}")
	except KeyError:
		spell = SpellChecker()
		list = spell.candidates(word)
		print(f"That word might be wrong. Did you instead mean any of these:\n\n**{', '.join(list)}**")
except Exception as e:
	print(e)
