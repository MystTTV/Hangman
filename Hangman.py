secret_word = input("enter a word to play Hangman\n")
secret_word_converted = []
for letter in secret_word:
    secret_word_converted += letter
guess_counter = 0
guess = []
for letter in secret_word:
    guess += "_"
temp = 0
guessed_right = False
def draw_hangman(guesses):
    if guesses == 0:
        print("  +---+")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif guesses == 1:
        print("  +---+")
        print("  |   |")
        print("  o   |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif guesses == 2:
        print("  +---+")
        print("  |   |")
        print("  o   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("=========")
    elif guesses == 3:
        print("  +---+")
        print("  |   |")
        print("  o   |")
        print(" /|   |")
        print("      |")
        print("      |")
        print("=========")
    elif guesses == 4:
        print("  +---+")
        print("  |   |")
        print("  o   |")
        print(" /|\  |")
        print("      |")
        print("      |")
        print("=========")
    elif guesses == 5:
        print("  +---+")
        print("  |   |")
        print("  o   |")
        print(" /|\  |")
        print(" /    |")
        print("      |")
        print("=========")
    elif guesses == 6:
        print("  +---+")
        print("  |   |")
        print("  o   |")
        print(" /|\  |")
        print(" / \  |")
        print("      |")
        print("=========")
        i = 0
        ans = ""
        return("sorry you lost")

while  guess != secret_word_converted:
    guess_letter = input("guess one letter or type word if you would like to guess the word\n")
    if guess_letter == "word":
        user_word_guess = input("what do you think the word it?\n")
        if user_word_guess == secret_word:
            print("you are correct good job")
            quit()
        else:
            print("yea that wasn't even close nice try though I guess")
            quit()
    else:
        print(guess)
        guessed_right = False
        for letter in secret_word:
            if(guess_letter == letter):
                temp = secret_word.index(letter)
                guess[temp] = letter
                guessed_right = True
        if guessed_right == False:
            guess_counter += 1
        draw_hangman(guess_counter)
        print(guess)
print("nice one")





