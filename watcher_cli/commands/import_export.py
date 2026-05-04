import typer
import json
from pathlib import Path
from watcher_cli.sevices.api_client import APIClient

app = typer.Typer(help="Commands for import and export of monitored packages.")

@app.command("export")
def export_packages(file: Path):
    """
    Command to export the list of monitored packages to a JSON file.
    This file will be in JSON format.
    """
    api_client = APIClient()
    try:
        packages = api_client.packages.GetMonitoredPackages()
        with open(file, 'w') as f:
            json.dump(packages, f, indent=4)
        typer.echo(f"Monitored packages exported successfully to {file}")
    except Exception as e:
        typer.echo(f"Failed to export monitored packages: {e}")

@app.command("import")
def import_packages(file: Path):
    """
    Command to import monitored packages from a JSON file.
    This file should be in JSON format.
    """
    api_client = APIClient()
    try:
        with open(file, 'r') as f:
            packages = json.load(f)
        for package in packages:
            api_client.packages.AddMonitoredPackage(package)
        typer.echo(f"Monitored packages imported successfully from {file}")
    except Exception as e:
        typer.echo(f"Failed to import monitored packages: {e}")