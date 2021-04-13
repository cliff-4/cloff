import os
#import re
#import requests
from configparser import ConfigParser
#import concurrent.futures
import praw
import discord
from discord.ext import commands
import random
import asyncio
import traceback

class reddit_images(commands.Cog):
	def __init__(self, cloff):
		info = ConfigParser()
		info.read(cloff_dict['path_to_file'] + '/conf.ini')
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
			if (k.over18) and (not (ctx.channel.is_nsfw())):
				await ctx.send("Can't post that here. The post is NSFW but the channel is not!")
			else:
				submissions = k.hot()
				for i in range(0, random.randint(1, 20)):
					submission = next(x for x in submissions if not x.stickied)
				kk = ''
				if k.over18:
					kk = f'_(Requested by <@!{ctx.message.author.id}>)_\n'
				await ctx.send(f'{kk}**{submission.title}**\nby u/{submission.author.name} (from r/{submission.subreddit.display_name})\n{submission.url}')
		except Exception as e:
			await self.client.get_channel(cloff_dict['error_channel_id']).send(f"{traceback.format_exc()} for [{ctx.message.content}]")

def setup(cloff):
	cloff.add_cog(reddit_images(cloff))
