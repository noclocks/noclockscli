"""Main module for the CLI."""

import click

from . import commands

@click.group()
def cli():
    """No Clocks CLI"""
    pass


cli.add_command(commands.hello)
cli.add_command(commands.add)
cli.add_command(commands.sub)
cli.add_command(commands.mul)
cli.add_command(commands.div)
