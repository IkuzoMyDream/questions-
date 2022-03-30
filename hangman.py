import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from a list
    while '-' in word or ' ' in word:  # dont need - or blanks in thi =s word
        word = random.choice(words)
    return word.upper()


def hang_man():
    word = get_valid_word(words)  # random words
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has gussed
    lives = 6
    print(word)
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join['a','b','cd'] --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is
        word_list = [ letter if letter in used_letters else '-' for letter in word ]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('\nGuess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1

        elif user_letter in used_letters:
            print('You have already used that character, Pleas try again.')

        else:
            print('Invalid character, please try again.')

    if lives == 0:
        print('You died, sorry. Tha word was', word)
    else:
        print('Yay you guessed the word, REJECT !!')


hang_man()
