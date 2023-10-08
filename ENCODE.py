from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

python_code = """
YOUR Python BotNet code
"""

encrypted_code = cipher_suite.encrypt(python_code.encode())

with open('encryption_KEY.txt', 'wb') as key_file:
    key_file.write(key)

with open('encrypted_CODE.txt', 'wb') as code_file:
    code_file.write(encrypted_code)
