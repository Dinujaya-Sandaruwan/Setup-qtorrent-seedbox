import os
import shutil
import zipfile

# Function to list folders in the current directory
def list_folders():
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    for i, folder in enumerate(folders, 1):
        print(f"{i:02d}. {folder}")
    return folders

# Function to compress a folder to a zip file and then delete the folder
def compress_and_delete_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    folder_name = folder_name.replace(" ", "_")  # Replace spaces with underscores in folder name
    zip_file_name = folder_name + ".zip"
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                arcname = arcname.replace(" ", "_")  # Replace spaces with underscores in file paths
                arcname_parts = arcname.split(os.path.sep)
                if arcname_parts[0] == "Other":
                    arcname_parts.pop(0)
                arcname = os.path.join(*arcname_parts)
                zipf.write(file_path, arcname=arcname)
                os.rename(file_path, os.path.join(root, arcname.replace("_", " ")))  # Rename the file
    new_folder_path = os.path.join(os.path.dirname(folder_path), folder_name)  # Rename the folder
    shutil.move(folder_path, new_folder_path)  # Rename and move the folder
    shutil.rmtree(new_folder_path)  # Delete the renamed folder
    return zip_file_name

# List all folders in the current directory
folders = list_folders()

# Ask the user for input (folder number)
while True:
    try:
        str_folder_number = input("Enter the number of the folder you want to zip (q to quit): ")
        if (str_folder_number != "q"):
            folder_number = int(str_folder_number)

        if str_folder_number == "q":
            print("Quitting the program.")
            break
        if folder_number < 1 or folder_number > len(folders):
            print("Invalid folder number. Please try again.")
            continue

        folder_to_zip = folders[folder_number - 1]
        zip_file_name = compress_and_delete_folder(folder_to_zip)
        print(f"Compressed for download: {folder_to_zip}, Zip File: {zip_file_name}")
        print(f"URL : http://178.128.54.254/{zip_file_name}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
