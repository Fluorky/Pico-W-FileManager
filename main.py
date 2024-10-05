import subprocess
import glob


def find_device():
    """Find the first available Pico W device."""
    devices = glob.glob('/dev/tty.usbmodem*')
    if devices:
        return devices[0]  # Return the first found device
    else:
        raise RuntimeError("No Pico W device found. Ensure it is connected.")


def list_files(port=None):
    """List files on the Pico W"""
    if port is None:
        port = find_device()  # Find the device if not specified
    try:
        result = subprocess.run(['ampy', '--port', port, 'ls'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Files on Pico W:")
            print(result.stdout)
        else:
            print("Error listing files:", result.stderr)
    except Exception as e:
        print(f"Failed to list files: {e}")


def upload_file(local_file, remote_file=None, port=None):
    """Upload a file to the Pico W"""
    if port is None:
        port = find_device()  # Find the device if not specified
    if not remote_file:
        remote_file = local_file
    try:
        result = subprocess.run(['ampy', '--port', port, 'put', local_file, remote_file], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully uploaded {local_file} to Pico W as {remote_file}")
        else:
            print("Error uploading file:", result.stderr)
    except Exception as e:
        print(f"Failed to upload file: {e}")

def download_file(remote_file, local_file=None, port=None):
    """Download a file from the Pico W"""
    if port is None:
        port = find_device()  # Find the device if not specified
    if not local_file:
        local_file = remote_file
    try:
        result = subprocess.run(['ampy', '--port', port, 'get', remote_file, local_file], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully downloaded {remote_file} from Pico W as {local_file}")
        else:
            print("Error downloading file:", result.stderr)
    except Exception as e:
        print(f"Failed to download file: {e}")

def remove_file(remote_file, port=None):
    """Remove a file from the Pico W"""
    if port is None:
        port = find_device()  # Find the device if not specified
    try:
        result = subprocess.run(['ampy', '--port', port, 'rm', remote_file], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully removed {remote_file} from Pico W")
        else:
            print("Error removing file:", result.stderr)
    except Exception as e:
        print(f"Failed to remove file: {e}")


def run_script(script, port=None):
    """Run a Python script on the Pico W"""
    if port is None:
        port = find_device()  # Find the device if not specified
    try:
        result = subprocess.run(['ampy', '--port', port, 'run', script], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully ran {script} on Pico W")
            print("Output:")
            print(result.stdout)
        else:
            print("Error running script:", result.stderr)
    except Exception as e:
        print(f"Failed to run script: {e}")
