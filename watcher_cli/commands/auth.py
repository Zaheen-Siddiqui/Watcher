import typer
from watcher_cli.services.api_client import APIClient
from watcher_cli.services.auth_service import save_token, clear_token

# Register the auth command group
app = typer.Typer(help="Authentication commands for Watcher CLI")

@app.command("login")
def Login():
    """
    Authentication command to log in to the Watcher service. This will prompt you for your username and password, and save the authentication token for future use."""
    username = typer.prompt("Username")
    password = typer.prompt("Password", hide_input=True)
    api_client = APIClient()
    try:
        token = api_client.authentication.Login(username, password)
        save_token(token)
        typer.echo("Login successful! Token saved.")
    except Exception as e:
        typer.echo(f"Login failed: {e}")

@app.command("logout")
def Logout():
    """
    Logout command to clear the saved authentication token. This will effectively log you out of the Watcher service.
    """
    clear_token()
    typer.echo("Logout successful! Token cleared.")

@app.command("register")
def Register():
    """
    Register command to create a new account on the Watcher service.
    This will prompt you for a username, email and password, and attempt to create a new account.
    """
    username = typer.prompt("Username")
    email = typer.prompt("Email")
    password = typer.prompt("Password", hide_input=True)
    api_client = APIClient()
    try:
        api_client.authentication.Register(username, email, password)
        typer.echo("Registration successful! You can now login with your new account.")
    except Exception as e:
        typer.echo(f"Registration failed: {e}")
