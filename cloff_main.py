#!/usr/bin/env python3

import discord
from discord.ext import commands
import os
import datetime
from configparser import ConfigParser
import builtins

__builtins__.path_to_file = str(os.path.dirname(os.path.abspath(__file__)))
info = ConfigParser()
info.read(path_to_file + '/conf.ini')
my_ass = info['DISCORD']['token']

time_start = datetime.datetime.now()

cloff = commands.Bot(command_prefix=";")
cloff.remove_command('help')

cog_list = []
for cog in os.listdir(path_to_file + "/cogs"):
    if cog.endswith(".py"):
        cog_list.append(cog[:-3])

print('\n###########################################')

@cloff.command(aliases=['l'])
async def reload(ctx, extention='vyuyteaiuycniyauwtdnaxiwtnaditzyweuxdiytnecbu'):
    if ctx.message.author.id != 700376271355379823:
        await ctx.send("You do not have permission to run this command :pig_nose:")
    else:
        if extention=='vyuyteaiuycniyauwtdnaxiwtnaditzyweuxdiytnecbu':
            try:
                for ext in cog_list:
                    if ctx.message.author.id == 700376271355379823:
                        cloff.unload_extension(f'cogs.{ext}')
                        cloff.load_extension(f'cogs.{ext}')
                        await ctx.send(f"reloaded {ext}")                    
            except Exception as e:
                await ctx.send(e)
        else:
            try:
                cloff.unload_extension(f'cogs.{extention}')
                cloff.load_extension(f'cogs.{extention}')
                await ctx.send(f"{extention} reloaded")
            except Exception as e:
                await ctx.send(e)


@cloff.command()
async def uptime(ctx):
    uptime = str(datetime.datetime.now()-time_start).split(":")
    await ctx.send(f"cloff has been online for {uptime[0]} hours, {uptime[1]} minutes and {round(float(uptime[2]))} seconds.")

for filename in cog_list:
    cloff.load_extension(f"cogs.{filename}")

cloff.run(my_ass)
