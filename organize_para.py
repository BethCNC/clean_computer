import os
import shutil

# Define the root of your iCloud storage
icloud_root = "/Users/bethcartrette/Library/Mobile Documents/com~apple~CloudDocs"

# Define PARA areas and related project folders
areas = {
    "Beth Business": [
        "FINANCE_AGENT",
        "BethCNC Brand",
        "Tailwind CSS CSV FIles",
    ],
    "Health": [
        "Personal Website Assets",
        "Diagnosis Binder Design & Assets",
    ],
    "Development & AI": [
        "streamlit UI",
        "CUSTOM_GPT_CONVERSATIONS",
    ],
    "Design": [
        "Maybry_Pro_Font",
        "BETTY BOT",
    ],
}

# Destination for uncategorized files
miscellaneous_folder = os.path.join(icloud_root, "01_Projects/Personal_Projects/Misc")

# Function to organize files into projects
def organize_folders():
    for area, projects in areas.items():
        # Define area directory
        area_dir = os.path.join(icloud_root, "02_Areas", area)
        if not os.path.exists(area_dir):
            os.makedirs(area_dir)

        for project in projects:
            project_src = os.path.join(miscellaneous_folder, project)
            project_dst = os.path.join(area_dir, project)
            
            # Move project folder if exists in Misc
            if os.path.exists(project_src):
                print(f"Moving {project} -> {project_dst}")
                shutil.move(project_src, project_dst)

    print("Organization complete!")

if __name__ == "__main__":
    organize_folders()