from discord.ext import commands

bot = commands.Bot(prefix_char='#')
token = 'NTI5MTQwNDA2NjQyODAyNzE5.DwshGA.sbD1HzSDR_weliLs-Tg2kpmwwU8'

@bot.event
asyn def on_ready():
 print('Logged as:'+bot.user.name+' '+bot.user.id)

bot.run(token)
