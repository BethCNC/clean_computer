import os
import shutil
from datetime import datetime

icloud_root = "/Users/bethcartrette/Library/Mobile Documents/com~apple~CloudDocs"
areas_folder = os.path.join(icloud_root, "02_Areas")
archives_folder = os.path.join(icloud_root, "04_Archives/2023")

# Create archives folder if it doesn't exist
if not os.path.exists(archives_folder):
    os.makedirs(archives_folder)

def archive_old_folders():
    for folder in os.listdir(areas_folder):
        folder_path = os.path.join(areas_folder, folder)
        if os.path.isdir(folder_path):
            # Get last modified time of the folder
            last_modified = datetime.fromtimestamp(os.path.getmtime(folder_path))
            if "_2023" in folder or last_modified.year == 2023:
                print(f"Archiving: {folder}")
                shutil.move(folder_path, os.path.join(archives_folder, folder))

    print("Archiving complete!")

if __name__ == "__main__":
    archive_old_folders()