import discord
from discord.ext import commands
import bot_token
import details
import asyncio
from typing import Optional , Literal 

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=["P!","<@1231616001880231996> " ], intents=intents)





@bot.event
async def on_ready():
  await bot.load_extension("cog.spam")
  await bot.load_extension("cog.shinyhunt")
  await bot.load_extension("cog.channel")
  await bot.load_extension("cog.error")
  print("bot is READY")





@bot.command()
async def suggestion(ctx, *, prompt: str):

  owner = bot.get_user(details.my_id)

  embed = discord.Embed(title="Suggestion", description=prompt)

  await owner.send(embed=embed)
  
  await ctx.send(f"Thank you for your suggestion, {ctx.author.name}! I have received your suggestion and will review it as soon as possible.")
   













@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")










  
@bot.command()
async def hello(ctx):
  await ctx.send("hellow")

bot.run(bot_token.TOKEN)