import asyncpraw
from configparser import ConfigParser
import asyncio
import os



async def main():
	path_to_file = str(os.path.dirname(os.path.abspath(__file__)))
	key = ConfigParser()
	key.read(path_to_file+'/conf.ini')
	reddit = asyncpraw.Reddit(
		client_id=key["REDDIT"]["client_id"],
		client_secret=key["REDDIT"]["client_secret"],
		user_agent="wow"
	)
	print(reddit.read_only)

if __name__ == "__main__":
	asyncio.run(main())