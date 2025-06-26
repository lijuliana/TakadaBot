import discord
import random
import json
import math
import datetime 
from datetime import timezone, tzinfo, timedelta
import sys
from typing import cast
from discord.ext import tasks
from typing import Union,TypeVar
from discord.ext.commands import has_permissions, cooldown, BucketType
from discord.ext import commands
from webserver import keep_alive
import asyncio
import os
import time
import time as timeModule

client=commands.Bot(command_prefix=['t?', 'T?', '<@!749025785704087593> ', '<@!749025785704087593>', '<@749025785704087593>', '<@749025785704087593> '], case_insensitive=True)
client.remove_command('help')

globalt=datetime.datetime.now()

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity = discord.Game('t?help ; r/takadabear'))
  print('Bot is ready.')


@client.command()
@has_permissions(administrator=True)
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
@has_permissions(administrator=True)
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_member_join(member):
  global m
  print(f'{member} has joined!')


@client.event
async def on_member_remove(member):
  print(f'{member} has left :(')
  

@client.event
async def on_message(message):
  channel = message.channel
  msg=str(message.content)
    
  await client.process_commands(message)


@client.command(aliases=['help'])
async def commands(ctx, cmd=None):
  if cmd==None:
    embed = discord.Embed(
      title = 'commands:',
      description = "\n`t?ping`\n`t?count`\n`t?date`\n`t?av @user`\n`t?invert @user`\n`t?enlarge [emoji]`\n\n**takadabear**\n`t?bear`\n`t?dog`\n`t?otter`\n`t?other`\n`t?boom boom`\n\n**reddit**\n`t?subreddits`\n`t?random [subreddit]`\n\n**links**\n✑；invite takadabot (wip)\n[ヾ；our server](https://discord.gg/rf7DkpQ)\n[✑；r/takadabear](https://www.reddit.com/r/takadabear/)\n[ヾ；takadabear's website](https://www.takadabear.com/)\n\n**use `t?help [command]` for\nmore info on each command!**",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
    embed.set_footer(text='@jelly#1000', icon_url='https://cdn.discordapp.com/emojis/738530291756564490.gif?v=1')
  elif cmd=='ping':
    embed = discord.Embed(
      title = 't?ping',
      description = "<:d_ping:740972507141505024> displays the ping time or latency of the bot in milliseconds",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
  elif cmd=='count' or cmd=='membercount' or cmd=='members':
    embed = discord.Embed(
      title = 't?count',
      description = "<a:d_stack:739945747092340748> server's member count (including bots)",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
  elif cmd=='date' or cmd=='time':
    embed = discord.Embed(
      title = 't?date',
      description = "<a:b_ok:746178660523966514> shows the day, date, and time (GMT)",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
  elif cmd=='av' or cmd=='avatar' or cmd=='av @user' or cmd=='avatar @user' or cmd=='pfp' or cmd=='pfp @user':
    embed = discord.Embed(
      title = 't?av @user',
      description = "<a:d_hug2:743581294549532765> enlarges the pfp/avatar of a user\n",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
    embed.set_footer(text="@user: user mention, user's id, or user's name (w/o spaces). leave empty to see your own avatar!")
  elif cmd=='invert':
    embed = discord.Embed(
      title = 't?invert @user',
      description = "wip <a:cat_nod:740790758373720065>\n",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
    embed.set_footer(text="@user: user mention, user's id, or user's name (w/o spaces). leave empty to invert your own pfp!")
  elif cmd=='enlarge' or cmd=='emote' or cmd=='emoji':
    embed = discord.Embed(
      title = 't?enlarge [emote]',
      description = "<:o_shell:746491798813147226> shows a larger version of your emote!",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
    embed.set_footer(text="[emote]: custom emoji from any server")
  elif cmd=='bear':
    embed=discord.Embed(
      title='t?bear',
      description="<a:b_clap:739884362106929205> takadabear bear gifs from [our discord server](https://discord.gg/rf7DkpQ)!",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
  elif cmd=='dog':
    embed=discord.Embed(
      title='t?dog',
      description="<a:d_hulahoop:743574088349515816> takadabear dog gifs from [our discord server](https://discord.gg/rf7DkpQ)!",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
  elif cmd=='otter':
    embed=discord.Embed(
      title='t?otter',
      description="<a:o_cheer:746489869165002922> takadabear otter gifs from [our discord server](https://discord.gg/rf7DkpQ)!",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
  elif cmd=='other':
    embed=discord.Embed(
      title='t?other',
      description="<:oth_chicken:747536942853521430> other takadabear gifs from [our discord server](https://discord.gg/rf7DkpQ)!",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
  elif cmd=='boom' or cmd=='boom boom':
    embed=discord.Embed(
      title='t?boom boom',
      description="<a:b_pray:738610824775729164> test it out hehe",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
  elif cmd=='subreddits' or cmd=='subs' or cmd=='subreddit':
    embed=discord.Embed(
      title='t?subreddits',
      description="<a:b_pointup:739954432539623567> shows available subreddits for `t?r [subbreddit]`!",
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
  await ctx.send(embed=embed)

@client.command(aliases=['date'])
async def time(ctx):
  t=datetime.datetime.now()
  tt=t.strftime("%A, %B %d %Y\n%I:%M %p (GMT)")
  embed = discord.Embed(
    colour = discord.Colour.from_rgb(47, 49, 55)
  )
  embed.set_footer(text=tt)
  await ctx.send(embed=embed)

@client.command(aliases=['count', 'membercount'])
async def members(ctx):
  countembed = discord.Embed(
    colour = discord.Colour.from_rgb(47, 49, 55)
  )
  countembed.set_footer(text=f'members: {ctx.guild.member_count}', icon_url='https://cdn.discordapp.com/emojis/738530291756564490.gif?v=1')
  await ctx.send(embed=countembed)

@client.command()
async def ping(ctx):
  await ctx.send(f'pOngo BoNGo! {round(client.latency * 1000)}ms')


#cooldown, error messages
#logs dms
#smth to do with dms
#t?invite command
#suggest cmd
#wyr, qotda
#https://discord.com/api/oauth2/authorize?client_id=749025785704087593&permissions=67497025&scope=bot

#future w/ databases:
#change prefix
#embeds
#autoresponder
#economy
#levels

keep_alive()
client.run(os.getenv('SECRET_KEY'))