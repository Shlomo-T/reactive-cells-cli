import click
from cli_app.app_manager import AppManager

app_manager = AppManager()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('file_path')
def init(file_path):
    """Set a new settable or computed value into the system"""
    with open(file_path) as f:
        file_data = f.read()
        values_list = file_data.split(',')
        app_manager.init_db(values_list)


@cli.command()
def current_state():
    """Present the current state of the system"""
    current_state = app_manager.current_status()
    click.echo(current_state)


@cli.command()
@click.argument('index', type=click.types.INT)
@click.argument('value')
def modify_value(index, value):
    """Set a new settable or computed value into the system"""
    app_manager.modify_record(index, value)


if __name__ == '__main__':
    cli()
