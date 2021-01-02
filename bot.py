import discord
from discord.ext import commands
import random
import numpy as np
import config

client = commands.Bot(command_prefix="+")

f = open("rules.txt", "r")
help_file = open("helps.txt", "r")
helps = help_file.readlines()
rules = f.readlines()


@client.event
async def on_ready():
    print("Les go........")


@client.command(aliases=['h'])
async def hep(ctx):
    for i in range(0, 10):
        await ctx.send(helps[i])


@client.command(aliases=['r'])
async def rule(ctx, *, number):
    await ctx.send(rules[int(number) - 1])


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)


@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason='Do we really need any reason...'):
    await ctx.send(member.name + " has been kicked from My sever, because: " + reason)
    await member.kick(reason=reason)


@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason='Do we really need any reason'):
    await ctx.send(member.name + " has been banned from My sever, because: " + reason)
    await member.ban(reason=reason)


@client.command(aliases=['mr'])
async def memerate(ctx):
    percentage = (random.randint(0, 100))
    if percentage == 50:
        say_ = 'not bad'
        embed_color = discord.Color.black()
    elif percentage > 50:
        say_ = 'nice quality meme'
        embed_color = discord.Color.red()
    else:
        say_ = 'Disappointed, but not surprised'
        embed_color = discord.Color.green()

    embed = discord.Embed(title="Meme Rate", colour=embed_color)
    embed.add_field(name=f"Your Meme rating: {percentage}", value=say_)
    await ctx.send(embed=embed)


@client.command(aliases=['pr'])
async def penisrate(ctx):
    percentage = (random.randint(0, 100))
    if percentage == 50:
        say_ = 'Average'
        embed_color = discord.Color.black()
    elif percentage > 50:
        say_ = 'mmhmmm'
        embed_color = discord.Color.red()
    else:
        say_ = 'Do not feel sad King'
        embed_color = discord.Color.green()

    embed = discord.Embed(title="Penis Rate", colour=embed_color)
    embed.add_field(name=f"Your Penis rating: {percentage}", value=say_)
    await ctx.send(embed=embed)


@client.command(aliases=['sr'])
async def simprate(ctx):
    percentage = (random.randint(0, 100))
    if percentage == 50:
        say_ = '50% simp not bad'
        embed_color = discord.Color.black()
    elif percentage > 50:
        say_ = 'supa simp'
        embed_color = discord.Color.red()
    else:
        say_ = 'Try again, I bet it will be supa simp'
        embed_color = discord.Color.green()

    embed = discord.Embed(title="simp Rate", colour=embed_color)
    embed.add_field(name=f"Your simp rating: {percentage}", value=say_)
    await ctx.send(embed=embed)


client.run(config.TOKEN)
print("")
