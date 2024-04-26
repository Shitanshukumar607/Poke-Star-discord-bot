import discord
from discord.ext import commands
import bot_token
import details



intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
  print("bot is READY")



@bot.event
async def on_message(message):
  
  if message.author.id == details.poketwo_id and "You received 35 Pokécoins!" in message.content:
    
    await message.add_reaction(details.congrats_emoji)
    await message.add_reaction(details.charmander_happy)

  
  await bot.process_commands(message)



@bot.command()
async def hello(ctx):
  await ctx.send("hello")

bot.run(bot_token.TOKEN)