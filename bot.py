import discord, json, pyfiglet, random, string, asyncio, json, time
from pyfiglet import Figlet
from discord.ext import commands
from random import randint
from time import sleep

bot = commands.Bot(description="Nitro Gen Bot", command_prefix="f!")
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user} IS ONLINE!!! WOOO')
    await bot.change_presence(activity=discord.Game(name="Generating..."))

@bot.command()
async def ascii(ctx, *, args):
    text = pyfiglet.figlet_format(args)
    await ctx.send(f'```{text}```')

@bot.command()
async def invite(ctx):
    await ctx.send(f'https://discord.gg/KXtpN9hNrb')

@bot.command()
async def help(ctx):
    embedVar = discord.Embed(title="Help", description="Prefix: f!", color=0xd5ffff)
    embedVar.add_field(name="help", value="Sends this help embed.", inline=True)
    embedVar.add_field(name="nitro", value="Generates a nitro gift code.", inline=True)
    embedVar.add_field(name="xbox", value="Generates a xbox gamepass code.", inline=True)
    embedVar.add_field(name="steam", value="Generates a steam gift code.", inline=True)
    embedVar.add_field(name="invite", value="Gives you a invite link to join this server.", inline=True)
    embedVar.set_footer(text="Made by Finnutz and Ntdi")
    await ctx.channel.send(embed=embedVar)

@bot.command()
@commands.cooldown(1.0, 60.0, commands.BucketType.guild)
async def steam(ctx):
    await ctx.message.delete()
    stemcod = ('').join(random.choices(string.ascii_uppercase + string.digits, k=5)) + "-" + ('').join(random.choices(string.ascii_uppercase + string.digits, k=5)) + "-" + ('').join(random.choices(string.ascii_uppercase + string.digits, k=5))
    await ctx.author.send(f'{stemcod}')
@steam.error
async def steam_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.message.delete()
        username = ctx.message.author.id
        msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(f'{msg}, <@{username}>')
    else:
        raise error 

@bot.command()
@commands.cooldown(1.0, 60.0, commands.BucketType.guild)
async def xbox(ctx):
    await ctx.message.delete()
    gamepass = ('').join(random.choices(string.ascii_uppercase + string.digits, k=4)) + "-" + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + "-" + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + "-" + ('').join(random.choices(string.ascii_letters + string.digits, k=4))
    await ctx.author.send(f'{gamepass}')
@xbox.error
async def xbox_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.message.delete()
        username = ctx.message.author.id
        msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(f'{msg}, <@{username}>')
    else:
        raise error

@bot.command()
@commands.cooldown(1.0, 60.0, commands.BucketType.guild)
async def nitro(ctx):
    await ctx.message.delete()
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    await ctx.author.send(f'{code}')

@nitro.error
async def nitro_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.message.delete()
        username = ctx.message.author.id
        msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(f'{msg}, <@{username}>')
    else:
        raise error



with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')
bot.run(token, bot=True)