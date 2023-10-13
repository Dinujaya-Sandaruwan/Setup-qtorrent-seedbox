import os

directory = "/var/www/html/"

# Get a list of all files in the directory
file_list = os.listdir(directory)

# Filter the list to only include .zip files
zip_files = [file for file in file_list if file.endswith(".zip")]

if zip_files:
    print("List of downloadable .zip files in server:")
    for i, zip_file in enumerate(zip_files, start=1):
        print(f"{i:02d}. http://178.128.54.254/{zip_file}")
else:
    print("No downloadable torrent files found!")