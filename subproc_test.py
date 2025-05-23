import subprocess
import time
import signal
import sys
import os
import msvcrt
time_rec=60
os.chdir(r'C:\Users\Graybird\MousePortal')
# Start the subprocess
proc = subprocess.Popen([sys.executable, 'trigger_cam_rec'])

try:
    print("Press 'Esc' to stop recording early...")
    start = time.time()
    while time.time() - start < time_rec:
        if msvcrt.kbhit():
            if msvcrt.getch() == b'\x1b':  # ESC key
                print("Esc pressed, terminating...")
                break
        time.sleep(0.1)
finally:
    # Terminate the subprocess
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()