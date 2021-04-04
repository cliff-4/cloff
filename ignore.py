import os, json, datetime
path_to_file = str(os.path.dirname(os.path.abspath(__file__)))

if 1:
	with open(path_to_file + f'/database/water.json', 'r+') as f:
		data = json.load(f)
		data['last_poing'] = str(datetime.datetime.now()) # <--- add `id` value.
		f.seek(0)        # <--- should reset file position to the beginning.
		json.dump(data, f, indent="\t")
		f.truncate()     # remove remaining par

last_poing = datetime.datetime.strptime(data["last_poing"], '%Y-%m-%d %H:%M:%S.%f')
print(datetime.datetime.now()-last_poing)
