# Imports to downalod
# pip install... # In shell
import requests
import discord
from discord.ext import commands, tasks
import random
import os
import keep_alive
from itertools import cycle
from requests import get
import json
import whois
import somecord

# Breh don't change this or bot won't work, it's connected with trixx.
os.chdir("/home/runner/TrixX/")

# Change prefix here (prefix per server isn't enabled) 
client = commands.Bot(command_prefix = '*', intents=discord.Intents.all(), case_insensitive=True)

# Kepp at is it.
client.remove_command('help')

# Kepp at is it.
@client.event
async def on_ready():
  changestatus.start()
  print('Proceeding as {0.user}'.format(client))

# General Commands

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! Bot latency is {round(client.latency*1000)}ms <:TrixxGG:901517233069645864>')

@client.command()
async def hello(ctx):
  await ctx.send(f'Heyo out there! <:TrixxHeart:901517258088648735>')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question=None):
  responses = ['It is certain.',
               'Probably not.',
               'What the hell are you even thinking of?',
               '**NO**',
               'Yea sure why not?',
               'Hmmmmmmmmmm...',
               'Im wondering whats going on in your mind.',
               'If you pay me 10$, yes.',
               'Definetly',]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases=['info', 'trixx'])
async def botinfo(ctx):
  embed=discord.Embed(title="**Trixx**",
  url="https://discord.com/api/oauth2/authorize?client_id=816573349093703710&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D816573349093703710%26permissions%3D8%26scope%3Dbot&scope=bot", description="How I was made...", color=0x42f5ef)
  embed.set_author(name="Navigator",
  url="https://www.youtube.com/channel/UC_wDXm7EO_FnslXGU1CLwdg",
  icon_url="https://i.redd.it/pfequv9fdwj71.png")
  embed.set_thumbnail(url="https://wonder-day.com/wp-content/uploads/2020/04/wonder-day-brawl-stars-sprout-50.jpg")

  embed.add_field(name="INFO", value="Hey, I'm a bot made by @T¹⁸| Navigator ✨#3582 ,and focused on Brawl Stars, fun commands and Moderation tools! If you want to learn more, join our support server (click below) or just toggle **help!")
  embed.set_footer(text="Join our support server! https://discord.gg/ZzKmT8Fqr9")
  await ctx.send(embed=embed)

@client.command()
async def subme(ctx):
  await ctx.send(f'https://www.youtube.com/channel/UC_wDXm7EO_FnslXGU1CLwdg <:TrixxClapping:901517217869463592>')

@client.command(aliases=['update'])
async def maintenance(ctx):
  await ctx.send(f'Bot is expected to be under maintenance for the next days, you will still be able to use it, but you could experience some lags. <:TrixxPhew:901517280704339968>')


@client.command()
async def invite(ctx):
  await ctx.send(f'Click here to add me to your server! Be sure to have **Manage server** permissions! https://discord.com/api/oauth2/authorize?client_id=816573349093703710&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D816573349093703710%26permissions%3D8%26scope%3Dbot&scope=bot')

@client.command()
async def purge(ctx, amount=1):
  await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  if (not ctx.author.guild_permissions.kick_members):
    await ctx.send('Playing a little bit Mod huh? Next time try with *Kick Members* permissions! <:TrixxAngry:901517200425353286>')
    return
  await member.kick(reason=reason)
  await ctx.send(f'{member.mention} has been kicked! <:TrixxPhew:901517280704339968>')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  if (not ctx.author.guild_permissions.ban_members):
    await ctx.send('Playing a little bit Mod huh? Next time try with *Ban Members* permissions! <:TrixxAngry:901517200425353286>')
    return
  await member.ban(reason=reason)
  await ctx.send(f'{member.mention} has been banned! <:TrixxPhew:901517280704339968>')



@client.command()
async def say(ctx, *, reason=None):
  await ctx.send(reason)

@client.command()
async def reply(ctx, *, reason=None):
  await ctx.reply(reason)

status = cycle(['#NavigatorDevs', '**help', 'Finally 24/7'])

@tasks.loop(seconds=10)
async def changestatus():
  await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def brawlerinfo(ctx):
  await ctx.reply(f'<:TrixxSad:901517290921672735> Hmmm, seems you forgot the hyphen between the *brawlerinfo and the brawlername, so you need to type: brawlerinfo-<brawler>')

@client.command(aliases=['credit'])
async def credits(ctx):
  user=ctx.author
  embed=discord.Embed(title="<:TrixxWorks:915578776623149116> Credits <:TrixxWorks:915578776623149116>", description="People who have participated in my build", colour=user.colour)
  embed.add_field(name="Navigator", value="Role: Owner", inline=False)
  embed.add_field(name="Neyo Golden", value="Role: Administrator", inline=False)
  embed.add_field(name="Supercell", value="Role: Assets Provider (not officially)", inline=False)
  embed.set_footer(text="All credit goes to them!")
  
  await ctx.send(embed=embed)

@client.command()
async def uptime(ctx):
  user=ctx.author
  embed=discord.Embed(title="Bot's Status", description="Recent downtimes and maintenances", colour=user.colour, url="https://discord.gg/JnsyAzwVZp")
  embed.add_field(name="<:D_Online:951132216044425237> NO RECENT DOWNTIMES! <:D_Online:951132216044425237>", value="Check our support server for more info on that.", inline=False)
  embed.set_footer(text="Support server: https://discord.gg/JnsyAzwVZp (or click the title of this embed)")
  
  await ctx.send(embed=embed)
  
  










######################








#Milestones 
#Shelly


@client.command(aliases=['brawlerinfo-shelly'])
async def brawlerishelly(ctx):
  embed=discord.Embed(title="Shelly", description="All info on Shelly", color=0x82ffff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/5/5e/Shelly_Skin-Default.png/revision/latest?cb=20210811191059")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/e/e5/Shelly_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200304182226")
  embed.add_field(name="<:Info:901525872878706778> **General info**", value="Shelly's spread-fire shotgun blasts the other team with buckshot. Her Super destroys cover and keeps her opponents at a distance!", inline=False)
  embed.add_field(name="<:Attack:901525850778918955> **Attack - Buckshot**", value="Shelly's boomstick fires a wide spread of pellets to a medium range. The more pellets hit, the greater the damage.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Super Shell**", value="Shelly's Super Shell obliterates both cover and enemies. Any survivors get knocked back.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203>  Gadget: Fast Forward", value="Shelly dashes ahead, skipping a few unnecessary steps!", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203>  Gadget: Clay Pigeons", value="On activation, for the next 5 seconds Shelly's main attacks focuses the fire to a smaller area and increases the range.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower: Shell Shock", value="Shelly's Super shells slow down enemies for 4.5 seconds!", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Band Aid", value="When Shelly falls below 40% health, she instantly heals for 2000 health. Band-Aid recharges in 15.0 seconds.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Nita

@client.command(aliases=['brawlerinfo-nita'])
async def brawlerinita(ctx):
  embed=discord.Embed(title="Nita", description="All info on Nita", color=0x82ffff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/3/36/Nita_Skin-Default.png/revision/latest?cb=20200829210549")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/9/9f/Nita_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200304182317")
  embed.add_field(name="<:Info:901525872878706778> **General info**", value="Nita strikes her enemies with a thunderous shockwave. Her Super summons a massive bear to fight by her side!", inline=False)
  embed.add_field(name="<:Attack:901525850778918955> **Attack - Rupture**", value="Nita sends forth a shockwave, damaging enemies caught in the tremor.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Overbearing**", value="Nita summons the spirit of Big Baby Bear to hunt down her enemies.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203>  Gadget - Bear Paws", value="Nita commands her bear to slam the ground, stunning all enemies within its reach.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Faux Fur", value="For the next 3 seconds, Nita's bear gets a 35% shield against damage.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Bear With Me", value="Nita recovers 800 health whenever her bear hits an enemy brawler. When Nita deals damage to an enemy brawler, her bear regains 800 health.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Hyperbear", value="Nita's bear attacks faster. Time between swipes is reduced by 60%.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Colt

@client.command(aliases=['brawlerinfo-colt'])
async def brawlericolt(ctx):
  embed=discord.Embed(title="Colt", description="All info on Colt", color=0x82ffff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/8/8a/Colt_Skin-Default.png/revision/latest?cb=20210906093846")
  embed.set_thumbnail(url="https://liquipedia.net/commons/images/1/15/Brawl_Colt.png")
  embed.add_field(name="<:Info:901525872878706778> **General info**", value="Colt fires an accurate burst of bullets from his dual revolvers. His Super shreds cover and extends the bullet barrage!", inline=False)
  embed.add_field(name="<:Attack:901525850778918955> **Attack - Six-Shooters**", value="Colt shoots six straight long-range shots out of his revolvers.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Bullet Storm**", value="Colt rattles off a massive burst of bullets that shoot extra far and destroy cover.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203>  Gadget - Speedloader", value="Colt instantly reloads 2 ammo.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Silver Bullet", value="Colt's next attack is a powerful shot that deals as much damage as 2 of his regular bullets, while going through obstacles and opponents alike.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Slick Boots", value="Colt's movement speed is increased by 13%.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Magnum Special", value="Colt’s main attack range and bullet speed are increased by 11%.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Bull

@client.command(aliases=['brawlerinfo-bull'])
async def brawleri(ctx):
  embed=discord.Embed(title="Bull", description="All info on Bull", color=0x82ffff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/b/b7/Bull_Skin-Default.png/revision/latest?cb=20210913081903")
  embed.set_thumbnail(url="https://liquipedia.net/commons/images/2/25/Brawl_Bull.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Bull deals massive damage up close with his shotgun. For his Super move, he charges through barriers and knocks back enemies!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Double Barrel**", value="Bull's double-barreled shotgun deals heavy damage. It has very short range, so Bull likes to get up close and personal.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Bulldozer**", value="Bull puts his head down and bulldozes through opponents and obstacles. He's always been headstrong!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - T-Bone Injector", value="Bull instantly rejuvenates himself for 1500 health.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Stomper", value="Bull can interrupt his Super charge and slow all nearby opponents with a massive stomp for 1.5 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Berserker", value="When Bull falls below 60% health, his reload speed doubles!", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Tough Guy", value="When Bull falls below 40% health, he gains a shield that reduces all damage taken by 30%.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Jessie

@client.command(aliases=['brawlerinfo-jessie'])
async def brawlerijessie(ctx):
  embed=discord.Embed(title="Jessie", description="All info on Jessie", color=0x82ffff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/1/15/Jessie_Skin-Default.png/revision/latest?cb=20210126112456&path-prefix=de")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/4/4e/Jessie_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200304182249")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Jessie's Shock Rifle shoots energy orbs that bounce between enemies. Her Super deploys a cute but deadly gun turret!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Shock Rifle**", value="Jessie fires off an energy orb. After hitting a target, the orb bounces at the next target in range, hitting up to three enemies.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Scrappy!**", value="Jessie deploys a gun turret that automatically shoots at enemies. It's made of 100% recycled materials!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Spark Plug", value="Jessie triggers a shockwave from her turret, slowing down all enemies within its area of effect.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Recoil Spring", value="Scrappy's attack speed is doubled for 5 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Energize", value="Jessie can repair her gun turret for 896 of its missing health by zapping it with her attack.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Shocky", value="Scrappy the Turret now shoots energy orbs that bounce between enemies. The orbs' range after a bounce is 51% of normal range.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Brock

@client.command(aliases=['brawlerinfo-brock'])
async def brawleribrock(ctx):
  embed=discord.Embed(title="Brock", description="All info on Brock", color=0x82ffff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/7/70/Brock_Skin-Default.png/revision/latest?cb=20200331164840")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/f/f9/Brock_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200304182256")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Brock fires a long-range, explosive rocket at enemies. His Super is a ballistic rocket barrage that destroys cover!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Rockin' Rocket**", value="Brock lets fly with a single Rockin' Rocket that really goes the distance.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Rocket Rain**", value="Brock fires a rocket barrage that takes out enemies and obstacles. He only wants to see you bathing in the Rocket Rain!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Rocket Laces", value="Brock blasts the ground below him and propels himself into the air. The explosion deals 500 damage to nearby enemies.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Rocket Fuel", value="Brock's next attack is a mega rocket that is bigger, faster, explodes with a large radius, destroys walls and deals 50% extra damage.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Incendiary", value="The impact of Brock's attack sets the ground on fire. Enemies in the area take 520 damage per second! Lasts for 2 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Rocket Number Four", value="Brock loads a fourth rocket into his launcher, increasing his ammo capacity (and discarding the thermos bottle he's been keeping in his launcher's #4 rube).", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Dynamike

@client.command(aliases=['brawlerinfo-dynamike'])
async def brawleridynamike(ctx):
  embed=discord.Embed(title="Dynamike", description="All info on Dynamike", color=0x82ffff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/6/6e/Dynamike_Skin-Default.png/revision/latest?cb=20201118121329")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/6/64/Dynamike_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200304182305")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Dynamike lobs two explosive sticks of dynamite. His Super attack is a whole barrel full of dynamite that blows up cover!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Short Fuse**", value="Mike tosses two sticks of dynamite, passing over any obstacles in the way. The fuses are cut as short as Mike's explosive temper!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Big Barrel O'Boom**", value="A big-bada-barrel of dynamite blows up cover. Any surviving enemies get knocked back on impact!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Fidget Spinner", value="Dynamike spins furiously and throws multiple sticks of dynamite around himself. Each dynamite deals 1200 damage to enemies.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Satchel Charge", value="Once activated, the next main attack also stuns enemies for 1.5 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Dyna-Jump", value="Dynamike can ride the blast wave of his explosives to jump over obstacles!", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Demolition", value="Adds +1000 damage to Mike’s Super.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Bo

@client.command(aliases=['brawlerinfo-bo'])
async def brawleribo(ctx):
  embed=discord.Embed(title="Bo", description="All info on Bo", color=0x82ffff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/e/ee/Bo_Skin-Default.png/revision/latest?cb=20190416001137")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/3/30/Bo_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20191013135616")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Bo fires three explosive arrows toward his targets. His Super ability places a trio of hidden, explosive mines on the ground!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Eagle-Eyed**", value="Bo releases a trio of exploding arrows, tearing up enemies like an eagle's talons.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Catch a fox**", value="Bo hides explosive traps in the ground. When triggered by an enemy, the traps explode after a short delay, knocking back and damaging enemies.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Super Totem", value="Bo places a totem that recharges his and any allies' Supers within the area of effect. The totem slowly loses its health over time.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Tripwire", value="Bo triggers all of his mines after 1.5 seconds. During the delay the mines are completely undetectable to opponents.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Circling Eagle", value="Bo spots enemies hidden in bushes from 150% longer distance than normally.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Snare a bear", value="Instead of a knockback, Bo’s traps now stun the enemy for 2 seconds.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Tick

@client.command(aliases=['brawlerinfo-tick'])
async def brawleritick(ctx):
  embed=discord.Embed(title="Tick", description="All info on Tick", color=0x82ffff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/b/b1/Tick_Skin-Default.png/revision/latest?cb=20200416072522")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/7/72/Tick_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20190629012550")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Tick is a metal ball of barely controlled excitement and energy - explosive energy! He throws mines, and his Super makes his head detach, seek a target and explode.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Minimines**", value="Tick lobs a cluster of mines that separate before landing. The mines explode on contact with a target, or after a few seconds.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Headfirst**", value="Tick detaches and launches his head. After landing, the head hops toward the nearest target and explodes on contact!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Mini Mania", value="Tick's next attack fires 6 mines.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Last Hurrah", value="Tick's next attack fires 6 mines.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Well Oiled", value="When Tick takes no damage and doesn't attack, he starts recovering health 2 seconds faster than normal.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Automa-Tick Reload", value="Tick's reload time is 9% shorter.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#8Bit

@client.command(aliases=['brawlerinfo-8bit'])
async def brawleri8bit(ctx):
  embed=discord.Embed(title="8 Bit", description="All info on 8 Bit", color=0x82ffff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/a/a2/8-BIT_Skin-Default.png/revision/latest?cb=20210812182214")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/f/f0/8-BIT_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20191012200012")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="8-Bit lumbers along like an arcade cabinet on legs. He shoots Blaster Beams and his Super boosts friendlies' damage!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Blaster Beams**", value="Shoots a burst of Blaster Beams that damage any opponent they hit. The beams have medium range and a slight spread.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Damage Booster**", value="Shoots a burst of Blaster Beams that damage any opponent they hit. The beams have medium range and a slight spread.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Cheat Cartridge", value="8-Bit instantly teleports to his Damage Booster.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Extra Credits", value="8-BIT's next attack has the number of projectiles increased to 18.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Boosted Booster", value="Increases the Damage Booster's range by 50% and boosts damage by an additional 15%.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Plugged In", value="When 8-Bit is near his Damage Booster, he will plug in and have increased movement speed.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Emz

@client.command(aliases=['brawlerinfo-emz'])
async def brawleriemz(ctx):
  embed=discord.Embed(title="Emz", description="All info on Emz", color=0x82ffff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/e/e0/Emz_Skin-Default.png/revision/latest?cb=20201112165906")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/a/a4/Emz_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200304182125")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Emz attacks with blasts of hair spray that deal damage over time, and slows down opponents with her Super.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Spray**", value="Emz gives you a blast of her hair spray! It's strong enough to melt your face.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Caustic Charisma**", value="Emz creates a cloud of toxicity around herself, slowing down the movement of enemies and damaging them.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Friendzoner", value="EMZ pushes back all enemies around her while also dealing 500 damage.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Bad Karma", value="Enemies that stay within the cloud of Emz's toxic hair spray suffer increasing damage, 25% per hit.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Hype", value="Emz recovers 420 health per second for each enemy inside her Super's area of effect.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Stu

@client.command(aliases=['brawlerinfo-stu'])
async def brawleristu(ctx):
  embed=discord.Embed(title="Stu", description="All info on Stu", color=0x82ffff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/b/b8/Stu_Skin-Default.png/revision/latest?cb=20210324100633&path-prefix=de")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/c/c8/Stu_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20210309220216")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Stu is a stunt driver extraordinaire with gasoline in his veins! He makes a big entrance, burning serious rubber all over the stage.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Razzle Dazzle**", value="Stu fires out two pyrotechnic shots that pack quite a wallop.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Nitro Boost**", value="Hitting an opponent with Razzle Dazzle charges up Stu's Nitro Boost, a short dash that bumps opponents out of the way. Leaves a trail of burning rubber on the ground that will set fire to any opponents that touch it.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Speed Zone", value="Stu drops a booster that makes himself, his teammates and other allies move faster while inside its area of effect.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Breakthrough", value="Stu's next Super can bash through obstacles, making debris fly forward. Each piece of debris deals 200 damage to any opponent it hits.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Zero Drag", value="Stu's Nitro Boost Super dash distance increases by 71%.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Gaso-Heal", value="Using his Nitro Boost Super restores 400 of Stu's health.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Rares
#El Primo

@client.command(aliases=['brawlerinfo-elprimo'])
async def brawlerielprimo(ctx):
  embed=discord.Embed(title="El Primo", description="All info on El Primo", color=0xa1ff8a)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/0/04/El_Primo_Skin-Default.png/revision/latest?cb=20200225131129")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/c/c5/El_Primo_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20191012200018")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="El Primo throws a flurry of punches at his enemies. His Super is a leaping elbow drop that deals damage to all caught underneath!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Fists of Fury**", value="El Primo fires off a furious flurry of four fiery fists. That's a spicy jalapeno knuckle sandwich!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Flying Elbow Drop**", value="Leaping high, El Primo drops an Intergalactic Elbow that knocks around enemies and destroys cover!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Suplex Supplement", value="El Primo grabs the closest enemy within his reach and flips them like a pancake over his broad shoulders.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Asteroid Belt", value="El Primo summons a small meteor to strike the nearest enemy. It deals 2000 damage and destroys walls.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - El Fuego", value="Enemies caught in El Primo's Super will burn for 1200 damage over 4 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Meteor Rush", value="El Primo gains 25% speed boost for 4 seconds after using his Super.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Rosa

@client.command(aliases=['brawlerinfo-rosa'])
async def brawlerirosa(ctx):
  embed=discord.Embed(title="Rosa", description="All info on Rosa", color=0xa1ff8a)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/3/34/Rosa_Skin-Default.png/revision/latest?cb=20210118061719")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/9/94/Rosa_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200303144700")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="This boxing botanist will plant her feet and go toe to toe! Her Super gives her tough, vegan protective gear.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Hands of Stone**", value="Rosa throws a flurry of powerful punches with perfect technique!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Strong Stuff**", value="Rosa gets a second skin of tough vine for 3 seconds, decreasing all damage received by 70% for the duration.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Grow Light", value="Rosa fertilizes the ground around her and bushes instantly grow to provide great cover.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Unfriendly Bushes", value="All opponents hiding in bushes take 100 damage and get slowed down for 3 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Plant Life", value="Rosa recovers 200 health per second when inside a bush.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Thorny Gloves", value="Rosa’s punches gain +220 damage during her Super.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Barley

@client.command(aliases=['brawlerinfo-barley'])
async def brawleribarley(ctx):
  embed=discord.Embed(title="Barley", description="All info on Barley", color=0xa1ff8a)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/3/3c/Barley_Skin-Default.png/revision/latest?cb=20200331165158")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/a/a1/Barley_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200304182055")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Barley attacks by lobbing bottles at enemies, doing splash damage. His Super is a huge barrage of burning bottles!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Undiluted**", value="Barley lobs a bottle, breaking it on the ground. Enemies take damage from the splash, and more damage over time if they stay in the puddle.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Last Call**", value="Barley hurls a flurry of fiery bottles, covering a huge area in flames. This one's on the house!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Sticky Syrup Mixer", value="Barley drops a sticky concoction that leaves a puddle, slowing down all enemies that make contact with it.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Herbal Tonic", value="Barley throws a healing potion at nearby allies that creates an area that heals for 500 health per second.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Medical Use", value="Barley regains 400 health from each atack.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Extra Noxious", value="Adds +200 damage per second to Barley’s attack.", inline=True)
  embed.set_footer(text="CC: Navigator")

  await ctx.send(embed=embed)

#Poco

@client.command(aliases=['brawlerinfo-poco'])
async def brawleripoco(ctx):
  embed=discord.Embed(title="Poco", description="All info on Poco", color=0xa1ff8a)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/2/24/Poco_Skin-Default.png/revision/latest?cb=20210407002227")
  embed.set_thumbnail(url="https://i.pinimg.com/originals/32/79/19/327919f986e11c2014d5d0cde63e124c.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Poco fires damaging sound waves at enemies. His Super can heal both Poco himself and his teammates!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Power Chard**", value="Poco strums his guitarrón, sending forward bone-jarring sound waves. Enemies hit by the waves take damage.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Encore**", value="Poco heals himself and all friends he can reach with his uplifting melody. Does not affect enemies.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Tuning Fork", value="Poco and all nearby allies heal 400 health per second for 5 seconds.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Protective Tunes", value="Removes active adverse effects from friendly brawlers in a large area and gives a 2 second immunity.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Da Capo!", value="When Poco's attack hits friendly Brawlers they now heal for 700 health.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Screeching Solo", value="Poco’s Super now also hits enemies, dealing 1000 damage.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Superrares
#Darryl

@client.command(aliases=['brawlerinfo-darryl'])
async def brawleridarryl(ctx):
  embed=discord.Embed(title="Darryl", description="All info on Darryl", color=0x264aff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/6/66/Darryl_Skin-Default.png/revision/latest?cb=20210202212827&path-prefix=de")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/4/46/Darryl_Portrait.png/revision/latest?cb=20200317100419")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Darryl has a powerful double-shotgun attack. His Super move is a reckless roll inside his bouncy barrel!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Double Deuce**", value="Darryl's double barrel shotguns fire two staggered blasts of heavy close-range damage.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Barrel Roll**", value="Darryl rolls forward inside his barrel, knocking back enemies and bouncing off walls. His Super recharges over time!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Recoiling Rotator", value="Darryl spins around and sprays a barrage of shots in all directions. Each shot deals 400 damage and recharges his Super by 25% if it hits enemies!", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Tar Barrel", value="Darryl creates a slowing area around himself for 5 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Steel Hoops", value="Darryl's Super reinforces his barrel, reducing all damage he takes by 90% for 0.9 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Rolling Reload", value="When Darryl uses his Super, he doubles his reload speed for 5 seconds.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Rico

@client.command(aliases=['brawlerinfo-rico'])
async def brawleririco(ctx):
  embed=discord.Embed(title="Rico", description="All info on Rico", color=0x264aff)
  embed.set_image(url="https://www.brawlstarsarena.com/wp-content/uploads/2020/10/BSA_avatar_Rico-300x300.png")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/e/e1/Rico_Portrait.png/revision/latest?cb=20200304182045")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Rico fires a burst of bullets that bounce off walls. His Super burst is a long barrage of bouncy bullets that pierce targets!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Bouncy Bullets**", value="Rico's bullets bounce off walls, gaining range. They can hit enemies behind cover.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Trick Shot**", value="Rico fires a long burst of bullets that pierce through enemies and bounce off walls, gaining range.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Multiball Launcher", value="Rico blasts waves of bouncy bullets in all directions.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Bouncy Castle", value="Rico's next attack will heal him for 250 health from each bounce of a projectile.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Super Bouncy", value="Rico's bullets, from attack and Super alike, get supercharged by their first bounce and deal +124 damage!", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Robo Retreat", value="Rico's bullets, from attack and Super alike, get supercharged by their first bounce and deal +124 damage!", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Penny

@client.command(aliases=['brawlerinfo-penny'])
async def brawleripenny(ctx):
  embed=discord.Embed(title="Penny", description="All info on Penny", color=0x264aff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/d/d6/Penny_Skin-Default.png/revision/latest?cb=20210119011330")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/8/8d/Penny_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200304182356")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Penny shoots bags of coins, damaging the target and anyone standing behind. Her Super is a mortar-style cannon turret!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Plunderbuss**", value="Penny shoots bags of coins, damaging the target and anyone standing behind. Her Super is a mortar-style cannon turret!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Old Lobber**", value="Penny sets up her cannon! It can shoot at enemies at a long range, even if they are behind cover.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Pocket Detonator", value="Penny blows up her cannon! The explosion destroys walls and deals 1500 damage to nearby enemies.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Captain's Compass", value="Penny blows up her cannon! The explosion destroys walls and deals 1500 damage to nearby enemies.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Last Blast", value="When Penny's Cannon is destroyed, it shoots out one last barrage of 4 bombs targeting nearby enemies, each dealing 1680 damage.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Balls of Fire", value="Cannonballs from Penny’s turret set the ground on fire for 3 seconds. Enemies in the burning area take 400 damage per second.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Carl

@client.command(aliases=['brawlerinfo-carl'])
async def brawlericarl(ctx):
  embed=discord.Embed(title="Carl", description="All info on Carl", color=0x264aff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/4/46/Carl_Skin-Default.png/revision/latest?cb=20200315100242")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/1/19/Carl_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200304182115")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Carl throws his Pickaxe like a boomerang. His Super is a crazy cart spin that clobbers anyone around him.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Pickaxe**", value="Carl throws his Pickaxe like a boomerang. After he catches the returning Pickaxe, he can throw it again.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Tailspin**", value="Carl throws his Pickaxe like a boomerang. After he catches the returning Pickaxe, he can throw it again.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Heat Ejector", value="Carl drops a trail of hot rocks behind his cart! Opponents that touch them are set on fire, and receive a total of 1200 damage over time each.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Flying Hook", value="Carl's next attack makes his pickaxe pull him to the farthest point of the attack.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Power Throw", value="Carl throws his Pickaxe with 12% more speed, allowing it to travel faster and return faster.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Protective Pirouette", value="During Carl's Super, all damage he receives is reduced by 35%.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Jacky

@client.command(aliases=['brawlerinfo-jacky'])
async def brawlerijacky(ctx):
  embed=discord.Embed(title="Jacky", description="All info on Jacky", color=0x264aff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/5/52/Jacky_Skin-Default.png/revision/latest?cb=20200430211047")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/0/03/Jacky_Portrait.png/revision/latest?cb=20200317100434")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Jacky works her Jackhammer to shake up the ground and nearby enemies. Her Super pulls in nearby foes, leaving them in the dust!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Groundbreaker**", value="Jacky hops on her Jackhammer to shake the ground all around. Enemies caught too close will get a pounding!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Holey Moley!**", value="Jacky drills a hole in the ground, pulling in foes to introduce them to her Jackhammer! She partially shields incoming attacks while performing her Super.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Pneumatic Booster", value="Jacky gets a burst of energy and moves 20% faster for 3 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Counter Crush", value="When receiving damage, Jacky returns the favor by converting 30% of the damage into a Groundbreaker counteratt", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Hardy Hard Hat", value="Jacky's Hard Hat protects her by reducing any damage she takes by 10%.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Epics
#Piper

@client.command(aliases=['brawlerinfo-piper'])
async def brawleripiper(ctx):
  embed=discord.Embed(title="Piper", description="All info on Piper", color=0xdd61ff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/5/5d/Piper_Skin-Default.png/revision/latest?cb=20210802192844")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/f/f0/Piper_Portrait.png/revision/latest?cb=20200304182144")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Piper's sniper shots do more damage the farther they travel. Her Super drops grenades at her feet, while Piper herself leaps away!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Gunbrella**", value="Piper's sniper shots do more damage the farther they travel. Her Super drops grenades at her feet, while Piper herself leaps away!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Poppin'**", value="Piper hops away to avoid pushy suitors. She leaves them a lady's favor though: live grenades from her garter!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Auto Aimer", value="Piper hops away to avoid pushy suitors. She leaves them a lady's favor though: live grenades from her garter!", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Homemade Recipe", value="On activation, Piper's next main attack will home in on enemies.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Ambush", value="Piper's attack deals +800 extra damage (at max range) when she's hidden in a bush.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Snappy Sniping", value="When Piper hits an enemy with her attack, she reloads 0.4 ammo instantly.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Pam

@client.command(aliases=['brawlerinfo-pam'])
async def brawleripam(ctx):
  embed=discord.Embed(title="Pam", description="All info on Pam", color=0xdd61ff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/6/68/Pam_Skin-Default.png/revision/latest?cb=20201129223707")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/d/dc/Pam_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200513143851")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Pam shoots from the hip, peppering targets with shrapnel. Her Super is a healing turret that restores her and teammates' health!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Scrapstorm**", value="Pam sprays a large area with bursts of scrap metal. Safety goggles advised!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Mama's Kiss**", value="Pam sprays a large area with bursts of scrap metal. Safety goggles advised!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Pulse Modulator", value="Pam triggers her turret to emit a pulse that heals allies inside the turret's range, including herself, for 1200 health.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Scrapsucker", value="Each hit from Pam's next attack removes 25% of opposing Brawlers' maximum ammo. Pam reclaims 50% of the ammo for herself.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Mama's Hug", value="Whenever Pam hits enemies with Scrapstorm, she heals herself and nearby friendly Brawlers for 48 health.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Mama's Squeeze", value="Healing turret now also damages enemies for 800 damage per second.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Frank

@client.command(aliases=['brawlerinfo-frank'])
async def brawlerifrank(ctx):
  embed=discord.Embed(title="Frank", description="All info on Frank", color=0xdd61ff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/5/55/Frank_Skin-Default.png/revision/latest?cb=20200811175300")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/6/63/Frank_Portrait.png/revision/latest?cb=20200304182409")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Frank swings his hammer at enemies, sending a shockwave. His Super is an especially powerful blow that stuns enemies!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Hammer Hit**", value="Frank takes a while to wind up his hammer blow, but the hit is so hard it sends a shockwave.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Stunning Blow**", value="Frank's greatest hit sends a shockwave that destroys environment and stuns enemies for a while.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Active Noise Canceling", value="Frank clears any disabling effect on himself, and momentarily becomes immune to stuns, slows and knockbacks.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Irresistible Attraction", value="Frank's next attack also pulls opponents towards him.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Power Grab", value="Frank's next attack also pulls opponents towards him.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Sponge", value="Frank's next attack also pulls opponents towards him.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Bibi

@client.command(aliases=['brawlerinfo-bibi'])
async def brawleribibi(ctx):
  embed=discord.Embed(title="Bibi", description="All info on Bibi", color=0xdd61ff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/c/c4/Bibi_Skin-Default.png/revision/latest?cb=20210903094636")
  embed.set_thumbnail(url="https://owwya.com/wp-content/uploads/2019/11/Brawl-Stars-Bibi.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Batter up! Bibi's got a sweet swing that can knock back enemies when her Home Run bar is charged. Her Super is a bouncing ball of gum that deals damage.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Three Strikes**", value="Bibi swings her baseball bat. When she has three swings at the ready, her Home Run bar will charge. Once fully charged, her next swing will knock back enemies!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Spitball**", value="Bibi bats a bouncing ball of bubble gum that can go through enemies, and even hit the same target multiple times!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Vitamin Booster", value="Bibi heals 600 health per second for 4 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Home Run", value="Bibi's movement speed is increased by 12% when her Home Run bar is fully charged.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Batting Stance", value="When Bibi’s Homerun bar is fully charged, she shields herself from all damage by 20%.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Bea

@client.command(aliases=['brawlerinfo-bea'])
async def brawleribea(ctx):
  embed=discord.Embed(title="Bea", description="All info on Bea", color=0xdd61ff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/7/73/Bea_Skin-Default.png/revision/latest?cb=20210319100234")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/a/ae/Bea_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200317100451")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Bea loves bugs and hugs. She shoots her mechanical drones at range, and her Super sends forth an angry army of swarming bees!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Big Sting**", value="Bea sends out a long range shot that, upon landing, supercharges her next shot to deal epic damage!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Iron Hive**", value="Bea deploys a swarm of drones that move and turn like jets. They slow down any opponents caught in their path.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Honey Molasses", value="Bea drops a beehive with a splash of sticky honey around it. The honey slows down enemies that step in it.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Rattled Hive", value="Bea unleashes 4 angry bees that circle away from her, dealing more damage the further they go (up to 600 damage).", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Insta Beeload", value="Instantly supercharge Bea's Big Sting one time if she misses a supercharged shot.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Honeycomb", value="Bea receives a 20% shield while Dig Sting is supercharged.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#NaNi

@client.command(aliases=['brawlerinfo-nani'])
async def brawlerinani(ctx):
  embed=discord.Embed(title="Nani", description="All info on Nani", color=0xdd61ff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/2/20/Nani_Skin-Default.png/revision/latest?cb=20201128223906")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/c/c0/Nani_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200513144321")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Nani loves her friends and looks over them with a watchful lens. She handles threats with angled shots, and her Super allows Nani to commandeer her pal Peep, who goes out with a bang!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Trigger-Nometry**", value="Nani shoots 3 light orbs that move at different angles and converge at max range.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Manual Override**", value="Nani takes control of Peep and can steer him remotely into enemies, exploding on contact!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Warp Blast", value="Nani detonates Peep and teleports herself to his last location.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Return to Sender", value="For the next 5 seconds, the first time Nani takes damage from an enemy, 80% of the damage is returned to the enemy.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Autofocus", value="Peep deals up to 1600 extra damage based on his travel distance.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Tempered Steel", value="Nani takes 80% less damage while her Super is active.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Edgar

@client.command(aliases=['brawlerinfo-edgar'])
async def brawleriedgar(ctx):
  embed=discord.Embed(title="Edgar", description="All info on Edgar", color=0xdd61ff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/2/2b/Edgar_Skin-Default.png/revision/latest?cb=20210106214320")
  embed.set_thumbnail(url="https://owwya.com/wp-content/uploads/2021/01/Brawl-Stars-Edgar-Icon.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Let's face it, this is an angry kid. He also loves parkour.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Fight Club**", value="Hits enemies with quick punches, healing himself for each landed punch.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Vault**", value="Edgar jumps over any obstacle and gets a temporary speed boost. His Super will slowly charge over time.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Let's Fly", value="Edgar's Super charges faster, 525% for 4 seconds.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Hardcore", value="Edgar gets a shield that protects him from the next 2000 damage. The shield gets weaker over time.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Hard Landing", value="Edgar's Super will also deal 1000 damage to nearby enemies upon landing.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Fisticuffs", value="Edgar receives 25% more healing from damage he deals.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Griff

@client.command(aliases=['brawlerinfo-griff'])
async def brawlerigriff(ctx):
  embed=discord.Embed(title="Griff", description="All info on Griff", color=0xdd61ff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/0/0f/Griff_Skin-Default.png/revision/latest?cb=20210616182427")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/c/c9/Griff_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20210616224003")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Griff is the proprietor of Starr Park's gift shop. Business is bad, but he still throws coins away - from his employees' tip jar!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Coin Toss**", value="Angry Griff pelts opponents with coins. He throws three salvos that spread out in a cone.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Cashback**", value="Griff throws a bunch of sharp-edged banknotes in a wide cone. Too valuable to just give away, they return to him, and may cause paper cuts twice to the same target. Opponents further away take more damage.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Piggy Bank", value="Griff drops a firecracker-filled piggy bank that, after a short delay, explodes destroying obstacles and dealing 1000 damage to opponents within range.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Keep the Change", value="Furious Griff tosses coins faster, reducing the time for a full salvo by 35%.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Business Resilience", value="Every 2 seconds, Griff regains up to 7% of his missing health.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)


#Grom

@client.command(aliases=['brawlerinfo-grom'])
async def brawlerigrom(ctx):
  embed=discord.Embed(title="Grom", description="All info on Grom", color=0xdd61ff)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/0/0a/Grom_Skin-Default.png/revision/latest?cb=20211222184112")
  embed.set_thumbnail(url="https://www.brawler.gg/_next/image?url=https%3A%2F%2Fstatic.brawler.gg%2Fimages%2Fportraits%2Fgrom-portrait.48ad8b8cfd.png&w=208&q=75")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Watchman Grom's priority is to keep guard. He throws his trusty radio at his enemies. His Super is a big bad bomb that breaks walls and pushes back enemies!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Bud go Boom!**", value="Grom hurls Bud, his exploding walkie-talkie! The blast moves in the shape of a cross, hurting enemies caught in its path.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Grom Bomb'**", value="Grom launches a devastating bomb with Bud's help! The Grom Bomb inflicts huge damage, breaks walls and the force from its blast pushes all enemies backwards.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Watchtower", value="Grom ejects a Watchtower from his Grom Bomb that gives all allies sight into bushes over a large area. The watchtower slowly loses health over time.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Radio Check", value="Grom's next attack throws 3 Buds in rapid succession.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Foot Patrol", value="When Grom's Super is fully charged, he gains +15% faster movement speed!", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - X-Factor", value="The split from Grom's main attack deals up to +30% extra damage at max distance.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)
#Mythics
#Tara

@client.command(aliases=['brawlerinfo-tara'])
async def brawleritara(ctx):
  embed=discord.Embed(title="Tara", description="All info on Tara", color=0xff5454)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/a/a7/Tara_Skin-Default.png/revision/latest?cb=20200713183458")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/4/49/Tara_Portrait.png/revision/latest?cb=20190630191241")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Tara's triple tarot card attack pierces through enemies. Her Super is a black hole that sucks in all nearby enemies, causing damage!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Triple Tarot**", value="Tara flicks her wrist, snapping off three tarot cards that pierce through enemies. Quite a trick!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Gravity**", value="Tara conjures up a mind-boggling gravity well! Enemies in the area of effect get pulled in, crashing together painfully hard.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Psychic Enhancer", value="Tara and her allies are able to see all enemies, even inside bushes, for 4 seconds.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Support from Beyond", value="Tara surrounds herself with three weak shadows that attack enemies and disappear after 6 sec", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Black Portal", value="Tara's Super cracks open a dimensional portal! A shadowy version of Tara appears and attacks her enemies.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Healing Shade", value="Tara’s Super cracks open a dimensional portal! A shadowy version of Tara’s appears to heal Tara and her teammates.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Mortis

@client.command(aliases=['brawlerinfo-mortis'])
async def brawlerimortis(ctx):
  embed=discord.Embed(title="Mortis", description="All info on Mortis", color=0xff5454)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/b/b2/Mortis_Skin-Default.png/revision/latest?cb=20191016142700&path-prefix=de")
  embed.set_thumbnail(url="https://brawlstarsup.com/wp-content/uploads/2018/12/mortis.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Mortis dashes forward with each swing of his shovel. As his Super attack, he sends a cloud of bats to damage enemies and heal himself!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Shovel Swing**", value="Mortis dashes forward with a sharp swing of his shovel, creating business opportunities for himself.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Life Blood**", value="Mortis calls forth a swarm of vampire bats that drain the health of his enemies while restoring his. Creepy!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Combo Spinner", value="Mortis spins his shovel, hitting all enemies around himself for 1300 damage.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Survival Shovel", value="Mortis reloads faster for 4 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Creepy Harvest", value="Mortis reaps the life essence of Brawler he defeats, restoring 1800 of his health.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Coiled Snake", value="Mortis gains his longer dash 1.5 seconds faster.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Gene

@client.command(aliases=['brawlerinfo-gene'])
async def brawlerigene(ctx):
  embed=discord.Embed(title="Gene", description="All info on Gene", color=0xff5454)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/5/54/Gene_Skin-Default.png/revision/latest?cb=20200608115231")
  embed.set_thumbnail(url="https://brawlace.com/assets/images/icons-players/28000038.png?v=12.8")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Gene uses his magic lamp to shoot a splitting projectile. His super is a magical hand that grabs and pulls enemies close!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Smoke Blast**", value="Gene shoots a solid ball of magical smoke from his lamp. If the ball doesn't hit a target, it splits up and spreads the damage in a cone.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Magic Hand**", value="Gene launches a magical hand from his lamp. If the hand hits an enemy, they get pulled back to Gene's location!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Lamp Blowout", value="All enemies close to Gene are instantly pushed back. If at least one enemy Brawler is within range, Gene will also restore 600 health.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Vengeful Spirits", value="Gene shoots a homing missile at all visible enemies within a large area, dealing up to 1000 damage based on distance.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Magic Puffs", value="Gene heals all friendly Brawlers around him for 400 health per second.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Spirit Slap", value="When Gene's Super is fully charged he does +300 damage with his attack.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Max

@client.command(aliases=['brawlerinfo-max'])
async def brawlerimax(ctx):
  embed=discord.Embed(title="Max", description="All info on Max", color=0xff5454)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/3/33/Max_Skin-Default.png/revision/latest?cb=20201110222310")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/8/83/Max_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20201022114240")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Max goes fast! Her attack is a fast-firing blaster. Her Super speeds up her and allies!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Faster Blaster**", value="Max's blaster shoots a bunch of projectiles fast! It holds a lot of rounds, and Max is quick with the reload.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Let's Go!**", value="Max momentarily boosts up her movement speed and that of nearby allies. Gotta go fast!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Phase Shifter", value="Max dashes forward, and becomes immune to all damage from enemies while dashing.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Sneaky Sneakers", value="Max blinks back to a place of her choosing after 3 seconds' delay, recovering any damage she received in the meantime.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Super Charged", value="Max now charges her Super while moving.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Run n' Gun", value="Max reloads faster while moving.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#MrP

@client.command(aliases=['brawlerinfo-mrp'])
async def brawlerimrp(ctx):
  embed=discord.Embed(title="Mr P", description="All info on Mr P", color=0xff5454)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/a/a4/Mr._P_Skin-Default.png/revision/latest?cb=20200517073422")
  embed.set_thumbnail(url="https://owwya.com/wp-content/uploads/2020/01/Brawl-Stars-Mr.-P.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Mr. P is a disgruntled luggage handler who angrily hurls suitcases at opponents. His Super calls robo-porters to help him.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Your Suitcase, Sir!**", value="Mr. P throws a heavy suitcase with angry intent. If the suitcase hits an obstacle or an opponent, it bounces over them, lands with a bang and deals area damage.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Porters! Attack!**", value="Mr. P deploys the home base for his robo-porters. He has reprogrammed the small penguin-head robots to attack and harass opponents (and unruly guests).", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Service Bell", value="Mr. P buffs his current porter by increasing its damage by 150 and health by 1000.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Porter Reinforcements", value="The next attack will spawn an extra porter where the attack lands.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Handle with Care", value="Mr.P's overstuffed suitcases bounce and burst even if they don't hit a target or obstacle.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Revolving Door", value="The robo-porters respawn 3 seconds faster after being defeated.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Sprout

@client.command(aliases=['brawlerinfo-sprout'])
async def brawlerisprout(ctx):
  embed=discord.Embed(title="Sprout", description="All info on Sprout", color=0xff5454)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/e/ec/Sprout_Skin-Default.png/revision/latest?cb=20200522051055")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/4/4d/Sprout_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200404120105")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Sprout was built to plant life, launching bouncy Seed Bombs with reckless love. Its Super creates a plant-based obstacle!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Seed Bomb**", value="Sprout propels a ball of seeds that bounces around before bursting with a bang! If it makes contact with enemies, it explodes on impact.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Hedge**", value="Sprout uses its Super Seed to grow a thick vine hedge, creating an impassable though temporary obstacle.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Garden Mulcher", value="Sprout consumes a bush to restore 1500 health.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Transplant", value="Sprout destroys its current Hedge, but will instantly have its Super fully charged again.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Overgrowth", value="Every 5 seconds, the next Seed Bomb will explode with a larger explosion radius.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Photosynthesis", value="Sprout activates a shield, partially protecting itself from all attacks while inside a bush.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Byron

@client.command(aliases=['brawlerinfo-byron'])
async def brawleribyron(ctx):
  embed=discord.Embed(title="Byron", description="All info on Byron", color=0xff5454)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/4/41/Byron_Skin-Default.png/revision/latest?cb=20210106213109")
  embed.set_thumbnail(url="https://owwya.com/wp-content/uploads/2021/01/Brawl-Stars-Byron-Icon.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Byron deals with potent medicaments, but never call him a snake oil salesman!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Careful Dose**", value="Shoots a long range dart that can hit both opponents and friendlies. Opponents will take damage over time and friendlies will heal over time.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Full Treatment**", value="Throws a vial that heals friendlies and damages opponents.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Shot in the Arm", value="Byron uses one of his shots to heal himself 800 per second for 3 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Malaise", value="Byron's Super will also cause opponents to receive 75% less healing from any source for 9 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Injection", value="Every 3.5 seconds the next basic attack will pierce through targets.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Squeak

@client.command(aliases=['brawlerinfo-squeak'])
async def brawlerisqueak(ctx):
  embed=discord.Embed(title="Squeak", description="All info on Squeak", color=0xff5454)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/c/cf/Squeak_Skin-Default.png/revision/latest?cb=20210525145828")
  embed.set_thumbnail(url="https://owwya.com/wp-content/uploads/2021/04/Brawl-Stars-Squeak-Icon.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="As Col. Ruff's accidental creation, Squeak was born to play fetch!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Sticky Bomb**", value="Squeak's sticky blobs of goo are unstable, and blow up with a big splash and an ouch! They attach to any opponent they hit outright, as well as any opponent that strays too near to a blob on the ground.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Big Blob**", value="Squeak lobs a blob that, after a short delay, blows up with aplomb! The explosion of goo stuns nearby opponents, and sends six smaller Sticky Blombs in all directions.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Windup", value="Squeak's next Sticky Blomb has its range increased by 100%.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Chain Reaction", value="Each opponent within the area of a Sticky Blomb's explosion increases the Blomb's damage by 10%.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Super Sticky", value="Secondary Sticky Blomb explosions from Squak's Super also slow down opponents for 4 seconds.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Legendaries
#Spike

@client.command(aliases=['brawlerinfo-spike'])
async def brawlerispike(ctx):
  embed=discord.Embed(title="Spike", description="All info on Spike", color=0xf9ff45)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/8/8e/Spike_Skin-Default.png/revision/latest?cb=20200712190313")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/2/22/Spike_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200304182450")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Spike throws cactus grenades that send needles flying, and a show-stopping Super: a field of cactus spines that slows down and damages enemies!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Needle Grenade**", value="Spike fires off a small cactus that explodes, shooting spikes in different directions.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Stick Around!**", value="Spike lobs a thorny grenade. Enemies caught in the blast area take damage and are slowed down.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Popping Pincushion", value="Spike shoots 3 waves of needles in all directions, dealing 520 damage per hit.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Life Plant", value="Spike grows a large cactus with 3500 health to give cover to friendlies. If destroyed, the cactus bursts, and all nearby friendlies recover 1000 health.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Fertilize", value="After using Super, Spike regenerates 800 health per second by staying in its area of effect.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Curveball", value="Spikes from cactus grenade fly in a curving motion, making it easier to hit targets.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Crow

@client.command(aliases=['brawlerinfo-crow'])
async def brawlericrow(ctx):
  embed=discord.Embed(title="Crow", description="All info on Crow", color=0xf9ff45)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/a/a2/Crow_Skin-Default.png/revision/latest?cb=20201107182328")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/6/6f/Crow_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200706075842")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Crow fires a trio of poisoned daggers. As a Super move he leaps, firing daggers both on jump and on landing!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Switchblade**", value="Crow throws a triple threat of daggers. Enemies nicked by the poisoned blades will take damage over time.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Swoop**", value="Crow takes to the skies, throwing a ring of poisoned daggers around him both on take-off and landing.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Defense Booster", value="Crow gets a shield for 40% of incoming damage for 3 seconds.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Slowing Toxin", value="All currently poisoned enemies are slowed for 5 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Extra Toxic", value="Crow's poison saps the strength of enemies, who deal 25% less damage while poisoned.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Carrion Crow", value="Crow deals +152 damage with his attack and Super to targets with 50% or less health.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Leon

@client.command(aliases=['brawlerinfo-leon'])
async def brawlerileon(ctx):
  embed=discord.Embed(title="Leon", description="All info on Leon", color=0xf9ff45)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/3/33/Leon_Skin-Default.png/revision/latest?cb=20190928133717&path-prefix=de")
  embed.set_thumbnail(url="https://brawlstarsup.com/wp-content/uploads/2018/12/leon.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Leon shoots a quick salvo of blades at his target. His Super trick is a smoke bomb that makes him invisible for a little while!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Spinner Blades**", value="Leon flicks his wrist and fires four Spinner Blades. The blades deal less damage the farther they travel.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Smoke Bomb**", value="Leon becomes invisible for 6 seconds. If he attacks, he will be revealed. Enemies close to Leon will be able to spot him.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Clone Projector", value="Leon creates an illusion of himself to confuse his enemies.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Lollipop Drop", value="Leon creates a stealthy area for his team to hide in.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Smoke Trails", value="When Leon uses his Super, he gains 30% boost to his movement speed for the duration of his invisibility.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Invisiheal", value="Leon recovers 1000 health per second while his Super is active.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Sandy

@client.command(aliases=['brawlerinfo-sandy'])
async def brawlerisandy(ctx):
  embed=discord.Embed(title="Sandy", description="All info on Sandy", color=0xf9ff45)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/8/80/Sandy_Skin-Default.png/revision/latest?cb=20200226195634")
  embed.set_thumbnail(url="https://owwya.com/wp-content/uploads/2019/11/Brawl-Stars-Sandy.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Sandy is a sleep-deprived Brawler with powerful control over sand: casting sharp pebbles at enemies, and summoning a sandstorm to hide teammates.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Pebble Blast**", value="Sandy pelts enemies with sharp, piercing pebbles. Ouch!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Sandstorm**", value="Sandy summons a sandstorm that lasts for 9 seconds and hides friendly Brawlers inside it.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Sleep Stimulator", value="Sandy falls a sleep for 2 seconds and his health is fully restored.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Sweet Dreams", value="Sandy's next attack lulls opponents to sleep for 1.0 seconds. They will however wake up from any damage.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Rude Sands", value="Sandstorm now also damages enemies for 100 damage per second.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Healing Winds", value="Sandstorm now also heals friendly Brawlers for 300 health per second.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Amber

@client.command(aliases=['brawlerinfo-amber'])
async def brawleriamber(ctx):
  embed=discord.Embed(title="Amber", description="All info on Amber", color=0xf9ff45)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/a/a3/Amber_Skin-Default.png/revision/latest?cb=20201108094559")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/9/96/Amber_Portrait.png/revision/latest?cb=20201022114232")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Amber has always been a firebug. She loves to light up the world and any opponents that come at her!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Dragon's Breath**", value="Amber blows a flaming inferno at her opponents. It looks awesome, but watch out or you'll get seared!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Torch'em!**", value="Amber blows a flaming inferno at her opponents. It looks awesome, but watch out or you'll get seared!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Fire Starters", value="Amber runs fast for 3 seconds while spilling her fire fluid, which she can then ignite.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Wild Flames", value="Amber can have two fuel puddles on the ground simultaneously and she will recharge her Super automatically when standing near one.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Scorchin' Siphon", value="While being near a puddle of fire fluid, Amber uses it to reload her firebreathing 50% faster.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Meg

@client.command(aliases=['brawlerinfo-meg'])
async def brawlerimeg(ctx):
  embed=discord.Embed(title="Meg", description="All info on Meg", color=0xf9ff45)
  embed.set_image(url="https://www.brawlstarsdicas.com.br/wp-content/uploads/2021/09/meg-brawl-stars-skin-padrao.png")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/5/58/Meg_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20210925184245")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Meg has a basic form and an advanced form where she hops inside her trusted Mecha. The Mecha loses health over time and has low healing ability. Destroying the Mecha returns Meg to her basic form.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Target Acquired**", value="Meg fires a short burst from her blaster that pokes at her enemies´ patience.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Mega Machina**", value="Meg jumps into her Mecha for some colossal carnage!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Jolting Volts", value="Heal the Mecha by 450 health per second for 5 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Force Field", value="Meg is protected by a 35% shield for 30 seconds when her Mecha is destroyed.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Chromatics
#Gale

@client.command(aliases=['brawlerinfo-gale'])
async def brawlerigale(ctx):
  embed=discord.Embed(title="Gale", description="All info on Gale", color=0xff42a4)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/1/1e/Gale_Skin-Default.png/revision/latest/scale-to-width-down/2000?cb=20201110085459")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/3/3f/Gale_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200513143833")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Gale is a tireless handyman who gets no rest. He blasts foes with a wide shot of wind and snow and his Super pushes them back with a huge gust of wind!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Polar Vortex**", value="Gale blasts a large snow ball wall at his enemies!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Gale Force!**", value="Gale delivers an almighty gust of wind and snow, pushing back all enemies caught in its path.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Spring Ejector", value="Gale drops a bounce pad underfoot, launching friend and foe alike into the air.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Twister", value="Gale uses his leaf blower to create a local tornado, which will push away any opponents that try to pass through.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Blustery Blow", value="Gale's Super now stuns enemies for 1.0 seconds if they are pushed against obstacles.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Freezing Snow", value="Gale's snow balls now also slow down opponents for 0.5 seconds.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Surge

@client.command(aliases=['brawlerinfo-surge'])
async def brawlerisurge(ctx):
  embed=discord.Embed(title="Surge", description="All info on Surge", color=0xff42a4)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/c/cf/Surge_Skin-Default.png/revision/latest?cb=20210306205238")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/2/27/Surge_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200706075845")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="He's a Protector with a penchant for parties. Surge attacks foes with energy drink blasts that split in two on contact. His Super upgrades his stats in 3 stages and comes complete with totally awesome body mods!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Juice of Justice**", value="Surge serves a shot of Juice that splits in two on contact with enemies.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Party Tricks**", value="With each Super, Surge gets upgraded (MAX 3). Upgrades are lost when Surge is defeated. | STAGE 1: Boosted movement speed | STAGE 2: Increased weapon range | STAGE 3: Main attack splits into 6 (instead of 2)", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Power Surge", value="Surge overloads his circuits and teleports a short distance forward.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - To the Max!", value="Surge's main attack now splits when hitting walls or when reaching max distance.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Serve Ice Cold", value="Surge keeps his STAGE 1 Super upgrade for the full match duration.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#COLETTE

@client.command(aliases=['brawlerinfo-colette'])
async def brawlericolette(ctx):
  embed=discord.Embed(title="Colette", description="All info on Colette", color=0xff42a4)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/6/63/Colette_Skin-Default.png/revision/latest?cb=20201113164723")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/e/e8/Colette_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20200911212332")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Colette is going to get you! She taxes opponents' health and has fancy moves to boot.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Taxing Shot**", value="Colette fires a shot that takes what you owe - you or your bear! And the more you have, the more you owe.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Time to Collect**", value="Colette makes a dash forth and back, dealing taxing damage to everyone in her path, based on their maximum health.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Na-ah!", value="Colette's next shot deals extra 1000 damage.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Push It", value="All enemy brawlers hit by Colette's charge are carried to the farthest point of the attack!", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Mass Tax", value="Colette's super gives her a 20% shield for 5 seconds. Every enemy brawler hit by it will add 10% more protection.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Lou

@client.command(aliases=['brawlerinfo-lou'])
async def brawlerilou(ctx):
  embed=discord.Embed(title="Lou", description="All info on Lou", color=0xff42a4)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/6/60/Lou_Skin-Default.png/revision/latest/scale-to-width-down/360?cb=20210127074241&path-prefix=de")
  embed.set_thumbnail(url="https://cdn.brawlify.com/brawler/Lou.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Lou is a cool guy, literally! He can dole out all kinds of chill stuff. But watch your step on the ice, and be careful not to get brain freeze!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Brain Freeze**", value="Barraging opponents with snow cones, Lou can eventually freeze them in place for 1.0 seconds.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Can-Do**", value="Lou lobs a can of freezing cold syrup that creates an icy, slippery area on the ground. Very tough for his opponents' fancy footwork!", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Ice Block", value="Lou shields himself with ice, becoming invulnerable for 1.0 seconds.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Cryo Syrup", value="Instantly adds 50% freeze meter to opponents inside Lou's Super.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Supercool", value="Opponents standing on Lou's Super area get gradually frozen, like from his Brain Freeze attack.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Hypothermia", value="Opponents lose up to 75% of their reload speed based on how frozen they are from Lou's attacks.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Col Ruffs

@client.command(aliases=['brawlerinfo-colonelruffs', 'brawlerinfo-colruffs', 'brawlerinfo-ruffs'])
async def brawlericolonelruffs(ctx):
  embed=discord.Embed(title="Colonel Ruffs", description="All info on Colonel Ruffs", color=0xff42a4)
  embed.set_image(url="https://www.brawler.gg/_next/image?url=%2Fassets%2Fimages%2Fskins%2Fdefault-colonel-ruffs-skin.png&w=640&q=75")
  embed.set_thumbnail(url="https://owwya.com/wp-content/uploads/2021/02/Brawl-Stars-Colonel-Ruffs-Icon.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Ruffs fires twin shots of lasers that bounce off walls. His Super is a supply drop that can damage enemies in the drop zone and leaves a power up for your team to use.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Double-Barrel Laser**", value="Ruffs' twin-laser bounces off walls multiple times. They can hit enemies behind cover.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Supply Drop**", value="Ruffs calls upon a supply drop that can damage enemies in the landing area and leaves a power-up for friendly brawlers to pick up. The power-up increases health and damage. It is does not stack and is lost on death.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Take Cover", value="Ruffs throws down 3 sandbags to cover himself. Each one has 2000 health.", inline=True)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Air Support", value="Ruffs throws down 3 sandbags to cover himself. Each one has 2000 health.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Air Superiority", value="Supply Drop now includes a bomb that adds +1000 damage to the drop and also allows it to destroy walls.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Field Promotion", value="Friendly Brawlers have their maximum health increased by 30 every second that they are in range of this ability while it's active.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Belle

@client.command(aliases=['brawlerinfo-belle'])
async def brawleribelle(ctx):
  embed=discord.Embed(title="Belle", description="All info on Belle", color=0xff42a4)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/d/d9/Belle_Skin-Default.png/revision/latest?cb=20210419032608")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/8/82/Belle_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20210406000502")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Belle inspires adoration in her gang, while her Electo-Rifle brings shock and awe to any opponent!", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Shocker**", value="Belle shoots a long range Electro-Bolt, dealing damage to any target hit. After a short delay, the bolt will jump to any nearby target, deal damage and jump to the next one, until there are no valid targets in range.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Spotter**", value="Belle fires a spotting shot that marks any opponent it hits. The marked opponent takes extra damage from any source. Only one target can be marked at a time.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Nest Egg", value="Belle places a trap on the ground that will explode when triggered by an opponent. The trap deals 500 damage, and slows down anyone within its blast radius for 3 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Positive Feedback", value="Belle gains a 20% shield whenever her Electro-Bolts hit a target.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Grounded", value="Getting marked by Belle's Super prevents the target from reloading for 3 seconds.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Buzz

@client.command(aliases=['brawlerinfo-buzz'])
async def brawleribuzz(ctx):
  embed=discord.Embed(title="Buzz", description="All info on Buzz", color=0xff42a4)
  embed.set_image(url="https://static.wikia.nocookie.net/brawlstars/images/6/62/Buzz_Skin-Default.png/revision/latest?cb=20210913083109")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/2/2c/Buzz_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20210614220112")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Buzz is the lifeguard at Velocirapids. He constantly scans for folks in trouble he can throw his torpedo buoy to, but his throws are rather overenthusiastic.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Buzz off**", value="Buzz throws five quick slaps in an arc.", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Torpedo Throw**", value="Buzz throws out his torpedo buoy. If it hits an opponent or a wall, Buzz hauls himself over there, stunning nearby opponents where he lands.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Reserve Buoy", value="Instantly fills the Super meter, but the next Torpedo Throw doesn't stun opponents.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Tougher Torpedo", value="The minimum duration of Buzz's Super stun is increased by 0.5 seconds.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Eyes Sharp", value="Buzz's Super charging area is increased by 33%.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Ash

@client.command(aliases=['brawlerinfo-ash'])
async def brawleriash(ctx):
  embed=discord.Embed(title="Ash", description="All info on Ash", color=0xff42a4)
  embed.set_image(url="https://media.brawltime.ninja/brawlers/ash/model.png?size=500")
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/brawlstars/images/9/92/Ash_Portrait.png/revision/latest/scale-to-width-down/1200?cb=20210825233042")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Ash easily gets furious about all the junk he has to clean up. Dealing or receiving blows, even more so. The Fury makes him faster and more dangerous, but eventually he cools down.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Clean-up**", value="Ash angrily smashes down with his broom. Get out of the way or you might bite the dust!", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Little Helpers**", value="Robotic rats for cleaning up? That's right, they explode on contact, dealing damage to opponents and greatly increasing Ash's Rage level.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Chill Pill", value="Though furious, Ash has to collect himself. A full Rage meter will recover 2500 health when this gadget is popped - less Rage, less recovery.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - First Bash", value="When hitting an opponent with his attack charges full, Ash gets even more angry. His Rage goes up by 100%.", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)

#Lola
@client.command(aliases=['brawlerinfo-lola'])
async def brawlerilola(ctx):
  embed=discord.Embed(title="Lola", description="All info on Lola", color=0xff42a4)
  embed.set_image(url="https://www.brawlstarsdicas.com.br/wp-content/uploads/2021/10/brawler-lola-win-pose-brawl-stars-dicas.png")
  embed.set_thumbnail(url="https://cdn1.dotesports.com/wp-content/uploads/2021/10/23104245/image_2021-10-23_174244-768x432.png")
  embed.add_field(name="**<:Info:901525872878706778> General info**", value="Despite being just a guide, Lola portrays herself as THE leading lady on Brawlywood. She attacks with her scarf and her super is a channeled manisfestation of her Ego.", inline=False)
  embed.add_field(name="**<:Attack:901525850778918955> Attack - Diamond Eyes**", value="Lola uses the eyes of here fake fox to fire sparkly projectiles at her enemies. ", inline=True)
  embed.add_field(name="<:Super:901525862900441179> **Super - Megalomaniac**", value="Lola spawns her Ego nearby which is a clone of herself that exactly does what she does.", inline=True)
  embed.add_field(name="**Gadgets & Starpowers**", value="List of additional abilities when reaching Power 7 or Power 9", inline=False)
  embed.add_field(name="<:Gadget_Filler:901434010385928203> Gadget - Freeze Frame", value="Lola's Ego stops moving for 4 seconds and gains a **75%** shield", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Improvise", value="When Lola only has one ammo loaded, her next shot's damage will increase by 30%.", inline=True)
  embed.add_field(name="<:Star_Power_Filler:901524938341638194> Starpower - Sealed With a Kiss", value="When Lola's Ego hits allies with its attack, it will pierce through them and heal them by 100HP per projectile", inline=True)
  embed.set_footer(text="CC: Navigator")
  
  await ctx.send(embed=embed)




#Breaksoon

#meme

  
@client.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.send(embed=meme)


#whois

@client.command(name="whois")
async def whois(ctx,user:discord.Member=None):
    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)


    embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}"),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'Requested by - {ctx.author}',
  icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=user.joined_at,inline=False)

  
 
    embed.add_field(name='Bot?',value=user.bot,inline=False)

    embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
    embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)

    await ctx.send(embed=embed) 


#Suggestion


@client.command()
async def suggest(ctx, *, suggestion):
  user=ctx.author
  await ctx.channel.purge(limit = 1)
  channel = client.get_channel(958318346921713664)
  suggestEmbed = discord.Embed(colour = user.color)
  suggestEmbed.set_author(name=f'Suggested by {ctx.message.author}', icon_url = f'{ctx.author.avatar_url}')
  suggestEmbed.add_field(name = 'New suggestion!', value = f'{suggestion}')
  message = await channel.send(embed=suggestEmbed)
  await message.add_reaction('✅')
  await message.add_reaction('❌')


#Report

@client.command()
async def report(ctx, *, suggestion):
  user=ctx.author
  await ctx.channel.purge(limit = 1)
  channel = client.get_channel(952984361257541643)
  suggestEmbed = discord.Embed(colour = user.color)
  suggestEmbed.set_author(name=f'Reported by {ctx.message.author}', icon_url = f'{ctx.author.avatar_url}')
  suggestEmbed.add_field(name = 'New report!', value = f'{suggestion}')
  message = await channel.send(embed=suggestEmbed)
  await message.add_reaction('✅')
  await message.add_reaction('❌')

#Serverinfo


@client.command()
async def serverinfo(ctx):
    user=ctx.author
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title=name + " Server Information", description=description, colour=user.color)
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    await ctx.send(embed=embed)


#Botservers

@client.command()
async def botservers(ctx):
  user=ctx.author
  em = discord.Embed(title = "Here are a few servers I am in!", colour=user.color)

  for guild in client.guilds:
        name = guild.name
        members = len(guild.members)
        em.add_field(name = name, value = f"Member count: {members}")

  await ctx.send(embed = em)


@client.command()
async def krdm(ctx, user: discord.User, *, message=None):
    message = message or "The person who sent you this message didn't include an actual message, sorry."
    await user.send(message)





@client.command()
async def mc(ctx, arg):
    r = requests.get('https://api.minehut.com/server/' + arg + '?byName=true')
    json_data = r.json()

    description = json_data["server"]["motd"]
    online = str(json_data["server"]["online"])
    playerCount = str(json_data["server"]["playerCount"])

    embed = discord.Embed(
        title=arg + " Server Info",
        description='Description: ' + description + '\nOnline: ' + online + '\nPlayers: ' + playerCount,
        color=discord.Color.dark_green()
    )
    embed.set_thumbnail(url="https://i1.wp.com/www.craftycreations.net/wp-content/uploads/2019/08/Grass-Block-e1566147655539.png?fit=500%2C500&ssl=1")

    await ctx.send(embed=embed)

print ("MineCraft Server Loaded By Golden")
print ("Neyo Golden's IP is 192.18.0.173:8080/")
print ("Due to COVID OUR API'S ARE DOWN")


#Tic Tac Toe

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn. Place using the *place <integer> command")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn. Place using the *place <integer> command!")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the *tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@Golden4>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

  



@client.command()
async def myip(ctx):
  ip = get('https://api.ipify.org').text
  embed=discord.Embed(
    title = "Public IP", 
    description = "IP: " + ip, 
    color = discord.Color.green()
  )
  return await ctx.send(embed=embed)
  embed.set_footer(text="This command works under an api. We aren't a resposibile for this!")









import secondary



@client.command()
async def profile(ctx):
    with open("data.json","r") as f:
        users = json.load(f)
    if str(ctx.author.id) in users:
        tag = users[str(ctx.author.id)]
        profile_info = secondary.get_info(tag)
        rank = secondary.get_rank(profile_info.trophies)
        imageid = secondary.get_logo(tag)
        if profile_info.is_qualified_from_championship_challenge == True:
            qual = "True"
        else:
            qual = "False"
        try:
            club = profile_info.club.name
        except:
            club = "Not in a club"
        brawlers = profile_info.brawlers
        top_brawler = brawlers[0]
        embed = discord.Embed(color=discord.Color.dark_red())
        embed.set_author(name=f" ~| Brawl Stars |~")
        embed.set_thumbnail(url=f"https://cdn.brawlstats.com/player-thumbnails/{imageid}.png")
        embed.add_field(name="Username: ", value=f"{rank[1]} | {profile_info.name}")
        embed.add_field(name="Tag:", value=f"{tag}")
        embed.add_field(name="Trophy Road Rank:", value=f"{rank[1]} | {rank[0]}")
        embed.add_field(name="Trophies:", value=f"{profile_info.trophies} <:Trophy:854606907439710218>")
        embed.add_field(name="Highest Trophies: ", value=f"{profile_info.highest_trophies} <:Trophy:854606907439710218>")
        embed.add_field(name="Exp Level: ", value=f"<:Exp:854978177386283028> {profile_info.exp_level}")
        embed.add_field(name="Club: ", value=f"<:Club:855027618448801805> {club}")
        embed.add_field(name="Qualified For Championship Challenge: ", value=f"<:ChampionshipChallenge:855020961401536532> {qual}")
        await ctx.send(embed=embed)
        second = discord.Embed(color=discord.Color.dark_red())
        second.set_author(name='Brawl Matches')
        second.add_field(name='3v3 Victories:', value=f"<:3v3:855020737445625887> {profile_info.x3vs3_victories}")
        second.add_field(name="Team Victories:", value=f"<:3v3:855020737445625887> {profile_info.team_victories}")
        second.add_field(name="Solo Victories:", value=f"<:SoloShowdown:855020872027734016> {profile_info.solo_victories}")
        second.add_field(name="Duo Victories:", value=f"<:DuoShowdown:855020811630018571> {profile_info.duo_victories}")
        second.add_field(name="Best Robo Rumble Time:", value=f"<:Robo_Rumble:855021062302334987> {profile_info.best_robo_rumble_time}")
        second.add_field(name="Best Time As Big Brawler:", value=f"<:Big_Game:855020746894737408> {profile_info.best_time_as_big_brawler}")
        await ctx.send(embed=second)
    else:
        embed = discord.Embed(color=discord.Color.dark_purple())
        embed.set_author(name="Exception In Command")
        embed.add_field(name="Error", value="Account not registered. $save #<tag> to save your brawl stars account.")
        await ctx.send(embed=embed)








client.command()
async def save(ctx, tag):
    Rlist = await verify_account(ctx.author, tag)
    value = Rlist[0]
    users = Rlist[1]
    if value == "yes":
        embed = discord.Embed(color=discord.Color.dark_purple())
        embed.set_author(name="Exception In Command")
        embed.add_field(name="Error", value="Account already registered. Type $remove to remove your brawl stars account.")
        await ctx.send(embed=embed)
    if value == "no":
        try:
            player = secondary.get_info(tag)
            rank = secondary.get_rank(player.trophies)
            with open("data.json", "w") as f:
                json.dump(users, f)
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Command Successful")
            embed.add_field(name="Added Account.", value=f"Successfully added account {rank[1]} | {player.name} ")
            await ctx.send(embed=embed)
        except:
            await ctx.send("Not A Valid Account")

async def verify_account(user, tag):
    with open("data.json", "r") as f:
        users = json.load(f)
    if str(user.id) in users:
        value = "yes"
    else:
        users[str(user.id)] = tag
        value = "no"
    return value, users

@client.command()
async def remove(ctx):
    with open("data.json","r") as f:
        users = json.load(f)
    if str(ctx.author.id) in users:
        profile = secondary.get_info(users[str(ctx.author.id)])
        users.pop(str(ctx.author.id))
        with open("data.json", "w") as f:
            json.dump(users, f)
        embed = discord.Embed(color=discord.Color.dark_red())
        embed.set_author(name="Command Successful")
        embed.add_field(name="Account Removed.", value=f"Successfully removed account {profile.name}")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(color=discord.Color.dark_purple())
        embed.set_author(name="Exception In Command")
        embed.add_field(name="Error", value="Account not registered. $save #<tag> to save your brawl stars account.")
        await ctx.send(embed=embed)

# For self hosting
keep_alive.keep_alive()
client.run(os.getenv('token4')) 

