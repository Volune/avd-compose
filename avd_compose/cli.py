import os

import click


DEFAULT_CONFIG_FILE = os.getenv("AVD_COMPOSE_CONFIG_FILE", "avd-compose.yml")


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.option("-c", "--config-file", default=DEFAULT_CONFIG_FILE)
@click.pass_context
def main(ctx, debug, config_file):
    ctx.ensure_object(dict)

    ctx.obj["DEBUG"] = debug
    ctx.obj["CONFIG_FILE"] = config_file


@main.command()
@click.pass_context
def version(ctx):
    """ prints the avd-compose, avdmanager, sdkmanager, emulator versions """
    pass


@main.command()
@click.pass_context
@click.option(
    "-n", "--name", default=None, type=str, help="specific android virtual device name"
)
def create(ctx, name):
    """ creates android virtual devices """
    pass


@main.command()
@click.pass_context
@click.option(
    "-n", "--name", default=None, type=str, help="specific android virtual device name"
)
def up(ctx, name):
    """ starts the avd-compose environment """
    pass


@main.command()
@click.pass_context
def status(ctx):
    """ status of the android virtual devices in the configuration file """
    pass


@main.command()
@click.pass_context
@click.option(
    "-n", "--name", default=None, type=str, help="specific android virtual device name"
)
def destroy(ctx, name):
    """ deletes all the android virtual devices """
    pass


if __name__ == "__main__":
    main(obj={})
