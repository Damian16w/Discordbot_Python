import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.members = True  

# Prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Event: Bot online?
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="You..."))

    
# Event: Nieuwe gozer gejoint
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1171816765349695501)
    
    if channel:
        await channel.send(f'Welkom nieuwe makker, {member.mention}!')
    
    guild = member.guild
    channel = bot.get_channel(1171816765777530951)
    await channel.edit(name=f"Aantal leden: {guild.member_count}")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1171816765777530951)

    if channel:
        await channel.send(f'{member.mention} is de server geleaved de groeten!')

        guild = member.guild
    channel = bot.get_channel(1171816765777530951)
    await channel.edit(name=f"Aantal leden: {guild.member_count}")

# Command: !hallo
@bot.command(name='hallo', help='Groet de user!')
async def hallo(ctx):
    await ctx.send('Hallo! Wat kan ik voor je doen?')
    print(f'!hallo is getriggerd')

@bot.command(name='loop', help='loopt')
async def loop(ctx):
   await ctx.send('Loop werkt niet mijn grote vriend!')
   print(f'loop gestart')

# Command: Thierry (Op verzoek van discord user: lucaswhk)
@bot.command()
async def rood(ctx):
    embed=discord.Embed(title="Rode Embed", description="De zijkant en de foto is in het rood!", color=0xad2323)
    embed.set_image(url="https://www.google.com/imgres?imgurl=https%3A%2F%2Fhtmlcolorcodes.com%2Fassets%2Fimages%2Fcolors%2Fred-color-solid-background-1920x1080.png&tbnid=8GW9Eda5iNsSFM&vet=12ahUKEwi1uqvys9KDAxV10AIHHRPqCmgQMygAegQIARBN..i&imgrefurl=https%3A%2F%2Fhtmlcolorcodes.com%2Fcolors%2Fred%2F&docid=YN4iCLvvQo26tM&w=1920&h=1080&itg=1&q=red%20color&ved=2ahUKEwi1uqvys9KDAxV10AIHHRPqCmgQMygAegQIARBN")
    embed.set_footer(text="Dit is een footer")
    await ctx.send(embed=embed)

# Command: !kick
@commands.command(name='kick', help='Gooit iemand uit de server')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, reason=None):
    # dm't de gekickte member
    try:
        await member.send(f'Hey je bent eruit gegooid vanwege, {reason}')
    except discord.Forbidden:
        pass
    
    # Kick
    await ctx.guild.kick(member)
    await ctx.send(f'{member.mention} Is eruit gegooid want, {reason}')
    print(f'{member.mention} is gekickt vanwege {reason}')

bot.add_command(kick)

# Command: !ban
@commands.command(name='ban', help='Verbant iemand uit de server')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, reason=None):
    # dm't de verbannen member
    try:
        await member.send(f'Hey droom zacht je bent verbannen vanwege, {reason}')
    except discord.Forbidden:
        pass
    
    # Logs
    await ctx.guild.ban(member)
    await ctx.send(f'{member.mention} droomt vanavond goed in banland want, {reason}')
    
bot.add_command(ban)

bot.run('MTE4NzMxOTM1MTcxNjYyMjM4Nw.Gl-Yus.KwmQicKMHQ6Jsj3IL-kg5iZDRrzC4ix0Mm4v4w')