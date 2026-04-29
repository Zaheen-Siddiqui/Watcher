import typer
from watcher_cli.commands import auth, packages, updates, email, import_export, help

app = typer.Typer(help="Watcher CLI - Dependency monitoring tool")

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Watcher CLI - Dependency maonitoring tool
    This CLI tool allows you to manage your dependencies, monitor for updates, and receive notifications about new releases. You can authenticate with your package manager, view and manage your packages, check for updates, and configure email notifications.
    """
    if ctx.involved_subcommand is None:
        typer.echo(ctx.get_help())

app = typer.Typer(auth.app, name="auth")
app.add_typer(auth.app, name="auth")
app.add_typer(packages.app, name="packages")
app.add_typer(updates.app, name="updates")
app.add_typer(email.app, name="email")
app.add_typer(import_export.app, name="import-export")


if __name__ == "__main__":
    app()

