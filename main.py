import discord,os
from discord.ext import commands 

bot = commands.Bot(command_prefix='?')

from os import listdir

for file in listdir('cogs/'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

dissecret = os.environ['TOKEN']

try:
    bot.run(dissecret)
except discord.errors.HTTPException:
    print("blocked by rate limits restarting now")
    os.system("python restarter.py")
    os.system("kill 1")
