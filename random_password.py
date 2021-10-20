import random 
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

password_len = 16 
passwords_amount = 50 
passwords = []
current_password = ''

def generate_passwords(password_len = 16, uppercase = True, lowercase = True, digs = True, syms = True):
    full_string = ''
    if uppercase:
        full_string += uppercase_letters
    if lowercase:
        full_string += lowercase_letters
    if digs:
        full_string += digits
    if syms:
        full_string += symbols

    for password in range(0,passwords_amount): 
        current_password = ''
        for index in range(0,password_len):
            current_password += full_string[random.randrange(0,len(full_string))]
        passwords.append(current_password)

    return passwords[random.randrange(0,len(passwords))]


print(generate_passwords())


        




