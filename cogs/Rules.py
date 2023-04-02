import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class Rules(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    '''
    RULES
    '''

    @commands.command()
    async def rules1(self, ctx):
        embed = discord.Embed(title="Rules | Celestial",
                              description="Celestial is a development area designed for like minded people to join. We wish you follow the rules to the best of your ability.", color=0x0048ad)
        embed.set_footer(
            text="These rules are not set, and are subject to change if needed. These rules are made by vertis, if you have issues or suggestions contact him.")
        updateChannel = self.bot.get_channel(792972567870439454)
        await updateChannel.send(embed=embed)

    @commands.command()
    async def rules2(self, ctx):
        embed = discord.Embed(color=0x0048ad)
        embed.add_field(name="Section 1-Text Channels",
                        value="S1.A: Flooding/Spamming of a text channel will be strictly prohibited at all times. This will be met with a `mute/ban` depending on what is being spammed and for how long.", inline=False)
        embed.add_field(
            name="\u200b", value="S1.B: Advertising any other product/server/content will be `ban`, you are eligible to appeal.", inline=False)
        embed.add_field(
            name="\u200b", value="S1.C: Sharing links with malicious content will be met with a `permanent ban` with no appeal available.", inline=False)
        embed.add_field(
            name="\u200b", value="S1.D: Sharing NSFW content will be met with a `permanent ban` with no appeal available.", inline=False)
        embed.add_field(
            name="\u200b", value="S1.E: Any form of racist/hostile remarks will be subjected to a `mute/ban`.", inline=False)
        embed.add_field(
            name="\u200b", value="S1.F: Do not mention/ping Staff with no reason backing it. This will be subject to `mute/ban`.", inline=False)
        embed.add_field(
            name="\u200b", value="S1.G: Harassing members/staff of Celestial will be met with a `ban`, you are eligible to appeal.", inline=False)
        embed.add_field(
            name="\u200b", value="S1.H: Attempting to bypass filters in the text channels will be met with a `mute/ban` depending on the severity.", inline=False)
        updateChannel = self.bot.get_channel(792972567870439454)
        await updateChannel.send(embed=embed)

    @commands.command()
    async def rules3(self, ctx):
        embed = discord.Embed(color=0x0048ad)
        embed.add_field(name="Section 2-Voice Channels",
                        value="S2.A: Spamming of the voice call will always be prohibited and will be a `mute/ban` depending on severity", inline=False)
        embed.add_field(
            name="\u200b", value="S2.B: Repeatedly joining and leaving a voice channel results with your permissions of joining the voice chat revoked and `muted`.", inline=False)
        embed.add_field(name="\u200b", value="S2.C: Skipping other people's songs to be annoying or playing long videos on the bot will result with your permissions of joining the voice chat revoked and `muted`.", inline=False)
        embed.add_field(
            name="\u200b", value="S2.D: Any form of racism will be a `mute/ban` depending on what has been said.", inline=False)
        updateChannel = self.bot.get_channel(792972567870439454)
        await updateChannel.send(embed=embed)

    @commands.command()
    async def rules4(self, ctx):
        embed = discord.Embed(color=0x0048ad)
        embed.add_field(name="Section 3-General", value="S3.A: People with other roles other than what the majority has are not exempt from the rules. If anyone is seen breaking a rule, please inform the Staff.", inline=False)
        embed.add_field(name="\u200b", value="S3.B: Punishments are left for the Staff issuing them. You can be given a warning depending on the Staff members leniency of the matter. If you believe that there was a mistake or you were unfairly punished, contact an Admin.", inline=False)
        embed.add_field(
            name="\u200b", value="S3.C: Instigating/Replying to a rule-breaking content will result in the same punishment from the person who shared it.", inline=False)
        embed.add_field(
            name="\u200b", value="S3.D: Attempting to bypass/undermine the rules in any way will be met with a `mute/ban` depending on the severity", inline=False)
        updateChannel = self.bot.get_channel(792972567870439454)
        await updateChannel.send(embed=embed)

    @commands.command()
    async def rules5(self, ctx):
        embed = discord.Embed(color=0x0048ad)
        embed.add_field(name="Section 4-Staff",
                        value="S4.A: Administrators/Owners have absolute authority over punishments, even if not stated in the rules.", inline=False)
        embed.add_field(
            name="\u200b", value="S4.B: If you think there is a mistake with your ruling, talk to Admin/Owner", inline=False)
        embed.add_field(name="\u200b", value="S4.C: By using all of the channels and using this server/being here, you acknowledge all the rules and wish to follow them. All rules here are subject to change as time goes on.", inline=False)
        embed.add_field(name="\u200b", value="S4.D: If an Admin/Mod is abusing his/her power, please contact the Owner with legitimate proof, such as messages. (Screenshare and videos are only valid)", inline=False)
        updateChannel = self.bot.get_channel(792972567870439454)
        await updateChannel.send(embed=embed)


async def setup(client):
    await client.add_cog(Rules(client))
