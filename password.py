import random
import string

def generate_password(length, include_digits=True, include_special_chars=True):
   
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    
    password = ''.join(random.choices(characters, k=length))
    return password


def password_generator():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive integer for the password length.")
            else:
                include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
                include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

                password = generate_password(length, include_digits, include_special_chars)
                print("Generated Password:", password)
                break
        except ValueError:
            print("Invalid input. Please enter a valid password length as a positive integer.")

if __name__ == "__main__":
    password_generator()
