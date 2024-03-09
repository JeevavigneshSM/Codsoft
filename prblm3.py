import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))

def main():
    length = int(input("Enter the desired length of the password: "))
    print("Generated Password:", generate_password(length))

if name == "main":
    main()