import click
import subprocess

@click.group()
def main():
    pass

@main.command()
@click.argument('fleet_size', type=int)
def allocate_route(fleet_size):
    """Allocate and route vehicles for the specified fleet size."""
    click.echo(f"Allocating and routing vehicles for fleet size: {fleet_size}")
    
    # Call the Action Client CLI to perform the task
    subprocess.call(['ros2', 'run', 'fleet_management_py', 'fleet_management_client_cli.py', str(fleet_size)])

if __name__ == '__main__':
    main()

