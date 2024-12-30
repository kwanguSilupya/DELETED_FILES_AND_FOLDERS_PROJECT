#make a programme that recovers deleted files and folders

import subprocess

def recover_files(disk_image):
    try:
        # Provide the full path to photorec
        subprocess.run(["/usr/local/bin/photorec", disk_image], check=True)
        print(f"Recovery started for {disk_image}")
    except subprocess.CalledProcessError as e:
        print(f"Error during file recovery: {e}")
    except FileNotFoundError:
        print("Error: photorec executable not found. Ensure it's installed and in your system's PATH.")

# Specify the disk or partition to recover from
recover_files('/dev/sda1')  # Replace with the appropriate disk or partition