import os
import shutil

# HashMap for file types (extension -> folder name)
file_type_map = {
    ".txt": "Documents",
    ".pdf": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".docx": "Documents",
    ".pptx": "Presentations",
    ".csv": "Data",
    ".exe": "Executables",
}

def create_folder_if_not_exists(folder_path):
    """Create the folder if it doesn't already exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def organize_files(path):
    """Organize files in the given path by file type."""
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)

        if os.path.isdir(full_path):
            # Skip subdirectories
            continue

        # Skip Python script files
        if entry.endswith('.py'):
            print(f"Skipping Python file: {entry}")
            continue

        # Get file extension
        _, ext = os.path.splitext(entry)
        ext = ext.lower()  # make extension case-insensitive

        # Find the category folder name based on the extension
        folder_name = file_type_map.get(ext)
        if folder_name:
            # Create the category folder if it doesn't exist
            category_folder = os.path.join(path, folder_name)
            create_folder_if_not_exists(category_folder)

            # Move the file into the appropriate folder
            new_file_path = os.path.join(category_folder, entry)
            shutil.move(full_path, new_file_path)
            print(f"Moved: {entry} -> {folder_name}/")
        else:
            print(f"Unknown file type: {entry}")
