import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# the minimum length of the password is 50 characters
minimum_length = 50
random_password = generate_random_password(minimum_length - len("Nimra"))

# "Nimra" is always a part of the password
password = random_password + "Nimra"

print(password) 