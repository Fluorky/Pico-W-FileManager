# **Pico W File Manager**

A command-line tool to manage files on the **Raspberry Pi Pico W** using the `ampy` tool. It allows users to **list, upload, download, remove files**, and **run Python scripts** directly on the Pico W.

## **Table of Contents**
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## **Features**
- Automatically detects a connected **Pico W**  
- List files on the device  
- Upload files to the Pico W  
- Download files from the Pico W  
- Remove files from the Pico W  
- Run Python scripts on the Pico W  

## **Requirements**
Before using this tool, ensure you have the following installed:

- **Python 3.11 or higher**
- [`ampy`](https://github.com/scientifichackers/ampy) – A command-line tool for interacting with MicroPython boards.

## **Installation**
Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/Pico-W-FileManager.git
cd Pico-W-FileManager
pip install -r requirements.txt
```

## **Usage**
Run the script using the command-line interface:

```bash
python main.py <command> [arguments]
```

### **Available Commands:**
- **List files on Pico W**  
  ```bash
  python main.py ls
  ```
- **Upload a file to Pico W**  
  ```bash
  python main.py put <local_file> [remote_file]
  ```
  Example:
  ```bash
  python main.py put example.py
  ```
- **Download a file from Pico W**  
  ```bash
  python main.py get <remote_file> [local_file]
  ```
  Example:
  ```bash
  python main.py get example.py
  ```
- **Remove a file from Pico W**  
  ```bash
  python main.py rm <remote_file>
  ```
  Example:
  ```bash
  python main.py rm example.py
  ```
- **Run a Python script on Pico W**  
  ```bash
  python main.py run <script.py>
  ```
  Example:
  ```bash
  python main.py run example.py
  ```
