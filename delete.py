import shutil

# Get input names separated by commas
folder_names = input("Enter folder names to delete (separated by commas): ").split(",")

for folder_name in folder_names:
    folder_name = folder_name.strip()
    try:
        shutil.rmtree(folder_name)
        print(f"{folder_name} deleted successfully!")
    except OSError as e:
        print(f"Error deleting {folder_name}: {e}")
