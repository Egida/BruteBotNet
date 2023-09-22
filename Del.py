import os
import filecmp
import hashlib
import time

directory_to_scan = "."  
scan_interval = 1  
max_survival_scans = 60

def is_text_file(filename):
    text_extensions = {".txt", ".csv", ".log", ".xml"} 
    _, file_extension = os.path.splitext(filename)
    return file_extension.lower() in text_extensions

def get_file_hash(filename):
    # Calculate the MD5 hash of a file.
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_duplicate_text_files(directory):
    file_hashes = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            full_path = os.path.join(root, filename)
            if is_text_file(full_path):
                file_hash = get_file_hash(full_path)
                if file_hash in file_hashes:
                    file_hashes[file_hash].append(full_path)
                else:
                    file_hashes[file_hash] = [full_path]
    return file_hashes

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted Report: {file_path}")
    except Exception as e:
        print(f"Error deleting Report {file_path}: {str(e)}")

def main():
    while True:
        try:
            last_scan_time = time.time()
            scan_count = 0
            
            while True:
                current_time = time.time()
                
                if current_time - last_scan_time >= scan_interval:
                    file_hashes = find_duplicate_text_files(directory_to_scan)
                    last_scan_time = current_time
                    scan_count += 1
                    
                    for hash_value, file_list in file_hashes.items():
                        if len(file_list) > 1:
                            file_list.sort(key=lambda x: os.path.getmtime(x), reverse=True)
                            
                            for i in range(1, len(file_list)):
                                if filecmp.cmp(file_list[0], file_list[i]):
                                    print(f"Deleting duplicate: {file_list[i]}")
                                    delete_file(file_list[i])
                
                if scan_count >= max_survival_scans:
                    last_file_list = find_duplicate_text_files(directory_to_scan).get(list(file_hashes.keys())[0], [])
                    if len(last_file_list) == 1:
                        print(f"Deleting last Report: {last_file_list[0]}")
                        delete_file(last_file_list[0])
                        scan_count = 0
                
                time.sleep(1)
                os.system("clear")
                os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Delete Old Reports. | lolcat")
                time.sleep(0.5)
                os.system("clear")
                os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Delete Old Reports.. | lolcat")
                time.sleep(0.5)
                os.system("clear")
                os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Delete Old Reports... | lolcat")
        except Exception as e:
            print(f"Error: {str(e)}")
            continue

if __name__ == "__main__":
    main()
