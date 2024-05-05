import discord 
from discord.ext import commands,tasks
from discord import app_commands
import asyncio
import details 


past_message = None
new_message = None


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

    print(past_message)
    print(new_message)

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

    print(past_message)
    print(new_message)

    if past_message and new_message and past_message == new_message and self.notified_spam2 is True:
      
      await ping_channel.send(f"{spam_channel.mention} <@862021572026040350> no msg in the channel")
      self.notified_spam2 = False
    
      



  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.id == details.my_id and message.content == "1":

      self.notified_spam1 = True
      await message.channel.send("made it true (1)")

    
    if message.author.id == details.my_id and message.content == "2":

      self.notified_spam2 = True
      await message.channel.send("made it true (2)")



async def setup(bot: commands.Bot):
  await bot.add_cog(spam(bot))
  