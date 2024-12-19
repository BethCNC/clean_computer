import os

# Define the root path to your Projects folder
projects_path = "/Users/bethcartrette/Library/Mobile Documents/com~apple~CloudDocs/01_Projects"

# List of existing project folders
existing_folders = [
    "Animation",
    "BethC Brand Fonts & Colors",
    "Bryan Poppy Grow",
    "Carla Creative Club",
    "Clients",
    "Home Projects",
    "ICONS",
    "Keynote Planner 2024",
    "LAUNCH FREELANCE BIZ",
    "Learning_Projects",
    "PERSONAL WEBSITE",
    "Personal_Projects",
    "Planning",
    "Profile Pictures & Avatars",
    "Todoist Setup",
    "Twitter",
    "VALUE OF GOOD DESIGN"
]

# Missing folders based on Finder Favorites
missing_folders = [
    "BETTY BOT",
    "UMI WELLNESS",
    "Diagnosis Binder Design & Assets",
    "ASD 2024",
    "Beth Name Logo"
]

# Rename mapping based on the proposed convention
rename_mapping = {
    "Animation": "2024_Design_Animation",
    "BethC Brand Fonts & Colors": "2024_Design_BethCBrandFonts",
    "Bryan Poppy Grow": "2024_Personal_BryanPoppyGrow",
    "Carla Creative Club": "2024_Design_CarlaCreativeClub",
    "Clients": "2024_Business_Clients",
    "Home Projects": "2024_Personal_HomeProjects",
    "ICONS": "2024_Design_ICONS",
    "Keynote Planner 2024": "2024_Design_KeynotePlanner",
    "LAUNCH FREELANCE BIZ": "2024_Business_LaunchFreelanceBiz",
    "Learning_Projects": "2024_Development_LearningProjects",
    "PERSONAL WEBSITE": "2024_Design_PersonalWebsite",
    "Personal_Projects": "2024_Personal_PersonalProjects",
    "Planning": "2024_Productivity_Planning",
    "Profile Pictures & Avatars": "2024_Design_ProfilePictures",
    "Todoist Setup": "2024_Productivity_TodoistSetup",
    "Twitter": "2024_Business_Twitter",
    "VALUE OF GOOD DESIGN": "2024_Design_ValueOfGoodDesign",
    "BETTY BOT": "2024_Design_BettyBot",
    "UMI WELLNESS": "2024_Design_UMIWellness",
    "Diagnosis Binder Design & Assets": "2024_Health_DiagnosisBinder",
    "ASD 2024": "2024_Health_ASD",
    "Beth Name Logo": "2024_Design_BethNameLogo"
}

def rename_and_create_folders():
    # Rename existing folders
    for folder in existing_folders:
        old_path = os.path.join(projects_path, folder)
        if folder in rename_mapping:
            new_path = os.path.join(projects_path, rename_mapping[folder])
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                print(f"Renamed: {folder} -> {rename_mapping[folder]}")
            else:
                print(f"Folder not found for renaming: {folder}")

    # Create missing folders
    for folder in missing_folders:
        new_folder_name = rename_mapping.get(folder, folder)
        new_folder_path = os.path.join(projects_path, new_folder_name)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f"Created missing folder: {new_folder_name}")
        else:
            print(f"Folder already exists: {new_folder_name}")

# Run the script
rename_and_create_folders()