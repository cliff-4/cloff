import os
import re
import requests
import asyncpraw
from configparser import ConfigParser #
import concurrent.futures
import argparse
import praw #
import discord #
from discord.ext import commands #
#import random
#import datetime

class redditImageScraper(commands.Cog):
	def __init__(self, sub, limit, order, nsfw=False):
		
		config = configparser.ConfigParser()
		config.read(path_to_file + '/conf.ini')
		self.sub = sub
		self.limit = limit
		self.order = order
		self.nsfw = nsfw
		self.path = f'images/{self.sub}/'
		self.reddit = asyncpraw.Reddit(client_id=config['REDDIT']['client_id'],
								  client_secret=config['REDDIT']['client_secret'],
								  user_agent='Multithreaded Reddit Image Downloader v2.0 (by u/impshum)')


	def download(self, image):
		r = requests.get(image['url'])
		with open(image['fname'], 'wb') as f:
			f.write(r.content)

	def start(self):
		images = []
		try:
			go = 0
			if self.order == 'hot':
				submissions = self.reddit.subreddit(self.sub).hot(limit=None)
			elif self.order == 'top':
				submissions = self.reddit.subreddit(self.sub).top(limit=None)
			elif self.order == 'new':
				submissions = self.reddit.subreddit(self.sub).new(limit=None)

			for submission in submissions:
				if not submission.stickied and submission.over_18 == self.nsfw \
					and submission.url.endswith(('jpg', 'jpeg', 'png')):
					fname = self.path + re.search('(?s:.*)\w/(.*)', submission.url).group(1)
					if not os.path.isfile(fname):
						images.append({'url': submission.url, 'fname': fname})
						go += 1
						if go >= self.limit:
							break
			if len(images):
				if not os.path.exists(self.path):
					os.makedirs(self.path)
				with concurrent.futures.ThreadPoolExecutor() as ptolemy:
					ptolemy.map(self.download, images)
		except Exception as e:
			print(e)

info = ConfigParser()
info.read(path_to_file + '/conf.ini')
client_id = info["REDDIT"]["client_id"]
client_secret = info["REDDIT"]["client_secret"]

class reddit_images(commands.Cog):
	def __init__(self, cloff):
		self.client = cloff
		self.reddit = None
		if client_id and client_secret:
			self.reddit = praw.Reddit(
				client_id=client_id,
				client_secret=client_secret,
				user_agent="Kudasaiii onii-chan!!"
			)
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('reddit image downloader package ready')

	@commands.command()
	async def r(self, ctx, sub="pics"):
		if self.reddit:
			if 
		else:
			await ctx.send("This command isn't working. Please contact the administrator")
		

def setup(cloff):
	cloff.add_cog(reddit_images(cloff))
