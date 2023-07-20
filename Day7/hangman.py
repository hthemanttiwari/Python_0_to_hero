# Hangman Project Guessing the word.

#Importing Libraries
import random
from hangman_words import word_list
from hangman_art import logo, stages

# Randomly Choosing a word from word list and taking length
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Setting end game to false and number of lives to 6
end_of_game = False
lives = 6

# Printing logo of out Game.
print(logo)


# Creating Blanks
display = []
for _ in range(word_length):
    display += "_"
# This will create a list like this. Till the length of chosen_word. If the length is 5 it will be like,
# display = ['_', '_', '_', '_', '_']



# Running the while loop till the end_of_game is not True
while not end_of_game:

    # Asking for user to input a word and converting it to lower case
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, printing to letter to let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
    

    # Checking the guessed letter in choosen_word. If the letter is present updating the same in display.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if the guessed letter is not in the choosen word. 
    # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    # And reducing the life of the user.
    # If user run out of lives (lives = 0) making the user lose the game.
    if guess not in chosen_word:
        print (f"You guessed {guess}, that is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print("The word was " + chosen_word)

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Printing the stage of lives. No. of Lives Left.
    print(stages[lives])

    # Check if user has got all letters. He wins.
    if "_" not in display:
        end_of_game = True
        print("You win.")