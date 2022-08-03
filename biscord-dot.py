import os
import discord
import time
from datetime import datetime
import json
from dotenv import load_dotenv
from discord.ext import commands, tasks
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')
ownerId = os.getenv('OWNER_ID')
bot = commands.Bot(command_prefix='`')

@bot.event
async def on_ready():
    StonksChecker = Daemon()

def getStockValue(exchange: str, stock: str):
    browser.get('https://www.google.com/finance/quote/' + stock + ':' + exchange)
    stockPrice = browser.find_element(By.CLASS_NAME, 'kf1m0').text
    dayPercentage = browser.find_element(By.CLASS_NAME, 'JwB6zf').get_property('textContent')
    print(dayPercentage)
    color = browser.find_element(By.CLASS_NAME, 'VOXKNe').value_of_css_property('color')
    if (color == 'rgba(165, 14, 14, 1)'):
        description = " down " + dayPercentage
    else: 
        description = " up " + dayPercentage
    return ('-' * 4 + exchange + ':' + stock + ' is ' + stockPrice + description)

@bot.command()
async def stonk(ctx, *args):
    exchange = args[0]
    stock = args[1]
    await ctx.author.send(getStockValue(exchange=exchange, stock=stock))

class Daemon():
    ##Background checker that can routinely check my stocks for me
    def __init__(self):
        self.interval = 0
        self.daemon_task.start()

    @tasks.loop(minutes=30)
    async def daemon_task(self):
        stocks = json.loads(os.getenv('STOCKS'))
        owner = await bot.fetch_user(ownerId)
        await owner.send("Stocks update at " + datetime.now().strftime("%H:%M:%S"))
        for stonk in stocks:
            code, exchange = stonk.split(':')
            time.sleep(1)
            value = getStockValue(exchange,code)
            await owner.send(value)
        
bot.run(token)
#TODO: Add command handling, 
#TODO: news updates, MOTDS, music / spotify playlist player ?
#TODO: get personalIp for owner.