""""
Copyright © Krypton 2022 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
This is a template to create your own discord bot in python.

Version: 5.3
"""

import random

from discord.ext import commands
from discord.ext.commands import Context

from data.helpers import checks


class CustomCommands(commands.Cog, name="custom"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="random_bs",
        description="Prints out random bullshit from the dataset.",
    )
    # This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    # This will only allow owners of the bot to execute the command -> example-config.json
    # @checks.is_owner()
    async def random_bs(self, context: Context):
        """
        The command that prints out random bullshit from the dataset.

        :param context: The application command context.
        """
        # Do your stuff here
        # Pick a random line from combined.txt and assign it to a variable called bs
        # the file is located in data/combined.txt
        # the file contents are in utf-8 encoding
        # the file contains one bullshit per line
        bs = random.choice(open("data/combined.txt", encoding="utf-8").readlines()).replace("___", "#")
        # Send the bullshit to the channel
        await context.send(bs)


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(CustomCommands(bot))
