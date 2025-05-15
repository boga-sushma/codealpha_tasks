import random

def hangman():
    # Word list for the game
    word_list = ['python', 'hangman', 'challenge', 'programming', 'code']
    word = random.choice(word_list).lower()
    word_letters = set(word)        # Unique letters in the word
    guessed_letters = set()         # Correct guesses
    wrong_guesses = set()           # Incorrect guesses
    tries = 6                       # Number of allowed incorrect guesses

    print("🎮 Welcome to Hangman!")
    print("_ " * len(word))

    # Game loop
    while len(word_letters) > 0 and tries > 0:
        print(f"\nWord: ", end="")
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print(" ".join(display_word))

        print(f"Wrong guesses: {', '.join(sorted(wrong_guesses))}")
        print(f"Remaining tries: {tries}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("⚠️ You already guessed that letter.")
            continue

        if guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print("✅ Correct!")
        else:
            wrong_guesses.add(guess)
            tries -= 1
            print("❌ Incorrect!")

    # End of game
    if tries == 0:
        print(f"\n💀 You lost! The word was: {word}")
    else:
        print(f"\n🎉 Congratulations! You guessed the word: {word}")

# Run the game
hangman()