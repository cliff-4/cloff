import os, json, datetime
path_to_file = str(os.path.dirname(os.path.abspath(__file__)))

if False:
	with open(path_to_file + f'/database/water.json', 'r+') as f:
		data = json.load(f)
		data['last_poing'] = str(datetime.datetime.now()) # <--- add `id` value.
		f.seek(0)        # <--- should reset file position to the beginning.
		json.dump(data, f, indent="\t")
		f.truncate()     # remove remaining par

	#date_time_str = data["last_poing"]
	#date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
	#print((datetime.datetime.now()-date_time_obj).minutes)

with open(path_to_file + f'/database/water.json', 'r+') as f:
	data = json.load(f)
	print(data['servers'])
