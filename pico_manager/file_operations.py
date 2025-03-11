import subprocess
import logging

def list_files(port):
    """List files on the Pico W."""
    try:
        result = subprocess.run(['ampy', '--port', port, 'ls'], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Files on Pico W:\n%s", result.stdout)
        else:
            logging.error("Error listing files: %s", result.stderr)
    except Exception as e:
        logging.error("Failed to list files: %s", e)

def upload_file(local_file, remote_file=None, port=None):
    """Upload a file to the Pico W."""
    remote_file = remote_file or local_file
    try:
        result = subprocess.run(['ampy', '--port', port, 'put', local_file, remote_file], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Uploaded %s to Pico W as %s", local_file, remote_file)
        else:
            logging.error("Upload error: %s", result.stderr)
    except Exception as e:
        logging.error("Failed to upload file: %s", e)

def download_file(remote_file, local_file=None, port=None):
    """Download a file from the Pico W."""
    local_file = local_file or remote_file
    try:
        result = subprocess.run(['ampy', '--port', port, 'get', remote_file, local_file], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Downloaded %s from Pico W as %s", remote_file, local_file)
        else:
            logging.error("Download error: %s", result.stderr)
    except Exception as e:
        logging.error("Failed to download file: %s", e)

def remove_file(remote_file, port=None):
    """Remove a file from the Pico W."""
    try:
        result = subprocess.run(['ampy', '--port', port, 'rm', remote_file], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info("Removed %s from Pico W", remote_file)
        else:
            logging.error("Error removing file: %s", result.stderr)
    except Exception as e:
        logging.error("Failed to remove file: %s", e)
