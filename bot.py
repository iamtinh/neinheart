from discord.ext import commands

bot = commands.Bot(prefix_char='#')
token = ''

@bot.event
asyn def on_ready():
 print('Logged as:'+bot.user.name+' '+bot.user.id)

bot.run(token)
