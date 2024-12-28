import os
import shutil

def transfer_files():
    # Define the source and target directories
    downloads_dir = os.path.expanduser("~/Downloads")
    target_dir = os.path.join(downloads_dir, "mercari_labels")

    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Loop through files in the Downloads directory
    for file_name in os.listdir(downloads_dir):
        # Check if the file starts with 'item-'
        if file_name.startswith("item-"):
            source_path = os.path.join(downloads_dir, file_name)
            target_path = os.path.join(target_dir, file_name)

            # Move the file to the target directory
            shutil.move(source_path, target_path)
            print(f"Moved: {file_name}")

    print("Transfer complete!")

if __name__ == "__main__":
    transfer_files()
