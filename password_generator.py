import random 
import string

def generate_password(length=12):
    if length < 4:
        print("Password length should be at least 4 characters")
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += random.choices(all_characters, k=length-4)

    random.shuffle(password)

    return ''.join(password)

password_length = 16 
password = generate_password(password_length)

print(f"Generated password: {password}")