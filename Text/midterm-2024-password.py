#password
#midterm question no.2

# Importing modules
import random  # For generating random numbers
import string  # For accessing string constants

def generate_password():
    # Define a list of characters for each requirement
    lowercase_letters = ''.join([c for c in string.ascii_lowercase if c not in 'aeiou'])
    uppercase_letters = ''.join([c for c in string.ascii_uppercase if c not in 'AEIOU'])
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
    password_characters = ''.join([random.choice(lowercase_letters + uppercase_letters + digits + '@#') for _ in range(remaining_length)])
    
    # Combine required characters and remaining characters
    password = ''.join(required_characters + list(password_characters))
    
    # Shuffle the password characters to ensure randomness
    password = ''.join(random.sample(password, len(password)))
    
    return password

# Generate 10 passwords
passwords = [generate_password() for _ in range(10)]

# Save passwords to a text file
with open('passwords.txt', 'w') as file:
    for password in passwords:
        file.write(password + '\n')

# Confirming the passwords are generated and saved
print("Passwords generated and saved successfully!")
