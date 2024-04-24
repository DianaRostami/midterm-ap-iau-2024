#text-midterm

#read_text_file function takes an input parameter called file_path, which represents the path to a text file.
#open() allows us to open a file in read mode
#encoding='utf-8' indicates that we're opening the file in UTF-8 format

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()


    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error", e)

#Select the file
file_path = "input.txt"

#Call the function to read the file
read_text_file(file_path)
