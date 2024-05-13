import discord 
from discord.ext import commands
from discord import app_commands


class error(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):

    if isinstance(error, commands.errors.MissingPermissions):
      await ctx.send("You don't have the permission to do that.")


    
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"You missed the `{error.param.name}` argument.\n\nDo it like: \n`{ctx.prefix} {ctx.command.qualified_name} {ctx.command.signature}`")

    elif isinstance(error, commands.RoleNotFound):
      await ctx.send(error)
    
      
    else:
      await ctx.send(f"An error occurred: {error}")



async def setup(bot: commands.Bot):
  await bot.add_cog(error(bot))