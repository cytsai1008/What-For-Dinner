# discord bot
import os
import random
import asyncio
import time
import json
import logging
import load_command
from load_command import *

import discord
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='Log/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix="nm!", help_command=None)
help_zh_tw = load_command.help_zh_tw_def()
bot.remove_command("help")

'''
def check_meal(food):
    if food not in ["breakfast", "lunch", "dinner"]:
        return False
'''


# 調用 event 函式庫
@bot.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', bot.user)
    game = discord.Game('nm!help')
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.online, activity=game)


'''
@client.event

async def status():
    game1 = discord.Game('吃拉麵')
    game2 = discord.Game('吃咖哩')
    game3 = discord.Game('吃壽司')
    game4 = discord.Game('吃火鍋')
    game5 = discord.Game('吃麵包')

    async def game_status():
        await client.change_presence(activity=game1)
        await asyncio.sleep(5)
        await client.change_presence(activity=game2)
        await asyncio.sleep(5)
        await client.change_presence(activity=game3)
        await asyncio.sleep(5)
        await client.change_presence(activity=game4)
        await asyncio.sleep(5)
        await client.change_presence(activity=game5)
        await asyncio.sleep(5)

    await game_status()

    await status()
'''


# 如果包含 dinner，機器人回傳 dinner list
@bot.command(Name="help")
async def help(ctx):
    await ctx.send(help_zh_tw)


@bot.command(Name="ping")
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.command()
async def sl(ctx):
    await ctx.send("Social Credit 👎\n"
                   "https://www.idlememe.com/wp-content/uploads/2021/10/social-credit-meme-idlememe.jpg")


@bot.command(Name="add")
async def add(ctx, *args):
    print(args)
    server_id = ctx.message.guild.id
    # args = dict(args)
    try:
        if args[0] not in ["breakfast", "lunch", "dinner"]:
            await ctx.send("錯誤餐名，請輸入\n"
                           "`nm!add breakfast <食物>`\n"
                           "`nm!add lunch <食物>`\n"
                           "`nm!add dinner <食物>`")
        elif args[1] is type(None):
            await ctx.send("錯誤餐名，請輸入\n"
                           "`nm!add breakfast <食物>`\n"
                           "`nm!add lunch <食物>`\n"
                           "`nm!add dinner <食物>`")
        else:
            await ctx.send('{} foods add into database'.format(len(args)-1))
            print(server_id)
            if os.path.exists('db/{}.json'.format(id)):
                with open('db/{}.json'.format(id), 'r') as f:
                    # TODO: Add key to json
                    pass

    except:
        await ctx.send("請輸入\n"
                       "`nm!add breakfast <食物>`\n"
                       "`nm!add lunch <食物>`\n"
                       "`nm!add dinner <食物>`")


with open("token.json", "r") as f:
    token = json.load(f)
token = token["token"]
bot.run(token)
