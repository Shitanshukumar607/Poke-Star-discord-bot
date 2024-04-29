import discord

poketwo_id = 716390085896962058
my_id = 862021572026040350
realpro_id = 1047861461801762846
pokename_id = 874910942490677270
poke2assistant_id = 854233015475109888

pokebots = [pokename_id,poke2assistant_id]


# EMOJIS 

charmander_happy = "<:Pokemon1:1224764942515830794>"  # happy charmander emoji
congrats_emoji = "🥳" 
shiny = "<a:shiny:1232000027103068322>"  # star shining emoji ✨


normal_time = 25
incense_timer = 9





# EMBEDS 

#embed for not to catch before timer ends

inc_warn_embed = discord.Embed( description="Hey fellow trainer, if the shiny hunter is not afk **do not catch this Pokemon** before this timer ends ❌ \n\n This timer will end in 9 seconds ", colour= 0xFF0000)

warn_embed = discord.Embed( description="Hey fellow trainer, if the shiny hunter is not afk **do not catch this Pokemon** before this timer ends ❌ \n\n This timer will end in 25 seconds ", colour= 0xFF0000)

catch_embed = discord.Embed( description="The timer has ended, you can now catch this Pokemon ✅" , colour= 0x00ff00)