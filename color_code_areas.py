import subprocess
import os

def color_code_areas(folder_path, color_map):
    """
    Apply color tags to folders in the Areas folder using AppleScript.

    Parameters:
    - folder_path: Path to the Areas folder.
    - color_map: Dictionary mapping folder names to color indices.
    """
    folders = os.listdir(folder_path)
    
    for folder in folders:
        full_path = os.path.join(folder_path, folder)
        
        # Ensure it's a directory
        if os.path.isdir(full_path):
            # Get color index from the color map
            color_index = color_map.get(folder, None)  # None if folder is not in the map
            
            if color_index is None:
                print(f"Folder '{folder}' not found in area_color_map. Skipping.")
                continue
            
            # AppleScript to apply the color
            applescript = f'''
            tell application "Finder"
                set folderPath to POSIX file "{full_path}" as alias
                set label index of folderPath to {color_index}
            end tell
            '''
            
            # Run AppleScript via subprocess
            subprocess.run(["osascript", "-e", applescript], check=True)
            print(f"Applied color {color_index} to: {folder}")

if __name__ == "__main__":
    # Path to the Areas folder
    areas_folder_path = "/Users/bethcartrette/Library/Mobile Documents/com~apple~CloudDocs/02_Areas"
    
    # Map folder names to Finder label indices
    area_color_map = {
        "Area_BethBusiness": 4,        # Yellow
        "Area_HOMELIFE": 6,           # Light Blue (Cyan)
        "Area_Health": 3,             # Orange
        "Area_Design": 7,             # Purple
        "Area_Development&AI": 5,     # Pink
        "Area_PRODUCTIVITY": 2        # Dark Blue
    }
    
    # Apply color coding
    color_code_areas(areas_folder_path, area_color_map)