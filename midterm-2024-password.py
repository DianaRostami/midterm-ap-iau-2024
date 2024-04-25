
# Importing modules
import random  # For generating random numbers
import string  # For accessing string constants

# Function to generate a password
def generate_password():
    # Generate a random length between 12 and 19 characters
    length = random.randint(12, 19)
    
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the passwordt
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Print the generated password
print("Generated Password:", generate_password())

