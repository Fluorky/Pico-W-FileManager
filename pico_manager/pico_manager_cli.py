import sys
import logging
from pico_manager.device import find_device
from pico_manager.file_operations import list_files, upload_file, download_file, remove_file
from pico_manager.script_runner import run_script
from pico_manager.utils import setup_logging

class PicoManagerCli:
    def __init__(self):
        setup_logging()
        try:
            self.port = find_device()
        except RuntimeError as e:
            logging.error(e)
            sys.exit(1)

    def run(self):
        logging.info("Starting Pico Manager")
        logging.info("Device connected on {}".format(self.port))

        if len(sys.argv) < 2:
            self.print_usage()
            sys.exit(1)

        command = sys.argv[1].lower()

        if command == "ls":
            list_files(self.port)
        elif command == "put" and len(sys.argv) >= 3:
            upload_file(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None, self.port)
        elif command == "get" and len(sys.argv) >= 3:
            download_file(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None, self.port)
        elif command == "rm" and len(sys.argv) >= 3:
            remove_file(sys.argv[2], self.port)
        elif command == "run" and len(sys.argv) >= 3:
            run_script(sys.argv[2], self.port)
        else:
            logging.error("Invalid command or missing arguments")
            self.print_usage()

    @staticmethod
    def print_usage():
        logging.info("Usage: python main.py <command> [arguments]")
        logging.info("Commands:")
        logging.info("  ls                        List files on Pico/Pico W")
        logging.info("  put <local> [remote]      Upload a file to Pico/Pico W")
        logging.info("  get <remote> [local]      Download a file from Pico/Pico W")
        logging.info("  rm <remote>               Remove a file from Pico/Pico W")
        logging.info("  run <script>              Run a Python script on Pico/Pivo W")
