import discord
from discord.ext import commands
import bot_token
import details
import asyncio


intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
  print("bot is READY")



@bot.event
async def on_message(message):

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
  if message.author.id == details.pokename_id and "Shiny Hunt Pings" in message.content:

    timer = await message.channel.send(embed= details.warn_embed)
    await asyncio.sleep(5)
    await timer.delete()
    await message.channel.send(embed= details.catch_embed)



  elif message.author.id == details.poke2assistant_id and "Shiny Hunt Pings" in message.content:
    
    timer = await message.channel.send(embed= details.warn_embed)
    await asyncio.sleep(5)
    await timer.delete()
    await message.channel.send(embed= details.catch_embed)

  

  
  await bot.process_commands(message)



@bot.command()
async def hello(ctx):
  await ctx.send("hello")

bot.run(bot_token.TOKEN)