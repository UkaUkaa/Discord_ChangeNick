import sys

import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix='<><><>')

@Bot.event
async def on_ready():
    oldName = Bot.user.name
    await Bot.user.edit(password = sys.argv[2], username = sys.argv[3])
    sys.exit(f'Old name = {oldName} |   New name = {sys.argv[3]}')

Bot.run(sys.argv[1])