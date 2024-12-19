import os
import shutil

def organize_files():
    base_path = "/Users/bethcartrette/Library/Mobile Documents/com~apple~CloudDocs"

    # Correct folders and their destinations
    folders_to_move = {
        "01_Projects/Clients/Sarah Email June 2024": "01_Projects/Clients/",
        "01_Projects/Clients/Creative Comunity Club": "01_Projects/Clients/",
        "01_Projects/Personal_Projects/life timeline gameboard": "01_Projects/Personal_Projects/",
        "01_Projects/Personal_Projects/Art Licensing": "01_Projects/Personal_Projects/",
        "01_Projects/Personal_Projects/GREETING CARDS": "01_Projects/Personal_Projects/",
        "01_Projects/Learning_Projects/Character Design": "01_Projects/Learning_Projects/",
    }

    print("Organizing files...")

    for folder_name, target_path in folders_to_move.items():
        full_folder_path = os.path.join(base_path, folder_name)
        target_folder_path = os.path.join(base_path, target_path, os.path.basename(folder_name))

        print(f"Checking for folder: {full_folder_path}")
        if os.path.exists(full_folder_path):
            if os.path.exists(target_folder_path):
                print(f"Destination already exists: {target_folder_path}")
            else:
                try:
                    shutil.move(full_folder_path, os.path.join(base_path, target_path))
                    print(f"Moved: {folder_name} to {target_path}")
                except Exception as e:
                    print(f"Error moving {folder_name}: {e}")
        else:
            print(f"Folder not found: {full_folder_path}")

if __name__ == "__main__":
    organize_files()