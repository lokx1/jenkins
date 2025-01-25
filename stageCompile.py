import os
import sys
import subprocess

def flush_print(message):
    """
    Print a message and immediately flush the output to ensure visibility.
    """
    print(message)
    sys.stdout.flush()

def compile_c_files(input_folder, output_folder):
    """
    Compile .c files in the input_folder into .o files and save them to output_folder.
    """
    if not os.path.exists(input_folder):
        flush_print(f"Input folder '{input_folder}' does not exist.")
        sys.exit(1)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Find all .c files in the input folder
    c_files = [f for f in os.listdir(input_folder) if f.endswith(".c")]
    if not c_files:
        flush_print(f"No .c files found in '{input_folder}'.")
        sys.exit(1)

    flush_print(f"Found {len(c_files)} .c file(s) in '{input_folder}':")
    for c_file in c_files:
        input_path = os.path.join(input_folder, c_file)
        output_path = os.path.join(output_folder, c_file.replace(".c", ".o"))
        
        flush_print(f"Compiling {c_file} into {output_path}...")
        try:
            # Compile the .c file into an object file
            result = subprocess.run(
                ['gcc', '-c', input_path, '-o', output_path],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                flush_print(f"Compilation successful for '{c_file}'.")
            else:
                flush_print(f"Compilation failed for '{c_file}':\n{result.stderr}")
        except FileNotFoundError:
            flush_print("GCC is not installed or not available in PATH.")
            sys.exit(1)
        except Exception as e:
            flush_print(f"An error occurred while compiling '{c_file}': {e}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        flush_print("Usage: python3 stageCompile.py <input_folder> <output_folder>")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    compile_c_files(input_folder, output_folder)
