import os
import time
from termcolor import *

def count_txt_files(folder_path):
    # احصل على جميع الملفات في المجلد
    all_files = os.listdir(folder_path)
    
    # احتسب عدد ملفات txt
    txt_files = [file for file in all_files if file.endswith(".txt")]
    
    return len(txt_files)

def main():
    folder_path = "."  # استبدل بمسار المجلد الخاص بك

    # احصل على العدد الأولي للملفات
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
        # احصل على العدد الحالي للملفات
        current_count = count_txt_files(folder_path)

        # قارن بين العددين
        if current_count != previous_count:
            # إذا كان هناك تغيير، قم بطباعة العدد الجديد
            os.system("clear")
            os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Targets Data | lolcat")
            print("")
            print(f"Targets Online : ")
            print("")
            os.system(f"figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf {current_count} | lolcat")
            # حدث العدد السابق
            previous_count = current_count

        # انتظر لبضع ثواني قبل الفحص التالي
        time.sleep(1)  # يمكنك تعديل هذا حسب احتياجاتك

if __name__ == "__main__":
    main()
