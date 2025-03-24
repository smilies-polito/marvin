import subprocess
import sys

def run_python_program(child_program):
    try:
        # Start the child program
        with subprocess.Popen(
            [sys.executable, child_program],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # Merge stderr into stdout
            bufsize=1,                # Line buffering
            universal_newlines=True   # Text mode for reading output
        ) as process:
            # Stream child's stdout to the parent's stdout in real-time
            for line in process.stdout:
                print(line, end="")  # Print each line without adding extra newlines

            # Wait for the child process to complete
            process.wait()

            # Check the exit code of the child process
            if process.returncode == 0:
                print(f"\n{child_program} finished successfully.")
            else:
                print(f"\n{child_program} exited with errors. Return code: {process.returncode}")

    except FileNotFoundError:
        print(f"Error: Program '{child_program}' not found.")
    except Exception as e:
        print(f"An error occurred while running {child_program}: {e}")

if __name__ == "__main__":
    # Replace with the path to your child Python script
    child_program_path = "program1.py"
    
    run_python_program(child_program_path)
