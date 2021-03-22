import os
import re
import requests
import praw
import configparser
import concurrent.futures
import argparse
import discord
from discord.ext import commands
#import random
#import datetime

class redditImageScraper(commands.Cog):
    def __init__(self, sub, limit, order, nsfw=False):
        
        config = configparser.ConfigParser()
        config.read('./cloff/conf.ini')
        self.sub = sub
        self.limit = limit
        self.order = order
        self.nsfw = nsfw
        self.path = f'images/{self.sub}/'
        self.reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],
                                  client_secret=config['REDDIT']['client_secret'],
                                  user_agent='Multithreaded Reddit Image Downloader v2.0 (by u/impshum)')


    def download(self, image):
        r = requests.get(image['url'])
        with open(image['fname'], 'wb') as f:
            f.write(r.content)
        print(r)
        return str(image['url'])

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
        return self.download


class cloff_reddit_image_sender(commands.Cog):

    def __init__(self, cloff):
        self.client = cloff
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('reddit image downloader package ready')

    @commands.command()
    async def reddit(self, ctx, sub):
        await ctx.send(redditImageScraper(sub, 1, 'hot').start())



def setup(cloff):
    cloff.add_cog(cloff_reddit_image_sender(cloff))
