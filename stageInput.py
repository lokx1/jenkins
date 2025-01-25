import os
import sys
import subprocess

import shutil


def flush_print(message):
    """
    Print a message and immediately flush the output to ensure visibility.
    """
    print(message)
    sys.stdout.flush()

def check_c_files(input_folder, checked_folder):
    """
    Check if the folder contains .c files and validate their syntax.
    If valid, copy the file to the 'input_checked' folder.
    """
    if not os.path.exists(input_folder):
        flush_print(f"Folder '{input_folder}' does not exist.")
        sys.exit(1)

    if not os.path.exists(checked_folder):
        os.makedirs(checked_folder)

    # Find all .c files in the input folder
    c_files = [f for f in os.listdir(input_folder) if f.endswith(".c")]
    if not c_files:
        flush_print(f"No .c files found in '{input_folder}'.")
        sys.exit(1)

    flush_print(f"Found {len(c_files)} .c file(s) in '{input_folder}':")
    for c_file in c_files:
        file_path = os.path.join(input_folder, c_file)
        flush_print(f" - Checking syntax for: {c_file}")
        if check_syntax(file_path):
            copy_to_checked_folder(file_path, checked_folder)

def check_syntax(c_file):
    """
    Perform syntax validation on a .c file using GCC.
    Returns True if the syntax is valid, False otherwise.
    """
    try:
        result = subprocess.run(
            ['gcc', '-fsyntax-only', c_file],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            flush_print(f"Syntax check passed for '{c_file}'.")
            return True
        else:
            flush_print(f"Syntax check failed for '{c_file}':\n{result.stderr}")
            return False
    except FileNotFoundError:
        flush_print("GCC is not installed or not available in PATH.")
        sys.exit(1)
    except Exception as e:
        flush_print(f"An error occurred while checking '{c_file}': {e}")
        sys.exit(1)

def copy_to_checked_folder(c_file, checked_folder):
    """
    Copy the file with valid syntax to the 'input_checked' folder.
    """
    try:
        destination = os.path.join(checked_folder, os.path.basename(c_file))
        shutil.copy(c_file, destination)
        flush_print(f"File '{c_file}' copied to '{checked_folder}'.")
    except Exception as e:
        flush_print(f"Failed to copy file '{c_file}': {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        flush_print("Usage: python3 <script_name.py> <input_folder> <checked_folder>")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    checked_folder = sys.argv[2]
    check_c_files(input_folder, checked_folder)