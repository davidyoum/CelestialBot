import discord
import os
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command('help')


async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

'''
UPDATES
'''


@client.command()
async def up(ctx):
    embed = discord.Embed(title="CelestialDB Update",
                          description="We are Celestial.", color=0x0047ab)
    embed.set_author(name=" ")
    embed.add_field(name="•Ban/Unban",
                    value="Fixed unban function also adding embed messages when peformed.", inline=False)
    embed.set_footer(text="Made By Celestial")
    updateChannel = client.get_channel(475110076181512221)
    await updateChannel.send(embed=embed)

'''
HELP
'''


@client.command()
async def help(ctx):
    embed = await discord.Embed(title="CelestialBot Help",
                                description="Commands: ", color=0x0047AB)
    embed.add_field(name=".help", value="Shows Commands For Bot", inline=False)
    embed.add_field(name=".clear [number of messages]",
                    value="Clears 'x' Amount of Messages", inline=False)
    embed.add_field(name=".kick [username] [reason]",
                    value="Kicks user from server", inline=False)
    embed.add_field(name=".ban [username] [reason]",
                    value="Bans user from server", inline=False)
    embed.add_field(name=".unban [username] [reason]",
                    value="Unbans user from server", inline=False)
    await ctx.author.send(embed=embed)
    await ctx.channel.purge(limit=1)

'''
START UP
'''


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("CelestialBot | .help"))

    embed = await discord.Embed(title="CelestialDB", description="The bot is up and running.",
                                color=0x0047AB).set_footer(text="Made By Celestial")
    logchannel = await client.get_channel(478314520893325322)
    await logchannel.send(embed=embed)

'''
MEMBER JOIN AND LEAVE MESSAGE
'''


@client.event
async def on_member_join(member):
    embed = await discord.Embed(title="Welcome to Celestial.", description=f"Hello, {member.mention}. Welcome to Celestial where we are Celestial.", color=0x0047AB).set_footer(
        text="Made By Celestial")
    welcomeLeaveChannel = await client.get_channel(792980247498588222)
    await welcomeLeaveChannel.send(embed=embed)


@client.event
async def on_member_remove(member):
    embed = await discord.Embed(title="Someone has left Celestial.",
                                description=f"{member.mention}, has left.", color=0x0047AB).set_footer(text="Made By Celestial")
    welcomeLeaveChannel = await client.get_channel(792980247498588222)
    await welcomeLeaveChannel.send(embed=embed)

'''
TEXT
'''


@client.command(name="hello", pass_context=True)
async def hello(ctx):
    await ctx.channel.send("Hello")

'''
Special Permissions Needed
ADMIN and MODERATION
'''


@client.command(name="clear", pass_context=True)
@has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)


@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(title="Kicked User")
    embed.add_field(name="User:", value=f'{member.mention}', inline=True)
    embed.add_field(name="Reason:", value=f'{reason}', inline=True)
    embed.set_footer(text="Made by Celestial")
    await ctx.channel.send(embed=embed)


@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title="Banned User")
    embed.add_field(name="User:", value=f'{member.mention}', inline=True)
    embed.add_field(name="Reason:", value=f'{reason}', inline=True)
    embed.set_footer(text="Made by Celestial")
    await ctx.channel.send(embed=embed)


@client.command()
@has_permissions(ban_members=True)
async def unban(ctx, *, member):

    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = await member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title="Unbanned User")
            embed.add_field(
                name="User:", value=f'{member.mention}', inline=True)
            embed.set_footer(text="Made by Celestial")
            await ctx.channel.send(embed=embed)


async def load():
    async with client:
        await load_extensions()
        await client.start('NzkzMjc4MDA2Nzc2NjkyNzM4.GfvfNn.Q612ORARYiGO7K986QbhenqJdaPWI_r6beZssw')

print('CelestialDB is RUNNING WELL!')

asyncio.run(load())
