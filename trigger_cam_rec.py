#!/usr/bin/env python3

import cv2
import signal
import sys
import time
import os
output_folder=r'C:\Users\Graybird\Desktop\test\catpured_frames'
# Global flag for termination
terminate = False

def handle_sigterm(signum, frame):
    global terminate
    terminate = True

def main():
    # Register SIGTERM handler
    signal.signal(signal.SIGTERM, handle_sigterm)

    # Video capture setup
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Error: Cannot open camera", file=sys.stderr)
        sys.exit(1)

    # Video writer setup
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out_filename = f"{output_folder}/frame_{int(time.time())}.avi"
    fps = 20.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(out_filename, fourcc, fps, (width, height))

    try:
        while not terminate:
            ret, frame = cap.read()
            if not ret:
                print("Error: Can't receive frame. Exiting...", file=sys.stderr)
                break
            out.write(frame)
            # Sleep to match FPS
            time.sleep(1.0 / fps)
    finally:
        cap.release()
        out.release()
        print(f"Video saved as {out_filename}")

if __name__ == "__main__":
    main()