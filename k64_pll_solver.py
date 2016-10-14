#!/usr/bin/env python
import click
from pll_solver import PLLSolver

__VERSION__ = "0.0.1"
@click.command()
@click.option("--freq_in", '-i', help="Input frequency value in Hz", type=int)
@click.option("--freq_out", '-o', help="Output frequency value in Hz", type=int)
@click.version_option(__VERSION__)
def cli(freq_in, freq_out):
    """
    Simple program which takes an input frequency and an output frequency and
    returns the pdiv and vdiv necissary for the pll in the freescale k64 processors
    """

    if (not freq_in or not freq_out):
        return

    solver = PLLSolver()
    click.echo(solver.solve(freq_in, freq_out))
    click.echo("wow")
if __name__ == "__main__":
    cli()
