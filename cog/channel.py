import discord 
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import has_permissions



class channel(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.hybrid_command()
  async def test(self, ctx):
    await ctx.send("Everything is working")


  @commands.hybrid_command()
  async def unhide(self,ctx, role: discord.Role):
 
    overwrite = discord.PermissionOverwrite()
    overwrite.view_channel = True

    await ctx.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f"Unhide the channel for {role.name}.")







async def setup(bot: commands.Bot):
  await bot.add_cog(channel(bot))
  

