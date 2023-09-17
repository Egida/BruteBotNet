import os
import shutil
import hashlib
import time

def calculate_hash(file_path):
    # Calculate a hash of the file's content
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def are_files_identical(file_path1, file_path2):
    # Compare the content hashes of two files
    return calculate_hash(file_path1) == calculate_hash(file_path2)

def copy_unique_text_files(source_dir, target_dir):
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Initialize a list to track copied file paths
    copied_files = []

    # Initialize counters for source and target files
    source_file_count = 0
    target_file_count = 0

    # Scan source directory for text files (only in the top-level directory)
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)

        # Check if the file is a text file (you can add more extensions if needed)
        if file_name.endswith((".txt", ".csv")):
            source_file_count += 1

            # Check if the file content is already copied
            if not any(are_files_identical(file_path, copied_file) for copied_file in copied_files):
                # Copy the file to the target directory
                target_file_path = os.path.join(target_dir, file_name)
                shutil.copy2(file_path, target_file_path)
                target_file_count += 1

                # Add the copied file to the list
                copied_files.append(target_file_path)

    return source_file_count, target_file_count

if __name__ == "__main__":
    source_directory = "."
    target_directory = "Data"

    while True:
        source_count, target_count = copy_unique_text_files(source_directory, target_directory)
        os.system("clear")
        os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Targets Data  | lolcat")

        print(f"Tagets Online : ")
        print(" ")
        os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/Reg.flf {source_count} | lolcat")
        print(f"Total Targets : ")
        print(" ")
        os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/Reg.flf {target_count} | lolcat")
        
        # Sleep for a specified time before scanning again (e.g., 1 sec)
        time.sleep(5)  # Sleep for 1 sec (adjust as needed)
