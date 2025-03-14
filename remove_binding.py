

# script to remove port binding from the server for macos
import socket
import os
import subprocess
import time
import signal
import sys
def get_pid_using_port(port):
    """Get the PID of the process using the specified port."""
    try:
        # Use lsof to find the PID of the process using the port
        result = subprocess.run(['lsof', '-t', f'-i:{port}'], capture_output=True, text=True)
        pids = result.stdout.strip().split('\n')
        return [int(pid) for pid in pids if pid]
    except Exception as e:
        print(f"Error getting PID for port {port}: {e}")
        return None
def kill_process(pid):
    """Kill the process with the specified PID."""
    try:
        os.kill(pid, signal.SIGTERM)
        print(f"Process {pid} killed.")
    except Exception as e:
        print(f"Error killing process {pid}: {e}")
def remove_port_binding(port):
    """Remove port binding by killing the process using the port."""
    pids = get_pid_using_port(port)
    if pids:
        for pid in pids:
            kill_process(pid)
        print(f"Port {port} is now free.")
    else:
        print(f"No process found using port {port}.")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_binding.py <port>")
        sys.exit(1)
    port = int(sys.argv[1])
    remove_port_binding(port)
    time.sleep(2)
    print("Port binding removed.")