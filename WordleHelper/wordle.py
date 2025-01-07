from collections import Counter
import time

# Load the words from the text file and put it in a variable
def load_words(language, string_length):
    if language == "1":
        file_name = "english_dict.txt"
    else:
        file_name = "dutch_dict.txt"
    with open(file_name) as word_file:
        valid_words = set(word_file.read().split())
        copy_words = valid_words.copy()
        for word in copy_words:
            if len(word) != string_length:
                valid_words.remove(word)
    return valid_words

def find_words(all_words, input_letters, fixed_letters):
    found_words = []
    for word in all_words:
        if len(fixed_letters) != 0:
            empty = 0
            match = 0
            turn = 0
            for x in fixed_letters:
                if x == "_":
                    empty += 1
                if word[turn] == x:
                    match += 1
                turn += 1
            test = match + empty
        else:
            test = word_count

        if test == word_count:
            count = 0
            for letter in word:
                if letter in input_letters:
                    count += 1
                else:
                    break

            if count == word_count:
                # Add the word to the list of found words if it's a full match
                found_words.append(word)

    return found_words


if __name__ == '__main__':

    # Keep asking for input
    while True:
        language = input("Type 1 for English dictionary, 2 for Dutch dictionary: ")

        # Stop when something is submitted and only contains only letters
        if language == "1" or language == "2":
            break


    # Keep asking for input
    while True:
        string = input("Enter some letters: ")
        alphacheck = string.isalpha()

        # Stop when something is submitted and only contains only letters
        if len(string) > 0 and alphacheck is True:
            break

    # Word count
    while True:
        word_count = input("Word count: ")
        word_count = int(word_count)

        # Stop when something is submitted and only contains only letters
        if word_count > 0:
            break

    # Already estalbished letters
    while True:
        definite_letters = input("Letters which are certainly in the word: ")
        alphacheck = definite_letters.isalpha()

        # Stop when something is submitted and only contains only letters
        if len(definite_letters) > 0 and alphacheck is True:
            break

    # Fixed position
    while True:
        fixed = input("Are there already letters on a fixed position? y/n: ")
        alphacheck = fixed.isalpha()

        # Stop when something is submitted and only contains only letters
        if fixed == "y" or fixed == "n":
            break

    fixed_letters = []
    if fixed == "y":
        print("If you don't know the letter, just hit enter")
        for x in range(1, (word_count + 1)):
            while True:
                character = input("Letter %i: "%x)
                if character == "":
                    fixed_letters.append("_")
                else:
                    fixed_letters.append(character)
                if len(character) < 2:
                    break
        print(fixed_letters)


    # Make the input lowercase so they can match words in the dictionary
    input_letters = string.lower()
    definite_letters = definite_letters.lower()

    # Load the words
    english_words = load_words(language=language, string_length=word_count)

    # Find anagrams with the given letters
    found_words = find_words(english_words, input_letters, fixed_letters)

    if found_words == []:
        print("We couldn't find any words with those letters!")
    else:
        for word in found_words:
            print(word)