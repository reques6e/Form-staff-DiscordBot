import nextcord
import os
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
                
@bot.event 
async def on_ready():
    print('client connected')

for fn in os.listdir("./cogs"):
	if fn.endswith(".py"):
		bot.load_extension(f"cogs.{fn[:-3]}")

@bot.command()
async def load(ctx, extension):
	bot.load_extension(extension)
	await ctx.send("Подключил cogs")


bot.run("MTE2OTk5OTcyODQ4NjkyNDMyOA.GltNuS.ORWmRIlp7VlxhAcbG_ED89RttcawX6uNHQC9rk")