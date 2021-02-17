import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


if __name__ == '__main__':
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lifes = 5
    while len(word_letters) > 0 and lifes > 0:
        # show what the user already tried
        print(f"You have {lifes} lifes left\nYou have used the letters: ", ", ".join(used_letters))

        # what the user have guessed
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("\nCurrent word: ", " ".join(word_list))

        # get the input
        user_input = input("\nGuess a letter: ").upper()

        # checks if the letter is in the alphabet and if it was not already tried
        if user_input in alphabet - used_letters:
            # add the letter to the used letters
            used_letters.add(user_input)

            # if the letter is in the word, we remove from the word_letters that are still remaining
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lifes -= 1
                "Not today!\n"

        # checks if the letter is repeated
        elif user_input in used_letters:
            print("You have already guessed this letter!")
        else:
            print("Type a valid character!")

    print(f"The word was {word}.")
    if lifes > 0:
        print("You won!")
    else:
        print("Try one more time!")