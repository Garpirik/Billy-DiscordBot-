from ntpath import join
import discord
from random import random, randrange, randint, choice
from discord.ext import commands
import os
client = discord.Client()


# bot = commands.Bot(command_prefix = "e!",intents = discord.Intents.all(),
# case_insenstive= True)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
        if message.author == client.user:
            return
       

        if message.content == 'Boba':
            await message.channel.send('Boba Gay')
        elif message.content == "Ilyaz":
             await message.channel.send('Ilyaz Gay')
             
        else: 
            if message.content == "ilyaz":
                await message.channel.send('Ilyaz Gay')
        if message.content == 'boba':
            await message.channel.send('Boba Gay')
        if message.content == 'Master':
            rn = randrange(0,100)
            if rn >= 50:
                await message.channel.send(f"Dungeon master :sunglasses: Число которое выпало: {rn} ")
                await message.send (rn)
            elif rn<=5:
                await message.channel.send(f"Jabroni, Число которое выпало:{rn}",)
                await message.send(rn)
            else:
                 await message.channel.send("Fucking Slave, Число которое выпало:{rn}",)
                 await message.send(rn)





# @bot.event
# async def on_ready(args):
#     print(f"{bot.user}is online")

# for filename in os.listdir("./cogs"):
#     if filename.endswith(".py"):
#         bot.load_extension(f"cogs.{filename[:-3]}")


        

