# Wordle: Working with files
# Coban, Omer Furkan
# SoSe 24/25
# CS4Science - Team B2

# Function to read all 5-letter words from file
def read_wordlist(filename):
    wordlist = []
    f = open(filename, "r", encoding="utf-8")
    for line in f:
        w = line.strip()
        if len(w) == 5:
            wordlist.append(w)
    f.close()
    return wordlist

# Function to choose a "random" word based on user input length
def choose_random_word(wordlist):
    print("Please type any random text (for random selection):")
    user_text = input()
    number = len(user_text)
    if len(wordlist) == 0:
        print("Wordlist is empty!")
        return ""
    index = number % len(wordlist)
    word = wordlist[index]
    return word

# Function to add a new word to file if it is not there
def append_word_to_file(filename, word):
    found = False
    f = open(filename, "r", encoding="utf-8")
    for line in f:
        if line.strip() == word:
            found = True
            break
    f.close()
    if found:
        print(word + " already in file.")
        return False
    if len(word) != 5:
        print(word + " is not a 5 letter word!")
        return False
    f = open(filename, "a", encoding="utf-8")
    f.write(word + "\n")
    f.close()
    print(word + " added to file.")
    return True

# Function to check if word is in wordlist, if not ask to add
def word_check(word, wordlist, filename):
    if len(word) != 5:
        print(word + " is not a 5 letter word! Choose another word")
        return False
    if word not in wordlist:
        print(word + " is not in the list. Add to list? (y/n)")
        answer = input()
        if answer == "y":
            wordlist.append(word)
            append_word_to_file(filename, word)
            print(word + " added to list.")
            return True
        else:
            print(word + " not added.")
            return False
    print(word + " is OK (already in list).")
    return True

# Compare guess and secret, mark +, o, -
def compare_words(guess, secret):
    result = ["-"] * 5
    s = []
    for i in range(5):
        s.append(secret[i])
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = "+"
            s[i] = " " # Mark as used
    for i in range(5):
        if result[i] == "-":
            for j in range(5):
                if guess[i] == s[j]:
                    result[i] = "o"
                    s[j] = " "
                    break
    return result

# Main program
if __name__ == "__main__":
    filename = "wordlewordsinLines.txt"
    # Read file
    words = read_wordlist(filename)
    print("Words loaded:", len(words))
    # Pick a random word
    secret = choose_random_word(words)
    print("Secret word is:", secret)  # (for demo)

    # Test section
    print(compare_words("cbaab", "abbac"))  # Should print: ['o', '+', 'o', '+', 'o']
    print(compare_words("abbac", "abbac"))  # Should print: ['+', '+', '+', '+', '+']
    print(compare_words("xyzgw", "abced"))  # Should print: ['-', '-', '-', '-', '-']

    # Try adding or checking words
    testwords = ["", "apple", "qqqqq", "quick", "looooong"]
    for w in testwords:
        word_check(w, words, filename)
# Test
    guess = input("Your guess: ")
    while not word_check(guess, words, filename):
        guess = input("Your guess: ")
    print(compare_words(guess, secret))


    # Try adding new word directly
    append_word_to_file(filename, "zzzzz")