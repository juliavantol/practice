from collections import Counter
import time

# Load the words from the text file and put it in a variable
def load_words(string_length):
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
        copy_words = valid_words.copy()
        for word in copy_words:
            if len(word) != string_length:
                valid_words.remove(word)
    return valid_words

def find_words(all_words, input_letters, input_count):
    found_words = []
    for word in all_words:
        check = 0

        # Find out how many times each letter is used
        word_count = Counter(word)

        for letter in input_letters:
            # Find words that have the exact same set of letters
            if letter in word and word_count[letter] == input_count[letter]:
                check += 1

        # Add the word to the list of found words if it's a full match
        if check == len(input_letters):
            found_words.append(word)

    return found_words


if __name__ == '__main__':

    print("Give us some letters and find out what words you can form with it!\n")

    # Keep asking for input
    while True:
        string = input("Enter some letters: ")
        alphacheck = string.isalpha()

        # Stop when something is submitted and only contains only letters
        if len(string) > 0 and alphacheck is True:
            break

    # Make the input lowercase so they can match words in the dictionary
    input_letters = string.lower()

    # Find out how many times each letter is used
    input_count = dict(Counter(input_letters))

    # Load the words
    english_words = load_words(string_length=len(input_letters))

    # Find anagrams with the given letters
    found_words = find_words(english_words, input_letters, input_count)

    if found_words == []:
        print("We couldn't find any words with those letters!")
    else:
        for word in found_words:
            print(word)