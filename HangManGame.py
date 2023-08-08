import random, hangman_words, hangman_art
import os
clear = lambda: os.system('clear')

#Variables:
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.') #Testing code, helps with debuging


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    #Check if guessed letter is correct
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}") #Helpful for debuging/testing
        if letter == guess:
            display[position] = letter

    #Check if guessed letter is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
