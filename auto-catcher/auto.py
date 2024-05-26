import discord 
from discord.ext import commands


rare_channel_id = 1242698730260664433
shiny_channel_id = 1239894738052845608
main_server = 1223898987241799691

class auto(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    

  

  @commands.Cog.listener()
  async def on_message(self, msg):

    if msg.author == self.bot.user or len(msg.embeds) == 0 or msg.embeds[0].title is None or "star" not in msg.channel.name or msg.guild.id == 1223898987241799691:     
      return 
  
    if "rare catch detected" in msg.embeds[0].title.lower() :   
      await self.bot.get_channel(rare_channel_id).send(embed = msg.embeds[0])


    elif "shiny catch detected" in msg.embeds[0].title.lower():
      await self.bot.get_channel(shiny_channel_id).send(embed = msg.embeds[0])

    
    

 

    
      
      
  
    







async def setup(bot: commands.Bot):
  await bot.add_cog(auto(bot))
  
