import discord
import random
import json
import math
import time 
from typing import cast
from discord.ext import tasks
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
from typing import Union,TypeVar
import os

import io
import PIL.ImageOps 
from PIL import Image, ImageOps
# import requests
from io import BytesIO
# from StringIO import StringIO

class ImagesCog(commands.Cog): 
  def __init__(self, client): 
    self.client = client
   
  @commands.command()
  async def invert(self, ctx, *, user : discord.Member=None):
    await ctx.send("wip, @jelly#1000 is having problems with this cmd, pls dm her if u can help :D")
    # if user!=None:
    #   pfp = user.avatar_url
    # elif user==None:
    #   pfp = ctx.author.avatar_url

    # img = Image.open(fp=pfp) #.convert("RGBA")
    # await ImageOps.invert(img)


    # img = PIL.Image.open(f"{pfp}")
    # im_invert = PIL.ImageOps.invert(img)
    # im_invert.save('newimg.png')
    # with open('newimg.png', 'rb') as fp:
    #   await ctx.send(file=discord.File(fp, 'newimg.png'))
    # await ctx.send(file=discord.File(f'newimg.png'))
    # os.remove('newimg.png')


  @commands.command(aliases=['av', 'pfp'])
  async def avatar(self, ctx, *, user : discord.Member=None):
    if user!=None:
      pfp = user.avatar_url
    elif user==None:
      pfp = ctx.author.avatar_url
    embed = discord.Embed(
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
    embed.set_image(url=pfp)
    await ctx.send(embed=embed)

  @commands.command(aliases=['emote', 'enlarge', 'emoji'])
  async def emotes(self, ctx, *, emote: Union[discord.Emoji, discord.PartialEmoji, str]):
    d_emoji = cast(discord.Emoji, emote)
    ext = "gif" if d_emoji.animated else "png"
    url = "https://cdn.discordapp.com/emojis/{id}.{ext}?v=1".format(id=d_emoji.id, ext=ext)
    embed = discord.Embed(
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
    embed.set_image(url=url)
    member=ctx.author
    await ctx.send(f'{member.mention}', embed=embed)


def setup(client): 
  client.add_cog(ImagesCog(client)) 
  print('Images loaded')