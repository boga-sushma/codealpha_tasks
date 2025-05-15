import os
import shutil

# Path to the folder you want to organize
SOURCE_FOLDER = r"C:\Users\dell\Downloads"

# File type categories and their extension
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}

def get_category(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files():
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        category = get_category(file)
        category_folder = os.path.join(SOURCE_FOLDER, category)

        # Create category folder if it doesn't exist
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        # Move file to appropriate folder
        dest_path = os.path.join(category_folder, file)
        shutil.move(file_path, dest_path)
        print(f"Moved: {file} --> {category}/")

if __name__ == "__main__":
    organize_files()
