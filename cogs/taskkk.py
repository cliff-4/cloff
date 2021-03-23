import discord
from discord.ext import tasks, commands

class task_uwu(commands.Cog):

    def __init__(self, cloff):
        self.index = 0
        self.printer.start()
        print("0")
        print("0")
        print("0")

    def cog_unload(self):
        self.printer.cancel()
    
    @tasks.loop(seconds=2)
    async def printer(self):
        print(self.index)
        self.index += 2

def setup(cloff):
    cloff.add_cog(task_uwu(cloff))