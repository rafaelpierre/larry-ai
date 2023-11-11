import subprocess
import logging
import click
from typing import List

def run(command: List[str]):
    process = subprocess.Popen(
        command, 
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    while True:
        output = process.stdout.readline()
        print(output.strip())
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            for output in process.stdout.readlines():
                print(output.strip())
            break

@click.command()
@click.option('--logs', default='info', help='Verbosity level, defaults to INFO')
@click.option('--host', default='0.0.0.0', help='Host Address, defaults to 0.0.0.0')
@click.option('--port', default='8000', help='HTTP Port for Backend, defaults to 8000')
def main(logs: str, host: str, port: str):
    """Runs Larry Web App."""

    logging.basicConfig(level = logs.upper())
    logging.info("Starting Larry server...")

    run(["uvicorn", "larry.web:app", "--host", host, "--port", port])


if __name__ == "__main__":
    main()