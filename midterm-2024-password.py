#password
#midterm question no.2

# Importing modules
import random  # For generating random numbers
import string  # For accessing string constants

def generate_password():
    # Define a list of characters for each requirement
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '@#'
    
    # Generate a random length between 12 and 19 characters
    length = random.randint(12, 19)
    
    # Ensure that at least one lowercase, one uppercase, one digit, and one special character is included
    required_characters = [random.choice(lowercase_letters),
                           random.choice(uppercase_letters),
                           random.choice(digits),
                           random.choice(special_characters)]
    
    # Fill the remaining characters with random choices
    remaining_length = length - len(required_characters)
    password_characters = ''.join([random.choice(string.ascii_letters + string.digits + '@#') for _ in range(remaining_length)])
    
    # Combine required characters and remaining characters
    password = ''.join(required_characters + list(password_characters))
    
    # Shuffle the password characters to ensure randomness
    password = ''.join(random.sample(password, len(password)))
    
    return password

print("Generated Password:", generate_password())
