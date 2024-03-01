import click

@click.command(help="Prints 'Hello, World!'")
@click.version_option("0.1.0", prog_name="noclockscli")
def hello():
    """Hello World"""
    click.echo("Hello, World!")


@click.command(help="Add two numbers.")
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def add(a, b):
    click.echo(a + b)


@click.command(help="Subtract two numbers.")
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def sub(a, b):
    click.echo(a - b)


@click.command(help="Multiply two numbers.")
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def mul(a, b):
    click.echo(a * b)


@click.command(help="Divide two numbers.")
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def div(a, b):
    click.echo(a / b)
