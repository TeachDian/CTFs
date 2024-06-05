import hashlib
import os

def calculate_checksum(file_path):
    """Calculate the checksum of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

def main():
    # Specify the folder path
    folder_path = "files"

    # Get the list of files in the specified folder
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Calculate and print checksum for each file
    for file_name in files:
        checksum = calculate_checksum(file_name)
        if checksum == "55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a":
            print(f"Correct file is {file_name}")

if __name__ == "__main__":
    main()
