import typer
from watcher_cli.services.api_client import APIClient
from watcher_cli.services.formatter import print_table

app = typer.Typer(help="Commands to check for updates on monitored packages in Watcher CLI")


@app.command("check")
def CheckUpdates():
    """
    Check for latest versions for all monitored packages.
    This will retrieve the list of the monitored packages and their latest versions in a table format.
    """
    api_client = APIClient()
    try:
        updates = api_client.updates.CheckUpdates()
        if not updates:
            typer.echo("No updates found for monitored packages.")
            return
        print_table(updates, headers=["Package Name", "Current Version", "Latest Version", "Release Date"])
    except Exception as e:
        typer.echo(f"Failed to check for updates: {e}")

@app.command("updates")
def Updates():
    """
    Command to check for all the updates since the last login.
    This will retrieve the list of all updates that have been released for the monitored packages since the last time you logged in, and display them in a table format.
    """
    api_client = APIClient()
    try:
        updates = api_client.updates.Updates()
        if not updates:
            typer.echo("No new updates found since last login.")
            return
        print_table(updates, headers=["Package Name", "Current Version", "Latest Version", "Release Date"])
    except Exception as e:
        typer.echo(f"Failed to check for updates: {e}")

