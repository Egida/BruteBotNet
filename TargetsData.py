import os
import time
from termcolor import *

def count_txt_files(folder_path):
    all_files = os.listdir(folder_path)
    
    txt_files = [file for file in all_files if file.endswith(".txt")]
    
    return len(txt_files)

def main():
    folder_path = "." 

    previous_count = count_txt_files(folder_path)

    if previous_count == 0:
        os.system("clear")
        os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Targets Data  | lolcat")
        print("")
        x = colored("[+] No Targets Connected!", 'red')
        print(x)
        print("")
        os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf 0 | lolcat")

    while True:
        current_count = count_txt_files(folder_path)

        if current_count != previous_count:
            os.system("clear")
            os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Targets Data | lolcat")
            print("")
            print(f"Targets Online : ")
            print("")
            os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf {current_count} | lolcat")
            previous_count = current_count

        time.sleep(1) 

if __name__ == "__main__":
    main()
