import os
import shutil

# Define the folder paths
icloud_root = "/Users/bethcartrette/Library/Mobile Documents/com~apple~CloudDocs"
areas_folder = os.path.join(icloud_root, "02_Areas")

# Define categories and their corresponding folders
categories = {
    "Beth Business": ["WORK", "Finances", "SARAH"],
    "Health": ["BETH MEDICAL", "Health", "GEORGE"],
    "Development & AI": ["LEARN_TO_CODE_2024", "GPT_2024", "AUTOMATIONS_and_AI_2024"],
    "Design": ["BETH C BRAND", "7 Stars", "Design"],
    "HOME LIFE": ["HOME LIFE", "PERSONAL", "Major"],
    "PRODUCTIVITY": ["PRODUCTIVITY", "Research & Notes"],
}

# Function to categorize folders
def categorize_areas():
    for category, folders in categories.items():
        # Create the category folder if it doesn't exist
        category_path = os.path.join(areas_folder, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

        # Move folders into the appropriate category
        for folder in folders:
            folder_path = os.path.join(areas_folder, folder)
            if os.path.exists(folder_path):
                print(f"Moving {folder} -> {category_path}")
                shutil.move(folder_path, category_path)

    print("Categorization complete!")

# Run the function
if __name__ == "__main__":
    categorize_areas()