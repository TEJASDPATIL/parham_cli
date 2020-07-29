import click
import subprocess

@click.command()
def start():
    a = subprocess.run("service postgresql-12 start",shell=True)
    click.echo(a)
@click.command()
def status():
    a = subprocess.run("service postgresql-12 status",shell=True)
    click.echo(a)
@click.command()
def stop():
    a = subprocess.run("service postgresql-12 stop",shell=True)
    click.echo(a)
