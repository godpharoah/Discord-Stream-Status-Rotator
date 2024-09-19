import asyncio
import random
import discord
from discord.ext import commands

token = ''
bot = commands.Bot(command_prefix='.', self_bot=True)

statuses: list[str] = [
    "by pharoah",
    "test",
    "test2"
]

@bot.event
async def on_ready() -> None:
    print("Bot is ready.")
    await update_status()

async def update_status() -> None:
    while True:
        status: str = random.choice(statuses)
        print(f"Setting random stream status to: {status}")
        await bot.change_presence(
            status=discord.Status.idle,
            activity=discord.Streaming(
                name=status,
                url="https://twitch.tv/your_channel"
            )
        )
        await asyncio.sleep(3)

if __name__ == "__main__":
    print("Starting the bot...")
    bot.run(token, bot=False, reconnect=True)
