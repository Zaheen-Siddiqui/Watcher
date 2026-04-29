import typer
from watcher_cli.services.api_client import APIClient
# An email will be sent when enabling/disabling email notifications, it will wait for confirmation response from the user via email this will ensure wether the emails are being sent properly or not, and also confirm the user's email address. If the user does not receive the email or does not confirm, they can try enabling/disabling email notifications again or check their email settings.
app = typer.Typer(help="Commands to enable/ disable email notifications for Watcher CLI")

@app.command("email_on")
def EmailOn():
    """
    Command to enable email notification for new updates on monitored packages.
    This will enable email notifications for new updates on monitored packages. You will receive an email notification whenever a new update is released for any of the monitored packages.
    """
    api_client = APIClient()
    try:
        api_client.email.EmailOn()
        typer.echo("Email notification enabled successfully!")
    except Exception as e:
        typer.echo(f"Failed to enable email notification: {e}")

@app.command("email_off")
def EmailOff():
    """
    Command to disable email notification for new updates on monitored packages.
    This will disable email notifications for new updates on monitored packages. You will not receive an email notification whenever a new update is released for any of the monitored packages.
    """
    api_client = APIClient()
    try:
        api_client.email.EmailOff()
        typer.echo("Email notification disabled successfully!")
    except Exception as e:
        typer.echo(f"Failed to disable email notification: {e}")

