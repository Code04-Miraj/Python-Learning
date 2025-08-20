import os
import shutil

folder_path = input("Enter the folder path: ")

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    print(f"\nFiles in '{folder_path}':\n")

    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "PDFs": [".pdf"],
        "Documents": [".doc", ".docx", ".txt", ".odt"],
        "Spreadsheets": [".xls", ".xlsx", ".csv"],
        "Compressed": [".zip", ".rar", ".tar", ".gz"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Audio": [".mp3", ".wav", ".aac"],
    }

    found_categories = set()
    file_classification = {}
    files = os.listdir(folder_path)

    # Step 1: Classify files
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            name, ext = os.path.splitext(file)
            ext = ext.lower()

            found_category = None
            for category, extensions in categories.items():
                if ext in extensions:
                    found_category = category
                    break

            if found_category:
                print(f"{file} --> This is a {found_category}")
                found_categories.add(found_category)
                file_classification[file] = found_category
            elif ext == "":
                print(f"{file} --> No Extension (Unknown Type)")
            else:
                print(f"{file} --> Unknown Type ({ext})")

    # Step 2: Create folders
    for category in found_categories:
        category_folder = os.path.join(folder_path, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
            print(f"✅ Folder Created: {category_folder}")

    # Step 3: Move files
    for file, category in file_classification.items():
        src_path = os.path.join(folder_path, file)
        dest_path = os.path.join(folder_path, category, file)
        shutil.move(src_path, dest_path)
        print(f"Moved {file} --> {category}/")

else:
    print("❌ The folder path you entered is not correct")
