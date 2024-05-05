import discord 
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import has_permissions

class mod(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.hybrid_command()
  async def test(self, ctx):
    await ctx.send("Everything is working")



  @commands.has_permissions(manage_roles=True)
  @commands.hybrid_command()
  async def role(self, ctx, Mem: discord.Member, *, Roler):


    role = discord.utils.get(ctx.guild.roles, name=Roler)
    
    if role is None:
        await ctx.send(f"Role '{Role}' not found.")

    else:


    
      if role not in Member.roles:
      
        await Member.add_roles(role)
        await ctx.send(f"Added **{role.name}** to **{Member.name}**")
      else:
        await Member.remove_roles(role)
        await ctx.send(f"Removed **{role.name}** from **{Member.name}**")







async def setup(bot: commands.Bot):
  await bot.add_cog(mod(bot))
  

