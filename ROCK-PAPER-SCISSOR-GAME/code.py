import random

def welcome_page():
    print("=====================================")
    print("|       WELCOME TO RPS GAME         |")
    print("|  RPS: ROCK, PAPER, SCISSORS GAME  |")
    print("|         RULES ARE SIMPLE          |")
    print("|   COMPUTER WILL GUESS ONE MOVE    |")
    print("|        YOU GUESS ONE MOVE         |")
    print("|    BEST OF THREE WILL DECIDE      |")
    print("=====================================")

    

    
def check(user_guess, computer_guess):
    if user_guess == computer_guess:
        return "DRAW!!"
    elif user_guess == "rock" and computer_guess == "scissors":
        return "YOU WIN!!"
    elif user_guess == "scissors" and computer_guess == "paper":
        return "YOU WIN!!"
    elif user_guess == "paper" and computer_guess == "rock":
        return "YOU WIN!!"
    else:
        return "YOU LOSE!!"


    
def game():
   
   
    
    options = ["rock", "paper", "scissors"]
    computer_score = 0
    player_score = 0
    count = 0
    while count < 3:
        try:
            user_guess = input("ENTER THE MOVE: ").lower().strip()
            computer_guess = random.choice(options)
            if user_guess not in options:
                raise ValueError("INVALID MOVE! PLEASE ENTER rock, paper, OR scissors")
            print(f"COMPUTER GUESS: {computer_guess}")
            print(f"YOUR GUESS: {user_guess}")
            
            result = check(user_guess,computer_guess)
            print(f"RESULT: {result}")
            
            if result == "YOU WIN!!":
                player_score += 1
            elif result == "YOU LOSE!!":
                computer_score += 1
                
            count+=1
        except ValueError as e:
            print(f"ERROR!! {e}")
    print("\n=============================")
    print(f"FINAL SCORES:\nPLAYER: {player_score} | COMPUTER: {computer_score}")
    if player_score > computer_score:
        print("🏆 CONGRATULATIONS! YOU ARE THE WINNER! 🏆")
    elif player_score < computer_score:
        print("💻 COMPUTER WINS THIS ROUND! BETTER LUCK NEXT TIME! 💻")
    else:
        print("🤝 IT'S A TIE! WELL PLAYED! 🤝")
    print("=============================")        
            
            
def main():
    welcome_page()
    game()
    
    
if __name__ == "__main__":
    main()