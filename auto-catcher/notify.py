import discord 
from discord.ext import commands,tasks
import asyncio


past_message1 = None

new_message1 = None

spammer1_id = 1223878867027230735
spammer2_id = 783543227189297192


spam_channel_1 = 1223899187519688734
spam_channel_2 = 1235593275143094294




ping_channel_id = 1235590585298190459


class spam(commands.Cog):

  
  
  def __init__(self, bot):
    
    self.bot = bot 
    self.notify_ac = self.bot.get_channel(notify_ac_id)
    self.ac_spam1 = True
    self.ac_spam2 = True
    self.spammer1.start(spam_channel_1)
    self.spammer2.start(spam_channel_2)
    

  
  @tasks.loop(seconds=60)
  async def spammer1(self, spam_channel_id):
    
    spam_channel1 = self.bot.get_channel(spam_channel_id1)
    


    
    async for message in spam_channel1.history(limit = 1):
      past_message1 = message.created_at
    await asyncio.sleep(50)

    async for message in spam_channel1.history(limit = 1):
      new_message1 = message.created_at

    

    if past_message1 and new_message1 and past_message1 == new_message1 and self.ac_spam1 is True:
      
      await self.notify_ac.send(f"<@862021572026040350> no msg in the {svr1}")
      self.ac_spam1 = False
      
    
      








  
  
      



  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.id == spammer1_id and self.notified_spam1 is False:

      self.notified_spam1 = True
      await message.channel.send("`self.notified_spam1` is true")

    
    


async def setup(bot: commands.Bot):
  await bot.add_cog(spam(bot))
  