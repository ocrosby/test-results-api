import click
import uvicorn

@click.group()
def cli():
    pass

@cli.command()
def start():
    """Start the Uvicorn server."""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    cli()
