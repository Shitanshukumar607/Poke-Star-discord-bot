import discord 
from discord.ext import commands,tasks
import asyncio


past_message = None
new_message = None

spammer1_id = 1223878867027230735
spammer2_id = 783543227189297192


spam_channel_1 = 1223899187519688734
spam_channel_2 = 1235593275143094294




ping_channel_id = 1235590585298190459


class spam(commands.Cog):

  
  
  def __init__(self, bot):
    
    self.bot = bot 
    self.notified_spam1 = True
    self.notified_spam2 = True
    self.spammer1.start(spam_channel_1)
    self.spammer2.start(spam_channel_2)
    

  
  @tasks.loop(seconds=60)
  async def spammer1(self, spam_channel_id):
    
    spam_channel = self.bot.get_channel(spam_channel_id)
    ping_channel = self.bot.get_channel(ping_channel_id)


    
    async for message in spam_channel.history(limit = 1):
      past_message = message.created_at

    await asyncio.sleep(50)

    
    async for message in spam_channel.history(limit = 1):
      new_message = message.created_at

    

    if past_message and new_message and past_message == new_message and self.notified_spam1 is True:
      
      await ping_channel.send(f"{spam_channel.mention} <@862021572026040350> no msg in the channel")
      self.notified_spam1 = False
      
    
      








  
  @tasks.loop(seconds=60)
  async def spammer2(self, spam_channel_id):
    
    spam_channel = self.bot.get_channel(spam_channel_id)
    ping_channel = self.bot.get_channel(ping_channel_id)


    
    async for message in spam_channel.history(limit = 1):
      past_message = message.created_at

    await asyncio.sleep(50)

    
    async for message in spam_channel.history(limit = 1):
      new_message = message.created_at

    

    if past_message and new_message and past_message == new_message and self.notified_spam2 is True:
      
      await ping_channel.send(f"{spam_channel.mention} <@862021572026040350> no msg in the channel")
      self.notified_spam2 = False
    
      



  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.id == spammer1_id and self.notified_spam1 is False:

      self.notified_spam1 = True
      await message.channel.send("`self.notified_spam1` is true")

    
    if message.author.id == spammer2_id and self.notified_spam2 is False:

      self.notified_spam2 = True
      await message.channel.send("`self.notified_spam2` is true")



async def setup(bot: commands.Bot):
  await bot.add_cog(spam(bot))
  