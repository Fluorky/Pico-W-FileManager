import subprocess
import logging

def run_script(script, port=None):
    """Run a Python script on the Pico W."""
    try:
        result = subprocess.run(['ampy', '--port', port, 'run', script], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Successfully ran %s on Pico W", script)
            logging.info("Output:\n%s", result.stdout)
        else:
            logging.error("Error running script: %s", result.stderr)
    except Exception as e:
        logging.error("Failed to run script: %s", e)
