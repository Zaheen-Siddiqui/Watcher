import typer
from watcher_cli.services.api_client import APIClient 

# Register the packages command group
app = typer.Typer(help="Package management command for Watcher cli")

@app.command("list")
def ListPackages():
    """
    List all the packages that are being monitored by Watcher
    """
    api_client = APIClient()
    try:
        packages = api_client.packages.ListPackages()
        if not packages:
            typer.echo("No packages found.")
            return
        typer.echo("Monitored Packages:")
        for package in packages:
            typer.echo(f"- {package['name']} (version: {package['version']})")
    except Exception as e:
        typer.echo(f"Failed to retrieve packages: {e}")

@app.command("add")
def AddPackages():
    """
    Add a new package to be monitored by Watcher. 
    This will prompt you for the package name and version, and add it to the list of monitored packages.
    """
    name = typer.prompt("Package Name")
    version = typer.prompt("Package Version")
    api_client = APIClient()
    try:
        api_client.packages.AddPackage(name, version)
        typer.echo(f"Packages '{name} (version {version})' added successfully!")
    except Exception as e:
        typer.echo(f"Failed to add package: {e}")

@app.command("remove")
def RemovePackage():
    """
    Removes a package from being monitored by WWatcher
    This will prompt you for the package name, and remove it from the list of monitored packages.
    """
    name =typer.prompt("Package Name")
    api_client= APIClient()
    try:
        api_client.packages.RemovePackage(name)
        typer.echo(f"Package {name} removed successfully!")
    except Exception as e:
        typer.echo(f"Failed to remove package: {e}") 

