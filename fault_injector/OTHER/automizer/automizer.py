import subprocess
import threading
import os
import time

num_hpc = 42

fi_file = "main.py"
sniffer_file = "sniffer.py"
converter_csv_file = "csv_converter.py" 

fault_file = "faults"

def cleanup():
    '''
    Remove the faults and hpc files
    '''
    if os.path.exists(fault_file):
        os.remove(fault_file)
        print(f"{fault_file} has been deleted.")
    
def start_process():
    '''
    start the fault injector and the sniffer file
    DOTO passing parameters to the process
    '''
    fi = subprocess.Popen(["python3", fi_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    sniffer = subprocess.Popen(["python3", sniffer_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    time.sleep(6)
    return fi, sniffer

def post_process():
    return

def stream_file():
    """Reads a file line by line as it is being written."""
    try:
        with open(fault_file, "r") as fault:
            # Move the file pointer to the end of the file initially
            fault.seek(0, 2)
            i = 0
            void_cycle = 0
            while True:
                line = fault.readline()
                if "golden run" in line:
                    print("Detected a crash")
                    break
                if line:
                    print(line, end="")  # Avoid adding extra newlines    
                    void_cycle = 0
                else:
                    void_cycle += 1    
                if void_cycle > 5000:
                    break    
                time.sleep(0.01)
                i+=1
            post_process()

    except FileNotFoundError:
        print(f"File not found.")
    except KeyboardInterrupt:
        print("\nStopped reading the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    while True: 
        cleanup()
        print("Start the Injection process")
        fi, sniffer = start_process()
        print("Init the reading")
        stream_file()
        fi.kill()
        sniffer.kill()
    
