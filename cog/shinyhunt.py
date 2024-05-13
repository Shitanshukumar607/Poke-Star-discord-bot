import discord 
from discord.ext import commands
from discord import app_commands
from discord.utils import utcnow
import details 
import asyncio
import datetime 


class shinyhunt(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.last_used: datetime.datetime = None
  
  @commands.Cog.listener()
  async def on_message(self, message):


    # this is when a user catches a new Pokemon 
    if message.author.id == details.poketwo_id and "You received 35 Pokécoins!" in message.content:
      await message.add_reaction(details.congrats_emoji)
      await message.add_reaction(details.charmander_happy)
    #ends here


    
    # this is when a user incenses its shiny chain
    if message.author.id == details.poketwo_id and "+1 Shiny chain!" in message.content:
      await message.add_reaction(details.shiny) 
    #ends here


  # this is when there's a shinn hunter

    if message.author.id in details.pokebots and "shiny hunt pings" in message.content.lower() and "incense" in message.channel.name.lower():
  
      await self.do_shit(message,details.inc_warn_embed,9)

    
    elif message.author.id in details.pokebots and "shiny hunt pings" in message.content.lower():
      
      print("elif")

      await self.do_shit(message,details.warn_embed,25)

  


  async def do_shit(self, message: discord.Message,embed,time):
    if self.last_used and (utcnow() - self.last_used).total_seconds() < 2:
      return # nothing coz 2s cooldown
    self.last_used = utcnow()
    timer = await message.channel.send(embed = embed)
    await asyncio.sleep(time)
    await timer.delete()
    await message.channel.send(embed= details.catch_embed)
  
async def setup(bot: commands.Bot):
  await bot.add_cog(shinyhunt (bot))
  