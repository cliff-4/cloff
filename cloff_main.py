import discord
from discord.ext import commands
import os
import datetime

my_ass = 'ODIxMDk3OTE2MTk3MzcyMDA0.YE-xBg.Y_dCag6rtq5YcNj8DDrG5n7wQTU'

time_start = datetime.datetime.now()

cloff = commands.Bot(command_prefix=";")
cloff.remove_command('help')

@cloff.command(aliases=['l'])
async def reload(ctx, extention='cloff'):
    if ctx.message.author.id == 700376271355379823:
        cloff.unload_extension(f'cogs.{extention}')
        cloff.load_extension(f'cogs.{extention}')
        await ctx.send("Commands reloaded")
    else:
        await ctx.send("You do not have permission to run this command :pig_nose:")

@cloff.command()
async def uptime(ctx):
    uptime = str(datetime.datetime.now()-time_start).split(":")
    await ctx.send(f"cloff has been online for {uptime[0]} hours, {uptime[1]} minutes and {round(float(uptime[2]))} seconds.")

for filename in os.listdir("/windowshare/shubbu's stuff/do not disturb/EXTRA_DND/cogs/"):
    if filename.endswith('.py'):
        cloff.load_extension(f"cogs.{filename[0:-3]}")

cloff.run(my_ass)