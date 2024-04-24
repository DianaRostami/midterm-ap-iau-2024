#text

#read_text_file function takes an input parameter called file_path, which represents the path to a text file.
def read_text_file(file_path):
    try:
        #open() allows us to open a file in read mode
        #encoding='utf-8' indicates that we're opening the file in UTF-8 format
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content  # Return the content of the file

    except FileNotFoundError:
        print("File not found")
        return None  # Return None if the file is not found
    except Exception as e:
        print("Error:", e)
        return None  # Return None for any other errors

#cout-characters function takes the content of the text file as input
#It returns the character_count dictionary containing the count of each character
def count_characters(content):
    character_count = {}

    for char in content:
        if char.isalnum():  # Check if the character is alphanumeric
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1

    return character_count

# Select the file
file_path = "input.txt"

# Call the function to read the file
file_content = read_text_file(file_path)

if file_content is not None: #meaning the file was successfully read
    #it calls the count_characters function to count the repetitions of each letter and number
    character_count = count_characters(file_content)
    print("Number of repetitions of each letter and number:")
    
    #print the count of each letter in alphabetical order
    for char in sorted(character_count.keys()):
        count = character_count.get(char, 0)  # Get the count for the character
        print(f"{char}: {count}")