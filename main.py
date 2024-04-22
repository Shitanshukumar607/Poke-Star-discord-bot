import discord
from discord.ext import commands
import os
import details


my_secret = os.environ['BOT_TOKEN']

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
  print("bot is ready")



@bot.event
async def on_message(message):
  if message.author.id == details.poketwo_id and "You received 35 Pokécoins!" in message.content:
    await message.add_reaction(details.new_mon)


  if message.author.id == 1047861461801762846 :
    await message.add_reaction(details.emoji)














@bot.command()
async def test(ctx):
    message = await ctx.send('test')
    await message.add_reaction(emoji)


@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")


bot.run(my_secret)