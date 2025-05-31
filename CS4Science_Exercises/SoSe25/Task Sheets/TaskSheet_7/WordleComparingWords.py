# Wordle: Comparing words
# Coban, Omer Furkan
# SoSe 24/25
# CS4Science - Team B2

# Create a basic word list
wordlist = ["abbac", "abced", "abcxy", "caabx"]

def word_check(word, wordlist):
    # Check if word has 5 letters
    if len(word) != 5:
        print(f"{word} is not a 5 letter word! Choose another word")
        print(f"Word: <{word}> is not feasible.")
        return False
    # Check if word is in list
    if word not in wordlist:
        answer = input(f"{word} is not in the list. Do you want to add it to the list? (y/n)")
        if answer == "y":
            wordlist.append(word)
            print(f"Word: <{word}> is feasible. The list now is {wordlist}")
            return True
        else:
            print(f"{word} does not exist! Choose another word")
            print(f"Word: <{word}> is not feasible.")
            return False
    print(f"Word: <{word}> is feasible. The list now is {wordlist}")
    return True

def compare_words(guess, secret):
    result = ["-"] * 5
    secret_temp = list(secret)

    # Mark correct letters at correct position
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = "+"
            secret_temp[i] = None  # Mark as used

    # Mark correct letters at wrong position
    for i in range(5):
        if result[i] == "-":
            if guess[i] in secret_temp:
                result[i] = "o"
                idx = secret_temp.index(guess[i])
                secret_temp[idx] = None
    return result

# Black box tests
print("Test: Is marking correct?")
print(compare_words("cbaab", "abbac"))  # ['o', '+', 'o', '+', 'o']
print(compare_words("abbac", "abbac"))  # ['+', '+', '+', '+', '+']
print(compare_words("xyzgw", "abced"))  # ['-', '-', '-', '-', '-']
print(compare_words("cbaab", "abcxy"))  # ['o', '+', 'o', '-', '-']
print(compare_words("abcxy", "caabx"))  # ['o', 'o', 'o', 'o', '-']

# Word feasibility tests - try with user input!
test_words = ["", "a", "abcdef", "ababa", "abcxy", "wertz"]
for w in test_words:
    word_check(w, wordlist)

guess = input("Guess a word: ")
secret = "abbac"
print(compare_words(guess, secret))