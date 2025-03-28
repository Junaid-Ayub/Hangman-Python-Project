import random


def hangman():
    words = ["apple", "banana", "orange", "grape", "melon", "pear"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the fruit name before you run out of attempts.\n")

    while attempts > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)

        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word:", secret_word)
            return


        guess = input("Guess a letter: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue


        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")

        print(f"Guessed letters: {', '.join(guessed_letters)}\n")

    print(f"Game over! The word was: {secret_word}")


hangman()