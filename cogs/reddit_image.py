import os
#import re
#import requests
#import asyncpraw
from configparser import ConfigParser #
#import concurrent.futures
#import argparse
import praw
import discord #
from discord.ext import commands #
import random
import asyncio
#import datetime

class reddit_images(commands.Cog):
	def __init__(self, cloff):

		info = ConfigParser()
		info.read(path_to_file + '/conf.ini')
		self.client = cloff
		self.reddit = praw.Reddit(
				client_id = info["REDDIT"]["client_id"],
				client_secret = info["REDDIT"]["client_secret"],
				user_agent="A very kawaii discord bot",
				check_for_async = False
			)

	@commands.Cog.listener()
	async def on_ready(self):
		print('RID package ready') #Reddit Image Downloader
		

	@commands.command(aliases=["reddit", "Reddit", "R"])
	async def r(self, ctx, sub="dankmemes"):
		try:
			k = self.reddit.subreddit(sub)
			if not k.over18:
				submissions = k.hot()
				for i in range(0, random.randint(1, 10)):
					submission = next(x for x in submissions if not x.stickied)
				await ctx.send(f'"{submission.title}"\n{submission.url}')
			else:
				submissions = k.hot()
				for i in range(0, random.randint(1, 10)):
					submission = next(x for x in submissions if not x.stickied)
				await ctx.send(f'**[NSFW]**\n"{submission.title}"\n_(Requested by <@!{ctx.message.author.id}>)_\n{submission.url}')
		except Exception as e:
			await ctx.send(e)

def setup(cloff):
	cloff.add_cog(reddit_images(cloff))
