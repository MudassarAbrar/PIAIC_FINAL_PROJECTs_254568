
#NUMBER GUESSING GAME BY COMPUTER
#USING BINARY APPROACH 


while True:
    lower_range = int(input("ENTER THE LOWER RANGE: "))
    higher_range = int(input("ENTER THE HIGHER RANGE: "))
    if lower_range > higher_range:
        print("ENTER VALID RANGE")
    else:
        break

# Initial guess
computer_guess = (lower_range + higher_range) // 2
print(f"Computer's guess: {computer_guess}")

while True:
    user_reply = input("ENTER 'guess lower', 'guess higher', or 'correct': ").strip().lower()

    if user_reply == "guess lower":
        higher_range = computer_guess - 1  # Update the upper bound
        computer_guess = (lower_range + higher_range) // 2
        print(f"Computer's new guess: {computer_guess}")

    elif user_reply == "guess higher":
        lower_range = computer_guess + 1  # Update the lower bound
        computer_guess = (lower_range + higher_range) // 2
        print(f"Computer's new guess: {computer_guess}")

    elif user_reply == "correct":
        print("Hooray! The computer guessed your number!")
        break

    else:
        print("Invalid input. Please enter 'guess lower', 'guess higher', or 'correct'.")
