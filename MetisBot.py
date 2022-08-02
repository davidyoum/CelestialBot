import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.', intents=intents)
client.remove_command('help')

for filename in os.listdir('./cogs'):
     if filename.endswith('.py'):
         client.load_extension(f'cogs.{filename[:-3]}')

'''
UPDATES
'''
@client.command()
async def up (ctx):
    embed=discord.Embed(title="Metis Update [SERVER]", description="We are Metis", color=0x0047ab)
    embed.set_author(name=" ")
    embed.add_field(name="•Test", value="NAWWWWW", inline=False)
    embed.add_field(name="•Discord Bot", value="added new commands", inline=True)
    embed.set_footer(text="Made By Metis")
    updateChannel = client.get_channel(475110076181512221)
    await updateChannel.send(embed=embed)

'''
HELP
'''
@client.command()
async def help(ctx):
    embed = discord.Embed(title="MetisBot Help", description="Commands: ", color=0x0047AB)
    embed.add_field(name="/help", value="Shows Commands For Bot", inline=False)
    embed.add_field(name="/clear [number of messages]", value="Clears 'x' Amount of Messages", inline=False)
    embed.add_field(name="/kick [username] [reason]", value="Kicks user from server", inline=False)
    embed.add_field(name="/ban [username] [reason]", value="Bans user from server", inline=False)
    embed.add_field(name="/unban [username] [reason]", value="Unbans user from server", inline=False)
    await ctx.author.send(embed=embed)
    await ctx.channel.purge(limit=1)

'''
START UP
'''
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("MetisBot | .help"))

    embed=discord.Embed(title="Metis.", description="The bot is up and running.", color=0x0047AB).set_footer(text="Made By Metis")
    logchannel = client.get_channel(478314520893325322)
    await logchannel.send(embed=embed)

'''
MEMBER JOIN AND LEAVE MESSAGE
'''
@client.event
async def on_member_join(member):
    embed=discord.Embed(title="Welcome to Metis.", description=f"Hello, {member.mention}. Welcome to Metis where we are Metis.", color=0x0047AB).set_footer(text="Made By Metis")
    welcomeLeaveChannel = client.get_channel(792980247498588222)
    await welcomeLeaveChannel.send(embed=embed)

@client.event
async def on_member_remove(member):
    embed=discord.Embed(title="Someone has left Metis.", description=f"{member.mention}, has left.", color=0x0047AB).set_footer(text="Made By Metis")
    welcomeLeaveChannel = client.get_channel(792980247498588222)
    await welcomeLeaveChannel.send(embed=embed)

'''
TEXT
'''
@client.command(name = "hello", pass_context=True)
async def hello (ctx):
    await ctx.channel.send("Hello")

'''
Special Permissions Needed
ADMIN and MODERATION
'''

@client.command(name = "clear", pass_context=True)
@has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

@client.command()
@has_permissions(ban_members=True)
async def unban(ctx, member : discord.Member, *, reason = None):
    await member.unban(reason = reason)

client.run('NzkzMjc4MDA2Nzc2NjkyNzM4.GfvfNn.Q612ORARYiGO7K986QbhenqJdaPWI_r6beZssw')