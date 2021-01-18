from discord.ext import commands

from cogs.libs.board import init_board

from cogs.libs.moves import legal_moves

from cogs.libs.move import push_san

from cogs.libs.state import checkmate
from cogs.libs.state import stalemate
from cogs.libs.state import insufficient_material
from cogs.libs.state import game_over
from cogs.libs.state import draw

from cogs.libs.repetitions import threefold_repetition
from cogs.libs.repetitions import halfmove_clock
from cogs.libs.repetitions import fifty_moves


class Chess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def board(self, ctx):
        await ctx.send(init_board())

    @commands.command()
    async def moves(self, ctx):
        await ctx.send(legal_moves())

    @commands.command()
    async def move(self, ctx, move):
        await ctx.send(push_san(move))

    @commands.command()
    async def checkmate(self, ctx):
        await ctx.send(checkmate())

    @commands.command()
    async def stalemate(self, ctx):
        await ctx.send(stalemate())

    @commands.command()
    async def insufficient_material(self, ctx):
        await ctx.send(insufficient_material())

    @commands.command()
    async def game_over(self, ctx):
        await ctx.send(game_over())

    @commands.command()
    async def draw(self, ctx):
        await ctx.send(draw())

    @commands.command()
    async def threefold_repetition(self, ctx):
        await ctx.send(threefold_repetition())

    @commands.command()
    async def halfmove_clock(self, ctx):
        await ctx.send(halfmove_clock())

    @commands.command()
    async def fifty_moves(self, ctx):
        await ctx.send(fifty_moves())


def setup(bot):
    bot.add_cog(Chess(bot))
