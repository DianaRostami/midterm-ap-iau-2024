#text

import pandas as pd

#We're using this module here to calculate the mean and variance of the counts of vowels and consonants in sentences, paragraphs, and the entire text
import statistics

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

#count_words function
def count_words(content):
    """
    Counts the number of words in the given text content and
    returns a dictionary containing the count of each word."""
       
    words = content.split()  # Split the content into words
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count, len(words)

#count_sentences function counts the number of sentences in the given text content
def count_sentences(content):
    # Define a list of sentence-ending punctuation marks
    sentence_enders = ['.', '!', '?']
    sentence_count = 0

    for char in content:
        if char in sentence_enders:
            sentence_count += 1

    return sentence_count

#count_paragraphs function counts the number of paragraphs in the given text content
def count_paragraphs(content):
    # Define paragraph delimiters
    paragraph_delimiters = ['\n\n', '\r\n\r\n']
    paragraph_count = 1  # Default is 1 since the text starts with a paragraph

    for delimiter in paragraph_delimiters:
        paragraph_count += content.count(delimiter)

    return paragraph_count

#count_vowels function counts the number of English vowels in the given text content
def count_vowels(content):
    vowels = 'aeiouAEIOU'
    vowel_count = 0

    for char in content:
        if char in vowels:
            vowel_count += 1

    return vowel_count

#count_silent_letters function counts the number of silent letters (consonants) in the given text content
def count_silent_letters(content):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    silent_letter_count = 0

    for char in content:
        if char in consonants:
            silent_letter_count += 1

    return silent_letter_count



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
        
    # Count words
    word_count, total_words = count_words(file_content)
    print("\nNumber of words", total_words)
    print("Number of repetitions of each word:")
    for word, count in word_count.items():
        print(f"{word}: {count}")
           
    # Count sentences
    sentence_count = count_sentences(file_content)
    print("\nNumber of sentences:", sentence_count)
    
    # Count paragraphs
    paragraph_count = count_paragraphs(file_content)
    print("Number of paragraphs:", paragraph_count)

    # Count vowels
    vowel_count = count_vowels(file_content)
    print("Number of English vowels:", vowel_count)

    # Count silent letters
    silent_letter_count = count_silent_letters(file_content)
    print("Number of silent letters (consonants):", silent_letter_count)

##########################################################################################
# Calculate average and variance of vowels and consonants in a given content
def calculate_average_and_variance(content):
    sentences = content.split('.')  # Split content into sentences
    paragraphs = content.split('\n\n')  # Split content into paragraphs

    vowels_counts = []
    consonants_counts = []

    # For each sentence
    for sentence in sentences:
        vowels_counts.append(count_vowels(sentence))
        consonants_counts.append(count_silent_letters(sentence))

    # For each paragraph
    paragraph_vowels_counts = []
    paragraph_consonants_counts = []
    for paragraph in paragraphs:
        paragraph_vowels_counts.append(count_vowels(paragraph))
        paragraph_consonants_counts.append(count_silent_letters(paragraph))

    # For the whole text
    text_vowels_count = count_vowels(content)
    text_consonants_count = count_silent_letters(content)

    # Calculate average and variance
    vowels_avg = statistics.mean(vowels_counts)
    consonants_avg = statistics.mean(consonants_counts)
    paragraph_vowels_avg = statistics.mean(paragraph_vowels_counts)
    paragraph_consonants_avg = statistics.mean(paragraph_consonants_counts)
    text_vowels_avg = text_vowels_count / len(sentences)
    text_consonants_avg = text_consonants_count / len(sentences)

    vowels_var = statistics.variance(vowels_counts)
    consonants_var = statistics.variance(consonants_counts)
    paragraph_vowels_var = statistics.variance(paragraph_vowels_counts)
    paragraph_consonants_var = statistics.variance(paragraph_consonants_counts)

    return (vowels_avg, consonants_avg, vowels_var, consonants_var,
            paragraph_vowels_avg, paragraph_consonants_avg, paragraph_vowels_var, paragraph_consonants_var,
            text_vowels_avg, text_consonants_avg)


if file_content is not None: #meaning the file was successfully read
    # it calls the count_characters function to count the repetitions of each letter and number
    character_count = count_characters(file_content)
    print("Number of repetitions of each letter and number:")
    
    # print the count of each letter in alphabetical order
    for char in sorted(character_count.keys()):
        count = character_count.get(char, 0)  # Get the count for the character
        print(f"{char}: {count}")
        
    # Count words
    word_count, total_words = count_words(file_content)
    print("\nNumber of words", total_words)
    print("Number of repetitions of each word:")
    for word, count in word_count.items():
        print(f"{word}: {count}")
           
    # Count sentences
    sentence_count = count_sentences(file_content)
    print("\nNumber of sentences:", sentence_count)
    
    # Count paragraphs
    paragraph_count = count_paragraphs(file_content)
    print("Number of paragraphs:", paragraph_count)

    # Count vowels
    vowel_count = count_vowels(file_content)
    print("Number of English vowels:", vowel_count)

    # Count silent letters
    silent_letter_count = count_silent_letters(file_content)
    print("Number of silent letters (consonants):", silent_letter_count)

    # Calculate average and variance of vowels and consonants
    (vowels_avg, consonants_avg, vowels_var, consonants_var,
     paragraph_vowels_avg, paragraph_consonants_avg, paragraph_vowels_var, paragraph_consonants_var,
     text_vowels_avg, text_consonants_avg) = calculate_average_and_variance(file_content)
    
    print("\nAverage number of vowels per sentence:", vowels_avg)
    print("Variance of vowels per sentence:", vowels_var)
    print("Average number of consonants per sentence:", consonants_avg)
    print("Variance of consonants per sentence:", consonants_var)

    print("\nAverage number of vowels per paragraph:", paragraph_vowels_avg)
    print("Variance of vowels per paragraph:", paragraph_vowels_var)
    print("Average number of consonants per paragraph:", paragraph_consonants_avg)
    print("Variance of consonants per paragraph:", paragraph_consonants_var)

    print("\nAverage number of vowels in the entire text:", text_vowels_avg)
    print("Average number of consonants in the entire text:", text_consonants_avg)

 # Save to text file
    with open("output.txt", "w") as text_file:
        text_file.write("Number of repetitions of each letter and number:\n")
        for char in sorted(character_count.keys()):
            count = character_count.get(char, 0)  # Get the count for the character
            text_file.write(f"{char}: {count}\n")
        
        text_file.write("\nNumber of words " + str(total_words) + "\n")
        text_file.write("Number of repetitions of each word:\n")
        for word, count in word_count.items():
            text_file.write(f"{word}: {count}\n")
           
        text_file.write("\nNumber of sentences: " + str(sentence_count) + "\n")
        text_file.write("Number of paragraphs: " + str(paragraph_count) + "\n")
        text_file.write("Number of English vowels: " + str(vowel_count) + "\n")
        text_file.write("Number of silent letters (consonants): " + str(silent_letter_count) + "\n")
        
        text_file.write("\nAverage number of vowels per sentence: " + str(vowels_avg) + "\n")
        text_file.write("Variance of vowels per sentence: " + str(vowels_var) + "\n")
        text_file.write("Average number of consonants per sentence: " + str(consonants_avg) + "\n")
        text_file.write("Variance of consonants per sentence: " + str(consonants_var) + "\n")

        text_file.write("\nAverage number of vowels per paragraph: " + str(paragraph_vowels_avg) + "\n")
        text_file.write("Variance of vowels per paragraph: " + str(paragraph_vowels_var) + "\n")
        text_file.write("Average number of consonants per paragraph: " + str(paragraph_consonants_avg) + "\n")
        text_file.write("Variance of consonants per paragraph: " + str(paragraph_consonants_var) + "\n")

        text_file.write("\nAverage number of vowels in the entire text: " + str(text_vowels_avg) + "\n")
        text_file.write("Average number of consonants in the entire text: " + str(text_consonants_avg) + "\n")

    # Save to Excel file
    data = {
        "Statistic": ["Average", "Variance"],
        "Vowels per sentence": [vowels_avg, vowels_var],
        "Consonants per sentence": [consonants_avg, consonants_var],
        "Vowels per paragraph": [paragraph_vowels_avg, paragraph_vowels_var],
        "Consonants per paragraph": [paragraph_consonants_avg, paragraph_consonants_var],
        "Vowels in entire text": [text_vowels_avg, "N/A"],
        "Consonants in entire text": [text_consonants_avg, "N/A"]
    }

    df = pd.DataFrame(data)
    df.to_excel("output.xlsx", index=False)