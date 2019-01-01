from discord.ext import commands

bot = commands.Bot(command_prefix='#')
token = 'NTI5MTQwNDA2NjQyODAyNzE5.DwshGA.sbD1HzSDR_weliLs-Tg2kpmwwU8'

@bot.event
async def on_ready():
 print('Logged as:'+bot.user.name+' '+bot.user.id)

bot.run(token)
