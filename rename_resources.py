import os

def rename_resource_folders(folder_path, rename_map):
    """
    Rename folders in the given directory using a predefined rename map.

    Parameters:
    - folder_path: Path to the Resources folder.
    - rename_map: Dictionary mapping old folder names to new folder names.
    """
    folders = os.listdir(folder_path)
    
    for folder in folders:
        full_path = os.path.join(folder_path, folder)
        
        if os.path.isdir(full_path):
            new_name = rename_map.get(folder, None)
            
            if new_name:
                new_path = os.path.join(folder_path, new_name)
                os.rename(full_path, new_path)
                print(f"Renamed: {folder} -> {new_name}")
            else:
                print(f"No rename mapping for: {folder}. Skipping.")

if __name__ == "__main__":
    # Path to the Resources folder
    resources_folder_path = "/Users/bethcartrette/Library/Mobile Documents/com~apple~CloudDocs/03_Resources"
    
    # Rename map: Old folder names -> New folder names
    rename_map = {
        "ADOBE": "Resource_Design_Adobe",
        "FIGMA FILES": "Resource_Design_FigmaFiles",
        "FONTS": "Resource_Design_Fonts",
        "SCRIPTS": "Resource_Code_Scripts",
        "MUsic": "Resource_Media_Music",
        "Mockups": "Resource_Design_Mockups",
        "Templates": "Resource_Design_Templates",
        "SlideShow Presentations": "Resource_Media_SlideShowPresentations",
        "UI_UX_Design": "Resource_Design_UIUXDesign",
        "AI IMAGE REFERENCES": "Resource_AI_ImageReferences",
        "AI PROMPTING": "Resource_AI_Prompting",
        "GIFS_2023": "Resource_Media_GIFs2023",
        "Stock Images": "Resource_Media_StockImages",
        "Stock Video": "Resource_Media_StockVideo",
        "COLOR": "Resource_Design_Color",
        "Typography": "Resource_Design_Typography",
        "Hand Lettering": "Resource_Design_HandLettering",
        "Graphic Design": "Resource_Design_GraphicDesign",
        "Web_Development": "Resource_Dev_WebDevelopment",
        "SquareSpace Web Design": "Resource_Dev_SquareSpace",
        "Social Media": "Resource_Media_SocialMedia",
        "CLIENT RESOURCES": "Resource_Business_ClientResources",
        "INSPO SWIPE FILE": "Resource_Design_InspoSwipeFile",
        "Internet Records": "Resource_Misc_InternetRecords",
        "ARC BROWSER": "Resource_Misc_ArcBrowser",
        "Assets": "Resource_Misc_Assets",
    }
    
    # Run the renaming function
    rename_resource_folders(resources_folder_path, rename_map)