import random
import discord
import random, os
print(os.listdir("images"))
print(os.listdir("pemandangan"))
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "$", intents=intents)

@bot.event
async def on_ready():
    print(f"We have loggged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hi! im a bot {bot.user}! ")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(8))

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def pemandangan(ctx):
    img_name2 = random.choice(os.listdir("pemandangan"))
    with open(f'pemandangan/{img_name2}', "rb") as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)



bot.run("")
