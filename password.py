import random
import string

def generate_hardcore_password(length=16):
    if length < 8:
        raise ValueError("Password length should be at least 8")

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()-_=+[]{}|;:',.<>?/"

    # Guarantee at least one character from each category
    password_chars = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with a mix of all characters
    all_chars = upper + lower + digits + special
    password_chars += random.choices(all_chars, k=length - 4)

    # Shuffle the resulting list to randomize character positions
    random.shuffle(password_chars)

    # Join to form the final password string
    return ''.join(password_chars)

if __name__ == "__main__":
    pwd_length = 16  # Change length if you want
    password = generate_hardcore_password(pwd_length)
    print("Generated hardcore password:", password)
