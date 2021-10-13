import discord
from discord.ext import commands

bot = commands.Bot("%")

@bot.event
async def on_ready():
    print(f"I'm Ready now For Working, Connected by discord bot: {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "Fuck"  in message.content:

        await message.channel.send(f"Por Favor nao Diga este tipo de Coisa aqui")

        await message.delete()

    await bot.process_commands(message)

@bot.command(name= "nlw")
async def cmd(ctx):
    response = "vem ai NLW HEAT dia 17 fml vamo q vamo"
    
    await ctx.send(response)

bot.run("YOUR BOT TOKEN HERE")