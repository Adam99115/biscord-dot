import os
import discord
from dotenv import load_dotenv
from discord.ext import tasks

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')
client = discord.Client()

@client.event
async def on_read():
        print("I've arrived")
        
@client.event
async def on_message(message):
       print("I've received", message)
       StonksChecker = Daemon()

class Daemon():
    ##Background checker that can routinely check my stocks for me
    def __init__(self):
        self.interval = 0
        self.daemon_task.start()

    @tasks.loop(seconds=3)
    async def daemon_task(self):
        print(self.interval)
        self.interval += 1
        
client.run(token)

#TODO : Add command handling, selenium for stocks / news updates, MOTDS, music / spotify playlist player ?