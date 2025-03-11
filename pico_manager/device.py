import glob
import logging

def find_device():
    """Find the first available Pico W device."""
    devices = glob.glob('/dev/tty.usbmodem*')
    if devices:
        return devices[0]
    else:
        logging.error("No Pico W device found. Ensure it is connected.")
        raise RuntimeError("No Pico W device found.")
