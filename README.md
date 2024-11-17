# guessing-game
USER GUESSING Mode:
The user inputs a start and end range for the number to be guessed.
If the start is greater than end, an error message is displayed.
Once the range is valid, the app generates a random number (number_to_guess) between the start and end range.
The user enters guesses, and the app gives feedback:
If the guess is too low or too high, the user is prompted to try again.
If the guess is correct, the app displays a success message and triggers balloons.
COMPUTER GUESSING Mode:
In this mode, the computer tries to guess a number that the user thinks of, within a specified range.
The user sets the min and max values for the range, and the computer begins with a guess in the middle of the range.
The user indicates whether the guess is correct, too low, or too high.
If the guess is correct, the game ends, and a success message is shown with the number of attempts.
If the guess is incorrect, the range is adjusted (either increase or decrease the range), and the computer makes a new guess.
The game continues until the computer guesses the correct number.
