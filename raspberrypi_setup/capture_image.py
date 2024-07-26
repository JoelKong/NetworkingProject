#Script that captures image every second via pi2
import subprocess
import time

def capture_image():
    while True:
        try:
            # Run the libcamera-jpeg command to capture an image
            subprocess.run(['libcamera-jpeg', '-o', '/home/networking/test.jpg'])
            print("Image captured")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        # Wait for 1 second 
        time.sleep(10)

if __name__ == "__main__":
    capture_image()
