import os
import shutil
import hashlib
import time

def calculate_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def are_files_identical(file_path1, file_path2):
    return calculate_hash(file_path1) == calculate_hash(file_path2)

def copy_unique_text_files(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    copied_files = []

    source_file_count = 0
    target_file_count = 0

    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)

        if file_name.endswith((".txt", ".csv")):
            source_file_count += 1

            if not any(are_files_identical(file_path, copied_file) for copied_file in copied_files):
                target_file_path = os.path.join(target_dir, file_name)
                shutil.copy2(file_path, target_file_path)
                target_file_count += 1

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
        
        time.sleep(1)  
