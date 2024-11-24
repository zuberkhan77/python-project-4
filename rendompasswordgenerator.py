import random

def generate_password(length):
    """
    Generates a random password of specified length consisting of digits (0-9).
    
    Parameters:
        length (int): Length of the password to generate.

    Returns:
        str: Generated password.
    """
    if length <= 0:
        return "Invalid length. Length should be greater than 0."
    
    # Generate a password using random digits
    password = ''.join(random.choices('abc@0123456789', k=length))
    return password

# Input: Specify the password length
try:
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
