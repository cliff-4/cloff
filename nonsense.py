import asyncpraw
from configparser import ConfigParser

###############################################
sub = 'cursedcomments'
priority = 'hot'

###############################################

config = ConfigParser()
config.read('./conf.ini')
client_id = config['REDDIT']['client_id']
client_secret = config['REDDIT']['client_secret']

reddit = asyncpraw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="my user agent",
)

@client.command()
async def k(self, ctx):
    subreddit = await reddit.subreddit("learnpython")
    async for submission in subreddit.hot(limit=10):
        print(submission.title)
