import random, hangman_words, hangman_art #Word list and ascii art are seperated in different files(modules), to keep the main game file cleaner
import os
clear = lambda: os.system('clear')

#Variables:
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
#guessBank = []

print(hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.') #Testing code, helps with debuging

#Loop for creating blanks "_" based on the words length
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game: # While the end_of_game variable is not True, contine with loop
    guess = input("Guess a letter: ").lower()
    clear() # Clears screen

    if guess in display: #Checks to see if Users guessed letter is in the display list, using "in"
        print(f"You've already guessed {guess}")

    #Check if guessed letter is correct
    for position in range(word_length): #Using the chosen words length to asign the index to position
        letter = chosen_word[position] #Using the position Index with the chosen word to asign the letter to the variable letter
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}") #Helpful for debuging/testing
        if letter == guess:
            display[position] = letter #If correct letter is chosen, replaces the blank space with the actual letter in the display list, using position as index

    #Check if guessed letter is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True #Once lives are down to 0, set end_of_game variable to True, which breaks the While Loop
            print("You lose.")

    print(f"{' '.join(display)}") #Join all the elements in the list and turn it into a String.

    #Check if user has got all letters.
    if "_" not in display: #Using "not in" to check that there are no longer any blank spaces, sets the end_of_game variable to true, breaks the While Loop
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])


#Used to check if the user enters the same letter more than once, and to warn them
#It works, however prints the message twice, cleaner solution used
    # guessBank.append(guess)
    # for letter2 in guessBank:
    #     x = guessBank.count(letter2)
    #     if x >= 2:
    #         print(f"You already guessed {letter2}, try a different one!")