import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the desired password length: "))

if password_length < 8:
    print("Password length should be at least 8 characters.")
else:
    random_password = generate_random_password(password_length)
    print("Generated Random Password:", random_password)