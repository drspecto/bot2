import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
THREAD_ID = int(os.getenv("THREAD_ID"))
ROLE_ID = os.getenv("ROLE_ID")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(THREAD_ID)
    if channel:
        role_mention = f"<@&{ROLE_ID}>" if ROLE_ID else ""
        message = f"{role_mention} 🔔 **Reminder:** Please send your *Login and Logout* updates in this chat ✅"
        await channel.send(message)
    await bot.close()

bot.run(TOKEN)
