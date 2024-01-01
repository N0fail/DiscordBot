from discord.ext import commands
from discord import Intents
import discord
import os
from commands import add_commands
from events import add_events


def run():
    bot = commands.Bot(command_prefix='/', intents=Intents.all())
    add_events(bot)
    add_commands(bot)
    bot.run(os.getenv("DISCORD_TOKEN"))


if __name__ == '__main__':
    if not discord.opus.is_loaded():
        discord.opus.load_opus(os.getenv("LIBOPUS_PATH"))
    run()
