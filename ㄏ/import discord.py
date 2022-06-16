import discord
from discord.ext import commands
import googletrans
import os
from pprint import pprint
import json

with open('Setting.json','r',encoding='utF8') as Sfile:
    Sdata = json.load(Sfile)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='p!', intents=intents)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(869640110507978762)
    print(F'@{member} 加入了💥在這看規則')

@bot.event
async def on_member_remove(member):
    print(F'@{member} 從地表上消失了😲')

# 起動時呼叫
@bot.event
async def on_ready():
    print('''✔ I'm ready''')
    game = discord.Game('ANO遊戲社群')
    await bot.change_presence(status=discord.Status.online, activity=game)


# 收到訊息時呼叫
@bot.event
async def on_message(message):
    # 送信者為Bot時無視
    if message.author.bot:
        return
    
    if bot in message.mentions: # @判定
        translator = googletrans.Translator()
        robotName = bot.name
        first, space, content = message.clean_content.partition('@'+robotName+' ')
        
        if content == '':
            content = first
        if translator.detect(content).lang == Sdata['DST']:
            return
        if translator.detect(content).lang == Sdata['SRC'] or Sdata['SRC'] == '':
            remessage = translator.translate(content, dest='zh-tw').text
            await message.reply(remessage) 

# Bot起動
bot.run(Sdata['TOKEN'])