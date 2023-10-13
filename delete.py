import os

# Directory where .zip files are located
directory = "/var/www/html/"

# List all .zip files in the directory
zip_files = [f for f in os.listdir(directory) if f.endswith('.zip')]

if not zip_files:
    print("No .zip files found in the directory.")
else:
    # Print the list of .zip files with numbers
    print("List of .zip files:")
    for i, zip_file in enumerate(zip_files, start=1):
        print(f"{i:02d}. {zip_file}")

    while True:
        try:
            # Ask the user to enter a number
            user_input = input("Enter the number of the file to delete (or 'q' to quit): ")
            
            if user_input == 'q':
                break

            # Convert user input to an integer
            selected_number = int(user_input)

            # Check if the selected number is within a valid range
            if 1 <= selected_number <= len(zip_files):
                selected_file = os.path.join(directory, zip_files[selected_number - 1])

                # Ask for confirmation before deleting
                confirm = input(f"Do you really want to delete '{selected_file}'? (yes/no): ").strip().lower()

                if confirm == "yes" or confirm == "y":
                    # Delete the selected file
                    os.remove(selected_file)
                    print(f"'{selected_file}' was deleted.")
                    zip_files.pop(selected_number - 1)  # Remove the file from the list
                else:
                    print(f"'{selected_file}' was not deleted.")
            else:
                print("Invalid number. Please enter a valid number.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid number or 'q' to quit.")
