import discord
from discord.ext import commands
import bot_token
import details
import asyncio


intents = discord.Intents.all()

bot = commands.Bot(command_prefix=["!","<@1231616001880231996> " ], intents=intents)





@bot.event
async def on_ready():
  await bot.load_extension("cog.spam")
  print("bot is READY")





@bot.command()
async def suggestion(ctx, *, prompt: str):

  owner = bot.get_user(details.my_id)

  embed = discord.Embed(title="Suggestion", description=prompt)

  await owner.send(embed=embed)
  
  await ctx.send(f"Thank you for your suggestion, {ctx.author.name}! I have received your suggestion and will review it as soon as possible.")
   
  

  
@bot.command()
async def hello(ctx):
  await ctx.send("hellow")

bot.run(bot_token.TOKEN)