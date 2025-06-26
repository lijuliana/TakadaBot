import discord
import random
import json
import math
import time 
from typing import cast
from discord.ext import tasks
from discord.ext import commands
from discord.ext.commands import has_permissions, BucketType, CommandOnCooldown
import asyncio
import os
import praw 

class RedditCog(commands.Cog): 
  def __init__(self, client): 
    self.client = client
    self.reddit=None
    self.reddit = praw.Reddit(client_id = os.getenv('REDDIT_ID'),
                            client_secret=os.getenv('REDDIT_SECRET'),
                            username="juls_li", 
                            password = os.getenv('REDDIT_PASS'),
                            user_agent="pythonpraw")
    
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error): 
    
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("A required argument is missing!")

    elif isinstance(error, commands.CommandOnCooldown):
      await ctx.send(f"You're on cooldown for `{error.retry_after:,.2f} seconds`!")

    elif isinstance(error, commands.MissingPermissions):
      await ctx.send("You do not have permission to run this command!")

  @commands.command(aliases=['subreddit', 'subs'])
  async def subreddits(self, ctx):
    embed = discord.Embed(
      title = '<a:d_pray:746183142359957504> available subreddits:',
      description = '✑；r/takadabear\nキ；r/cats\n✑；r/aww\nキ；r/sneks\n✑；r/kittens\nキ；r/memes\n✑；r/ihadastroke\nキ；r/rarepuppers\n✑；r/surrealmemes\nキ；r/mildlyinteresting\n✑；r/im14andthisisdeep\nキ；r/technicallythetruth\n\n*use `t?r [subreddit]` to view posts!*',
      colour = discord.Colour.from_rgb(47, 49, 55)
    )
    await ctx.send(ctx.author.mention, embed=embed)

  @commands.command(aliases=['rand', 'r']) 
  @commands.cooldown(1, 5, BucketType.user)
  async def random (self, ctx, subreddit:str=""): 
    async with ctx.channel.typing():
      try:
        if self.reddit:
          choices=['surrealmemes', 'ihadastroke', 'takadabear', 'memes', 'aww', 'sneks', 'cats', 'kittens', 'rarepuppers', 'mildlyinteresting', 'technicallythetruth', 'im14andthisisdeep']
          chosen_subreddit=random.choice(choices)
          if subreddit:
            if subreddit in choices:
              chosen_subreddit=subreddit
            else:
              await ctx.send("view available subreddits using t?subreddits!")
              return
          
          all_subs=[]
          submissions=self.reddit.subreddit(chosen_subreddit).hot(limit=50)
          for sub in submissions: 
            if not sub.stickied and "v.redd.it" not in sub.url and "/comments/" not in sub.url and "gfycat.com" not in sub.url and "reuters.com" not in sub.url and "theguardian.com" not in sub.url and "sciencemag.org" not in sub.url and "youtube.com" not in sub.url and "imgur.com" not in sub.url:
              all_subs.append(sub)
            # if sub.media and not sub.stickied and 'reddit_video' not in sub.media:
            #    all_subs.append(sub)
          submission=random.choice(all_subs)

          if not submission.over_18:
            imgurl=submission.url
            embed = discord.Embed(
              title = f'r/{chosen_subreddit}',
              description = submission.title,
              colour = discord.Colour.from_rgb(47, 49, 55)
            )
            embed.set_footer(text=f'{submission.score} upvotes')
            embed.set_image(url=imgurl)
            await ctx.send(ctx.author.mention, embed=embed)
          else:
            await ctx.send("no nsfw subreddits! <a:b_bad2:743580332359417956>")

        else:
          await ctx.send("Error! Please contact @jelly#100")
      except:
        await ctx.send("This subreddit does not exist, or there are not enough image posts :(")


def setup(client): 
  client.add_cog(RedditCog(client)) 
  print('Reddit loaded')