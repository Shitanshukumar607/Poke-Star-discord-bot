import discord 
from discord.ext import commands
from discord import app_commands
import details 
import asyncio



class shinyhunt(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

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

    if "incense" in message.channel.name.lower():

      if message.author.id == details.pokename_id and "shiny hunt pings" in message.content.lower():

        timer = await message.channel.send(embed = details.inc_warn_embed)
    
        await asyncio.sleep(9)
        await timer.delete()
        await message.channel.send(embed= details.catch_embed)


      elif message.author.id == details.poke2assistant_id and "shiny hunt pings" in message.content.lower():
    
        timer = await message.channel.send(embed= details.inc_warn_embed)
        await asyncio.sleep(9)
        await timer.delete()
        await message.channel.send(embed= details.catch_embed)


    else:

    
      if message.author.id == details.pokename_id and "shiny hunt pings" in message.content.lower():

        timer = await message.channel.send(embed = details.warn_embed)
    
        await asyncio.sleep(25)
        await timer.delete()
        await message.channel.send(embed= details.catch_embed)



      elif message.author.id == details.poke2assistant_id and "shiny hunt pings" in message.content.lower():

        timer = await message.channel.send(embed= details.warn_embed)
    
        await asyncio.sleep(25)
        await timer.delete()
        await message.channel.send(embed= details.catch_embed)


  
    


    








async def setup(bot: commands.Bot):
  await bot.add_cog(shinyhunt (bot))
  

