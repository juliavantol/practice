import copy

# Load the words from the text file and put it in a variable
def load_words(string_length):
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
        copy_words = valid_words.copy()
        for word in copy_words:
            if len(word) != string_length:
                valid_words.remove(word)
    return valid_words


if __name__ == '__main__':

    # Keep asking for input
    while True:
        string = input("Enter some letters: ")
        alphacheck = string.isalpha()

        # Stop when something is submitted and only contains only letters
        if len(string) > 0 and alphacheck is True:
            break
    # Make the input lowercase
    letters = string.lower()
    check_list = []
    for one_letter in letters:
        check_list.append(one_letter)

    # Load the words
    english_words = load_words(string_length=len(letters))

    for word in english_words:
        check = 0
        for letter in letters:
            if letter in word:
                check += 1

        if check == len(letters):
            print(word)





