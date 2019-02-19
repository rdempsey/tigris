import logging
import json_logging
import click
import subprocess


# Logging
json_logging.ENABLE_JSON_LOGGING = True
json_logging.init()
logger = logging.getLogger(name="tigris-logger")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler(filename='tigris.log'))


def log(message, log_extras={}):
    """
    Create a log in json format.

    :param message: message to log
    :param log_extras: dict of arbitrary length to add to the log
    """
    logger.info(message, extra={'props': log_extras})


@click.group()
@click.version_option(version='0.1.0', prog_name='Tigris')
def cli():
    pass


@click.command(name='create', help='Create a new Anaconda project with a default set of libraries.')
@click.argument('new', nargs=1)
@click.argument('env_type', nargs=1)
@click.argument('conda', nargs=1)
@click.option('-n', '--name', help='Name of the project', required=True, type=str)
@click.option('-p', '--python', help='Python version', default='3.7', required=True, type=float, show_default=True)
def create(new, env_type, conda, name, python):
    """
    Create a new <basic|data|web> Anaconda environment with a default set of packages.

    Usage: create new <basic|data> conda env --name my_env --python 3.7
    """
    base_packages = ['ptpython', 'jupyter', 'pytest', 'pytest-cov', 'pytest-benchmark']

    if env_type == 'basic':
        packages = base_packages
    elif env_type == 'data':
        packages = base_packages + ['cython', 'numpy', 'scipy', 'pandas']
    elif env_type == 'web':
        packages = base_packages + ['Flask', 'Flask-SQLAlchemy', 'Flask-Testing', 'SQLAlchemy', 'gunicorn']

    command = f"conda create -y -q -n {name} python={python}"

    for package in packages:
        command += f" {package}"

    message = f"Creating a {new} {env_type} conda env called {name} with python {python}"
    log(message)
    click.echo(message)

    subprocess.run(command, shell=True, check=True)
    subprocess.run(f"/anaconda3/envs/{name}/bin/pip install jupyter_contrib_nbextensions")

    message = f"Conda env {name} created"
    log(message)
    click.echo(message)

    message = f"Activate your new anaconda environment when ready: `source activate {name}`"
    log(message)
    click.echo(message)



cli.add_command(create)
