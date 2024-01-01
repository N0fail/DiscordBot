from discord.ext import commands
from discord import Intents
import os
from src.commands import add_commands
from src.events import add_events


def run():
    bot = commands.Bot(command_prefix='/', intents=Intents.all())
    add_events(bot)
    add_commands(bot)
    bot.run(os.getenv("DISCORD_TOKEN"))


if __name__ == '__main__':
    run()
