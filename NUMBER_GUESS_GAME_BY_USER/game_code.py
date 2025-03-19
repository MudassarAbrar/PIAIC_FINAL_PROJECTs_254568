#NUMBER GUESSING GAME USING RANDOM METHOD
print("---------NUMBER GUESSING GAME----------")
import random
number_of_guesses=0
while True:
    try:
        lowest_limit = int(input("Enter the lowest limit: "))
        highest_limit = int(input("Enter the highest limit: "))
        if lowest_limit > highest_limit:
            raise ValueError("Lowest limit must not be greater than the highest limit.")
        break  # Exit the loop if input is valid
    except ValueError as e:
        print("ERROR:", e)
        print("Please enter the limits again.\n")
    
    
random_number=random.randint(lowest_limit,highest_limit)
while True:
  user_guess=int(input("Enter your guess: "))
  number_of_guesses+=1
  if user_guess>highest_limit or user_guess<lowest_limit :
    print("Invalid guess")
    print("GUESS AGAIN")
  elif user_guess>random_number:
    print("Your guess is too high")
  elif user_guess<random_number:
    print("Your guess is too low")
  elif user_guess==random_number:
    print("You guessed it right")
    print("--------------YOUR RESULT---------------")
    print(  "Number of guesses: ",number_of_guesses)
    if number_of_guesses<5:

      print("🎉 YOU WON! Great job!")
    else:
      print("😞 YOU LOSE! Better luck next time.")
    break