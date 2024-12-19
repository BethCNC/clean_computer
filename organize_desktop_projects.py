import os
import shutil

# Paths
desktop_path = "/Users/bethcartrette/Desktop"
icloud_projects_path = "/Users/bethcartrette/Library/Mobile Documents/com~apple~CloudDocs/01_Projects"

# Define active projects (favorites or currently working on)
active_projects = [
    "Animation", "BethC Brand Fonts & Colors", "Bryan Poppy Grow",
    "Carla Creative Club", "Clients", "Home Projects",
    "Keynote Planner 2024", "LAUNCH FREELANCE BIZ", "Learning_Projects",
    "PERSONAL WEBSITE", "Personal_Projects", "VALUE OF GOOD DESIGN"
]

# Define fallback folder for uncategorized items
misc_folder = os.path.join(icloud_projects_path, "Personal_Projects/Misc")

def find_project_folder(item_name):
    """Check if a file or folder matches an active project."""
    for project in active_projects:
        if project.lower() in item_name.lower():
            return os.path.join(icloud_projects_path, project)
    return None

def organize_desktop():
    # Ensure the fallback folder exists
    os.makedirs(misc_folder, exist_ok=True)

    # Iterate through desktop contents
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)

        # Skip system files
        if item.startswith('.'):
            continue

        # Check if item matches an active project
        project_folder = find_project_folder(item)
        if project_folder:
            os.makedirs(project_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(project_folder, item))
            print(f"Moved: {item} -> {project_folder}")
            continue

        # If item is a directory and doesn't match a project
        if os.path.isdir(item_path):
            # Move to misc folder for manual sorting
            target_path = os.path.join(misc_folder, item)
            shutil.move(item_path, target_path)
            print(f"Moved folder: {item} -> {misc_folder}")
        else:
            # Move files to misc folder for manual sorting
            target_path = os.path.join(misc_folder, item)
            shutil.move(item_path, target_path)
            print(f"Moved file: {item} -> {misc_folder}")

if __name__ == "__main__":
    print("Organizing desktop...")
    organize_desktop()
    print("Desktop organized!")