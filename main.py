import subprocess
import sys

# Set port to /dev/tty.usbmodem14201
PICO_PORT = '/dev/tty.usbmodem14101'


def list_files(port=PICO_PORT):
    """List files on the Pico W"""
    try:
        result = subprocess.run(['ampy', '--port', port, 'ls'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Files on Pico W:")
            print(result.stdout)
        else:
            print("Error listing files:", result.stderr)
    except Exception as e:
        print(f"Failed to list files: {e}")


def upload_file(local_file, remote_file=None, port=PICO_PORT):
    """Upload a file to the Pico W"""
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


def download_file(remote_file, local_file=None, port=PICO_PORT):
    """Download a file from the Pico W"""
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


def remove_file(remote_file, port=PICO_PORT):
    """Remove a file from the Pico W"""
    try:
        result = subprocess.run(['ampy', '--port', port, 'rm', remote_file], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully removed {remote_file} from Pico W")
        else:
            print("Error removing file:", result.stderr)
    except Exception as e:
        print(f"Failed to remove file: {e}")


def run_script(script, port=PICO_PORT):
    """Run a Python script on the Pico W"""
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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pico_manager.py <command> [arguments]")
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
        print("Invalid command or missing arguments")
        print("Commands:")
        print("  ls                       List files on Pico W")
        print("  put <local> [remote]      Upload a file to Pico W")
        print("  get <remote> [local]      Download a file from Pico W")
        print("  rm <remote>               Remove a file from Pico W")
        print("  run <script>              Run a Python script on Pico W")
