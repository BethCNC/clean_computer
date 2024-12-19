import os

def organize_areas_with_years(areas_path, years):
    """
    Organize areas by renaming and creating yearly subfolders.
    
    Parameters:
    - areas_path: Path to the "Areas" folder.
    - years: List of years to create subfolders for.
    """
    areas = os.listdir(areas_path)
    
    for area in areas:
        area_path = os.path.join(areas_path, area)
        
        # Ensure it’s a folder
        if os.path.isdir(area_path):
            # Rename to consistent format (e.g., Beth Business -> Area_BethBusiness)
            renamed_area = f"Area_{area.replace(' ', '')}"
            renamed_area_path = os.path.join(areas_path, renamed_area)
            os.rename(area_path, renamed_area_path)
            print(f"Renamed: {area} -> {renamed_area}")
            
            # Create yearly subfolders
            for year in years:
                year_path = os.path.join(renamed_area_path, str(year))
                if not os.path.exists(year_path):
                    os.makedirs(year_path)
                    print(f"Created: {year_path}")

if __name__ == "__main__":
    # Path to the "Areas" folder
    areas_folder_path = "/Users/bethcartrette/Library/Mobile Documents/com~apple~CloudDocs/02_Areas"
    
    # List of years to create subfolders for
    years_to_add = [2024, 2025]
    
    # Organize and rename folders
    organize_areas_with_years(areas_folder_path, years_to_add)