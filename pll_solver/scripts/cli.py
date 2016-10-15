#!/usr/bin/env python
import click
from ..version import __VERSION__
from pll_solver import PLLSolver
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

def get_verbosity_level(verbosity):
    return max(logging.CRITICAL - (verbosity * 10), 0)

@click.command()
@click.option("--freq_in", '-i', help="Input frequency value in Hz", type=float)
@click.option("--freq_out", '-o', help="Output frequency value in Hz", type=float)
@click.option("--verbosity", '-v', help="Verbosity of output", count=True)
@click.version_option(__VERSION__)
@click.pass_context
def cli(ctx, freq_in, freq_out, verbosity):
    """
    Simple program which takes an input frequency and an output frequency and
    returns the pdiv and vdiv necissary for the pll in the freescale k64 processors
    """
    logger.setLevel(get_verbosity_level(verbosity))

    if (not freq_in or not freq_out):
        click.echo(ctx.get_help())
        return

    freq_in = int(freq_in)
    freq_out = int(freq_out)

    solver = PLLSolver()

    try:
        click.echo(solver.solve(freq_in, freq_out))
    except Exception as e:
        logger.debug(e)
        click.echo("No results found.")
        return 1
