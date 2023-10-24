import random
import string

def generate_random_password_with_nimra(length):
    if length < 8:
        return "Password length should be at least 8 characters."

    password_length = length - len("Nimra")
    # length of the password excluding "Nimra" in the middle

    characters = string.ascii_letters + string.digits + string.punctuation
    half_length = password_length // 2

    first_half = ''.join(random.choice(characters) for _ in range(half_length))
    # the first half of the password

    second_half = ''.join(random.choice(characters) for _ in range(half_length))
    # second half of the password

    password = first_half + "Nimra" + second_half
    # Combine the two halves with Nimra

    return password

password_length = int(input("Enter the desired password length: "))

random_password = generate_random_password_with_nimra(password_length)
print("Generated Random Password:", random_password)
