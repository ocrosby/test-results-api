import click
import uvicorn


@click.group()
def cli():
    """
    This is a command line interface for the test results FastAPI application.

    :return:
    """
    pass


@cli.command()
def run():
    """Start the Uvicorn server."""
    uvicorn.run("app.main:api", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    cli()
