import requests

# قائمة بالروابط التي تحتوي على الملفات التي ترغب في تنزيلها
urls = [
    'https://github.com/AzizDXT/BruteBotNet/releases/download/V6.0/PYIN.ps1',
    'https://github.com/AzizDXT/BruteBotNet/releases/download/V6.0/InstallerBN.zip',
    'https://github.com/AzizDXT/BruteBotNet/releases/download/V6.0/Advanced.Installer.Architect.v13.2.exe'
]

# مجلد الوجهة الذي ترغب في حفظ الملفات فيه
destination_folder = '.'

# تكرار عبر الروابط وتنزيل الملفات
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        # استخراج اسم الملف من عنوان الرابط
        file_name = url.split('/')[-1]
        file_path = destination_folder + file_name
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f'Downloaded > {file_name}')
    else:
        print(f'No Downloaded {url}')
