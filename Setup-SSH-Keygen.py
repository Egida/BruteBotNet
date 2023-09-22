import os
from termcolor import colored
import time
import random


INFO = colored("There are important instructions before using this service!", 'red')
print(INFO)
print("=" * 40)
print("""
1- First pressing the Enter button.
         
2- You will be asked this question 'Generating public/private rsa key pair. Enter file in which to save the key (/home/Your-user-name/.ssh/id_rsa)' before creating the key, Also, save the key file in its default location by pressing the Enter button.

3- You will also be asked this question 'Enter passphrase (empty for no passphrase):' Enter a password and then again to verify and save it.
        
4- After successfully creating a key, all that remains is verification via a Google account or a GitHub account. Just write a random domain for initial verification, and after that, the script will verify the rest of the requirements.
""")
print("=" * 40)
print("Start Setup")
print("=" * 40)
print("SSH Key Setup")
os.system("ssh-keygen && exit")
print("=" * 40)
time.sleep(3)
print("Verify with Google or GitHub account")
print("=" * 40)
print("Your Test Domain")
PORTSERV = input("Domain :")
print("After this command, a script will be run and it contains two links, the first is Google and the second is GitHub. Copy one of them and enter them in the browser and log in with one of the accounts in order for the verification to be successful.")
print("")
X = colored("After successful verification, you can close the window and it will not appear again.",'red')
print(X)
time.sleep(2)
Loc = random.randint(1090, 49151)
os.system(f"ssh -R {PORTSERV}:80:localhost:{Loc} serveo.net")
