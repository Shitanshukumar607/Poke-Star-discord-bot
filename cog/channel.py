import discord 
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import has_permissions



class channel(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  


  # UNHIDE COMMAND
  @commands.has_permissions(manage_channels=True)
  @commands.hybrid_command()
  async def unhide(self,ctx, role: discord.Role):

    overwrite = discord.PermissionOverwrite()
    overwrite.view_channel = True

    await ctx.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f"Unhide the channel for {role.name}.")





  
  # HIDE COMMAND 
  @commands.has_permissions(manage_channels=True)
  @commands.hybrid_command()
  async def hide(self,ctx, role: discord.Role):

    overwrite = discord.PermissionOverwrite()
    overwrite.view_channel = False

    await ctx.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f"Hide the channel for {role.name}.")





  
  # LOCK COMMAND 
  @commands.has_permissions(manage_channels=True)
  @commands.hybrid_command()
  async def lock(self,ctx, role: discord.Role):
 
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False

    await ctx.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f"Locked the channel for {role.name}.")




  # UNLOCK COMMAND
  @commands.has_permissions(manage_channels=True)
  @commands.hybrid_command()
  async def unlock(self,ctx, role: discord.Role):
 
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True

    await ctx.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f"Unlocked the channel for {role.name}.")










async def setup(bot: commands.Bot):
  await bot.add_cog(channel(bot))
  

