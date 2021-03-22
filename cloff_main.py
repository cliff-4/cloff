#!/usr/bin/env python3

import discord
from discord.ext import commands
import os
import datetime
from configparser import ConfigParser

info = ConfigParser()
info.read('./conf.ini')
my_ass = info['DISCORD']['token']

time_start = datetime.datetime.now()

cloff = commands.Bot(command_prefix=";")
cloff.remove_command('help')

@cloff.command(aliases=['l'])
async def reload(ctx, extention='vyuyteaiuycniyauwtdnaxiwtnaditzyweuxdiytnecbu'):
    if ctx.message.author.id != 700376271355379823:
        await ctx.send("You do not have permission to run this command :pig_nose:")
    else:
        if extention=='vyuyteaiuycniyauwtdnaxiwtnaditzyweuxdiytnecbu':
            try:
                for ext in ['cloff', 'reddit_image']:
                    if ctx.message.author.id == 700376271355379823:
                        cloff.unload_extension(f'cogs.{ext}')
                        cloff.load_extension(f'cogs.{ext}')
                        await ctx.send(f"{ext} reloaded")                    
            except Exception as e:
                print(e)
        else:
            try:
                cloff.unload_extension(f'cogs.{extention}')
                cloff.load_extension(f'cogs.{extention}')
                await ctx.send(f"{extention} reloaded")
            except Exception as e:
                print(e)

@cloff.command()
async def uptime(ctx):
    uptime = str(datetime.datetime.now()-time_start).split(":")
    await ctx.send(f"cloff has been online for {uptime[0]} hours, {uptime[1]} minutes and {round(float(uptime[2]))} seconds.")

for filename in os.listdir("./cogs/"):
    if filename.endswith('.py'):
        cloff.load_extension(f"cogs.{filename[0:-3]}")

cloff.run(my_ass)
