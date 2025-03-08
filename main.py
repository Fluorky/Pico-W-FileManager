import glob
import logging
import subprocess
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def find_device():
    """Find the first available Pico W device"""
    devices = glob.glob('/dev/tty.usbmodem*')
    if devices:
        return devices[0]  # Return the first found device
    else:
        raise RuntimeError("No Pico W device found. Ensure it is connected.")


# Set port to dynamically found device
PICO_PORT = find_device()


def list_files(port=PICO_PORT):
    """List files on the Pico W"""
    try:
        result = subprocess.run(['ampy', '--port', port, 'ls'], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Files on Pico W:\n%s", result.stdout)
        else:
            logging.error("Error listing files: %s", result.stderr)
    except Exception as e:
        logging.error("Failed to list files: %s", e)


def upload_file(local_file, remote_file=None, port=PICO_PORT):
    """Upload a file to the Pico W"""
    if not remote_file:
        remote_file = local_file
    try:
        result = subprocess.run(['ampy', '--port', port, 'put', local_file, remote_file], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Successfully uploaded %s to Pico W as %s", local_file, remote_file)
        else:
            logging.error("Error uploading file: %s", result.stderr)
    except Exception as e:
        logging.error("Failed to upload file: %s", e)


def download_file(remote_file, local_file=None, port=PICO_PORT):
    """Download a file from the Pico W"""
    if not local_file:
        local_file = remote_file
    try:
        result = subprocess.run(['ampy', '--port', port, 'get', remote_file, local_file], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Successfully downloaded %s from Pico W as %s", remote_file, local_file)
        else:
            logging.error("Error downloading file: %s", result.stderr)
    except Exception as e:
        logging.error("Failed to download file: %s", e)


def remove_file(remote_file, port=PICO_PORT):
    """Remove a file from the Pico W"""
    try:
        result = subprocess.run(['ampy', '--port', port, 'rm', remote_file], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Successfully removed %s from Pico W", remote_file)
        else:
            logging.error("Error removing file: %s", result.stderr)
    except Exception as e:
        logging.error("Failed to remove file: %s", e)


def run_script(script, port=PICO_PORT):
    """Run a Python script on the Pico W"""
    try:
        result = subprocess.run(['ampy', '--port', port, 'run', script], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Successfully ran %s on Pico W", script)
            logging.info("Output:\n%s", result.stdout)
        else:
            logging.error("Error running script: %s", result.stderr)
    except Exception as e:
        logging.error("Failed to run script: %s", e)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Usage: python pico_manager.py <command> [arguments]")
        logging.info("Commands:")
        logging.info("  ls                       List files on Pico W")
        logging.info("  put <local> [remote]     Upload a file to Pico W")
        logging.info("  get <remote> [local]     Download a file from Pico W")
        logging.info("  rm <remote>              Remove a file from Pico W")
        logging.info("  run <script>             Run a Python script on Pico W")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "ls":
        list_files()
    elif command == "put" and len(sys.argv) >= 3:
        local_file = sys.argv[2]
        remote_file = sys.argv[3] if len(sys.argv) > 3 else None
        upload_file(local_file, remote_file)
    elif command == "get" and len(sys.argv) >= 3:
        remote_file = sys.argv[2]
        local_file = sys.argv[3] if len(sys.argv) > 3 else None
        download_file(remote_file, local_file)
    elif command == "rm" and len(sys.argv) >= 3:
        remote_file = sys.argv[2]
        remove_file(remote_file)
    elif command == "run" and len(sys.argv) >= 3:
        script = sys.argv[2]
        run_script(script)
    else:
        logging.error("Invalid command or missing arguments")
        logging.info("Commands:")
        logging.info("  ls                       List files on Pico W")
        logging.info("  put <local> [remote]      Upload a file to Pico W")
        logging.info("  get <remote> [local]      Download a file from Pico W")
        logging.info("  rm <remote>               Remove a file from Pico W")
        logging.info("  run <script>              Run a Python script on Pico W")
