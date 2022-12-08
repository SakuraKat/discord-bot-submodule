# ------------------------------------------------------------------------------
#      Copyright (c) 2022                                                      -
#      - Katheryn Sakura (pseudonym)                                           -
#      - https://github.com/SakuraKat                                          -
#                                                                              -
#      This program is free software: you can redistribute it and/or modify    -
#      it under the terms of the GNU General Public License as published by    -
#      the Free Software Foundation, either version 3 of the License, or       -
#      (at your option) any later version.                                     -
#                                                                              -
#      This program is distributed in the hope that it will be useful,         -
#      but WITHOUT ANY WARRANTY; without even the implied warranty of          -
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           -
#      GNU General Public License for more details.                            -
#                                                                              -
#      You should have received a copy of the GNU General Public License       -
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.  -
#                                                                              -
#      Long Description:                                                       -
#                                                                              -
#                                                                              -
# ------------------------------------------------------------------------------

import random

from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks


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
    # This will only allow owners of the bot to execute the command -> config.json
    # @checks.is_owner()
    async def random_bs(self, context: Context):
        """
        The command that prints out random bullshit from the dataset
        :param context: The application command context
        """
        # Do your stuff here
        # Pick a random line from combined.txt and assign it to a variable called bs
        # the file is located in data/combined.txt
        # the file contents are in utf-8 encoding
        # the file contains one bullshit per line
        # file path from root directory: data/combined.txt
        # current file path: discord-bot-submodule\cogs\custom.py
        # relative file path: ../data/combined.txt
        bs = random.SystemRandom().choice(
            open("../data/combined.txt", encoding="utf-8").readlines()).replace("___", "#")
        # Send the bullshit to the channel
        await context.send(bs)


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(CustomCommands(bot))
