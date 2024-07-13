import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def main():
    print("Welcome to the Dice Game!")
    print("You will roll two dice and try to guess the sum.")

    while True:
        # Roll the dice
        die1, die2 = roll_dice()
        total = die1 + die2

        # Ask the player for their guess
        guess = int(input("Guess the sum of the two dice (2-12): "))

        # Validate the guess
        if guess < 2 or guess > 12:
            print("Please enter a guess between 2 and 12.")
            continue

        # Print the result of the roll
        print(f"You rolled a {die1} and a {die2}, totaling {total}.")

        # Determine if the guess is correct
        if guess == total:
            print("Congratulations! Your guess was correct.")
        else:
            print("Sorry, your guess was incorrect.")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()