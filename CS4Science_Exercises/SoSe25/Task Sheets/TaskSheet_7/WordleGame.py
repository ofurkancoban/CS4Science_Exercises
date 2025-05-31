# Wordle: use the former scripts as modules and put it all together
# Coban, Omer Furkan
# SoSe 24/25
# CS4Science - Team B2

def read_wordlist(filename):
    wordlist = []
    f = open(filename, "r", encoding="utf-8")
    for line in f:
        w = line.strip()
        if len(w) == 5:
            wordlist.append(w)
    f.close()
    return wordlist

def choose_random_word(wordlist):
    print("Please type any random text (for random selection):")
    user_text = input()
    if len(wordlist) == 0:
        print("Wordlist is empty!")
        return ""
    number = len(user_text)
    index = number % len(wordlist)
    word = wordlist[index]
    return word

def append_word_to_file(filename, word):
    found = False
    f = open(filename, "r", encoding="utf-8")
    for line in f:
        if line.strip() == word:
            found = True
            break
    f.close()
    if found:
        return False
    if len(word) != 5:
        return False
    f = open(filename, "a", encoding="utf-8")
    f.write(word + "\n")
    f.close()
    return True

def compare_words(guess, secret):
    result = ["-"] * 5
    s = []
    for i in range(5):
        s.append(secret[i])
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = "+"
            s[i] = " "  # Mark as used
    for i in range(5):
        if result[i] == "-":
            for j in range(5):
                if guess[i] == s[j]:
                    result[i] = "o"
                    s[j] = " "
                    break
    return result

def is_feasible(word, wordlist):
    # Checks only length and letters, not file adding
    if len(word) != 5:
        return False
    for c in word:
        if not c.isalpha():
            return False
    return True

# --- Main program as in the diagram ---

def main():
    filename = "wordlewordsinLines.txt"
    wordlist = read_wordlist(filename)
    secret = choose_random_word(wordlist)
    trial = 0
    gameWon = False

    while trial < 6 and not gameWon:
        guess = input("\nEnter your guess (5-letter word): ").lower()
        # Step: Is guess feasible?
        if not is_feasible(guess, wordlist):
            print("Invalid guess! Please enter a 5-letter word with only letters.")
            continue  # does NOT increment trial

        trial += 1  # Increment trial counter

        # Is it a new word?
        if guess not in wordlist:
            add_word = input(f"'{guess}' is not in the list. Add to list and file? (y/n): ")
            if add_word.lower() == "y":
                wordlist.append(guess)
                append_word_to_file(filename, guess)
                print(f"'{guess}' added to the list and file.")

        # Compare and show marks
        marks = compare_words(guess, secret)
        print("Result: ", marks)

        # Check win
        if guess == secret:
            gameWon = True

    if gameWon:
        print("\nCongratulations! You guessed the word:", secret)
    else:
        print("\nGame over. The word was:", secret)

if __name__ == "__main__":
    main()