import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='#')
token = 'NTI5MTQwNDA2NjQyODAyNzE5.DwshGA.sbD1HzSDR_weliLs-Tg2kpmwwU8'

@bot.event
async def on_ready():
 print('Logged as:'+bot.user.name+' '+bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
 embed = discord.Embed(
  title ='stop'
 )
 embed.set_image(url='https://media3.giphy.com/media/l4Ki2obCyAQS5WhFe/giphy.gif')
 await ctx.send(embed = embed)

bot.run(token)
