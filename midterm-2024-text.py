#text

#We're using this module here to calculate the mean and variance of the counts of vowels and consonants in sentences, paragraphs, and the entire text
import statistics
import matplotlib.pyplot as plt
import string
import re

# Function to count occurrences of each letter and number
def count_chars(text):
    chars_count = {char: text.count(char) for char in string.ascii_letters + string.digits}
    return chars_count

# Function to count words and their occurrences
def count_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.strip(string.punctuation)
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return len(words), word_count

# Function to count sentences and paragraphs
def count_sentences_and_paragraphs(text):
    sentences = re.split(r'[.!?]+', text)
    paragraphs = text.split('\n\n')
    return len(sentences), len(paragraphs)

# Function to count vowels and consonants
def count_vowels_and_consonants(text):
    vowels = 'aeiou'
    vowel_count = sum(text.lower().count(vowel) for vowel in vowels)
    consonant_count = sum(text.lower().count(consonant) for consonant in string.ascii_lowercase if consonant not in vowels)
    return vowel_count, consonant_count

# Function to calculate average and variance of vowels and consonants
def calculate_avg_and_variance(text):
    sentences = re.split(r'[.!?]+', text)
    paragraphs = text.split('\n\n')
    vowels_per_sentence = [sum(1 for char in sentence if char.lower() in 'aeiou') for sentence in sentences if sentence]
    consonants_per_sentence = [sum(1 for char in sentence if char.isalpha() and char.lower() not in 'aeiou') for sentence in sentences if sentence]
    vowels_per_paragraph = [sum(1 for char in paragraph if char.lower() in 'aeiou') for paragraph in paragraphs if paragraph]
    consonants_per_paragraph = [sum(1 for char in paragraph if char.isalpha() and char.lower() not in 'aeiou') for paragraph in paragraphs if paragraph]
    vowels_total = sum(vowels_per_sentence)
    consonants_total = sum(consonants_per_sentence)
    avg_vowels_sentence = sum(vowels_per_sentence) / len(vowels_per_sentence) if vowels_per_sentence else 0
    avg_consonants_sentence = sum(consonants_per_sentence) / len(consonants_per_sentence) if consonants_per_sentence else 0
    avg_vowels_paragraph = sum(vowels_per_paragraph) / len(vowels_per_paragraph) if vowels_per_paragraph else 0
    avg_consonants_paragraph = sum(consonants_per_paragraph) / len(consonants_per_paragraph) if consonants_per_paragraph else 0
    variance_vowels_sentence = sum((vowels - avg_vowels_sentence) ** 2 for vowels in vowels_per_sentence) / len(vowels_per_sentence) if vowels_per_sentence else 0
    variance_consonants_sentence = sum((consonants - avg_consonants_sentence) ** 2 for consonants in consonants_per_sentence) / len(consonants_per_sentence) if consonants_per_sentence else 0
    variance_vowels_paragraph = sum((vowels - avg_vowels_paragraph) ** 2 for vowels in vowels_per_paragraph) / len(vowels_per_paragraph) if vowels_per_paragraph else 0
    variance_consonants_paragraph = sum((consonants - avg_consonants_paragraph) ** 2 for consonants in consonants_per_paragraph) / len(consonants_per_paragraph) if consonants_per_paragraph else 0
    return {
        'avg_vowels_sentence': avg_vowels_sentence,
        'variance_vowels_sentence': variance_vowels_sentence,
        'avg_consonants_sentence': avg_consonants_sentence,
        'variance_consonants_sentence': variance_consonants_sentence,
        'avg_vowels_paragraph': avg_vowels_paragraph,
        'variance_vowels_paragraph': variance_vowels_paragraph,
        'avg_consonants_paragraph': avg_consonants_paragraph,
        'variance_consonants_paragraph': variance_consonants_paragraph,
        'total_vowels': vowels_total,
        'total_consonants': consonants_total
    }

# Function to save data to a text file
def save_to_text(data, filename):
    with open(filename, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

# Function to save data to an Excel file
def save_to_excel(data, filename):
    df = pd.DataFrame.from_dict(data, orient='index', columns=['Value'])
    df.to_excel(filename)

# Function to create a plot of sentence number vs. number of vowels
def plot_vowels_per_sentence(text):
    sentences = re.split(r'[.!?]+', text)
    vowel_counts = [sum(1 for char in sentence if char.lower() in 'aeiou') for sentence in sentences if sentence]
    plt.plot(range(1, len(vowel_counts) + 1), vowel_counts, marker='o', linestyle='-')
    plt.xlabel('Sentence Number')
    plt.ylabel('Number of Vowels')
    plt.title('Number of Vowels per Sentence')
    plt.grid(True)
    plt.show()

# Read the text file
with open('input.txt', 'r') as file:
    text_content = file.read()

# Analyze the text
char_count = count_chars(text_content)
word_count, word_occurrences = count_words(text_content)
sentence_count, paragraph_count = count_sentences_and_paragraphs(text_content)
vowel_count, consonant_count = count_vowels_and_consonants(text_content)
avg_and_variance = calculate_avg_and_variance(text_content)

# Print the analysis results
print("Number of repetitions of each letter and number:")
print(char_count)
print("\nNumber of words and the number of repetitions of each:")
print(f"Total words: {word_count}")
print(word_occurrences)
print("\nNumber of sentences:", sentence_count)
print("\nNumber of paragraphs:", paragraph_count)
print("\nNumber of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print("\nAverage and variance of vowels and consonants:")
for key, value in avg_and_variance.items():
    print(f"{key}: {value}")

# Save the printed output in text and Excel files
output_data = {
    "Number of repetitions of each letter and number": char_count,
    "Number of words": word_count,
    "Word occurrences": word_occurrences,
    "Number of sentences": sentence_count,
    "Number of paragraphs": paragraph_count,
    "Number of vowels": vowel_count,
    "Number of consonants": consonant_count,
    "Average and variance of vowels and consonants": avg_and_variance
}