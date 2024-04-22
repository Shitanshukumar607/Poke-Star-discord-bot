import discord
from discord.ext import commands
import os
my_secret = os.environ['BOT_TOKEN']

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
  print("bot is ready")




@bot.command()
async def test(ctx):
    message = await ctx.send('test')
    emoji = '\N{THUMBS UP SIGN}'
    await message.add_reaction(emoji)


@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")


bot.run(my_secret)