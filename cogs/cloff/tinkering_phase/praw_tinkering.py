import praw
from configparser import ConfigParser

config = ConfigParser()
config.read('./conf.ini')



info = ConfigParser()
info.read('./conf.ini')
my_ass = info['DISCORD']['token']
print(my_ass)