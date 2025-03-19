import random
import streamlit as st

def welcome_page():
    st.markdown("""
        <div style="text-align: center;">
            <h1>WELCOME TO RPS GAME</h1>
            <h3>RPS: ROCK, PAPER, SCISSORS GAME</h3>
            <p>RULES ARE SIMPLE:</p>
            <p>1. COMPUTER WILL GUESS ONE MOVE</p>
            <p>2. YOU GUESS ONE MOVE</p>
            <p>3. BEST OF THREE WILL DECIDE THE WINNER</p>
        </div>
    """, unsafe_allow_html=True)

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

    st.write("### Play the Game")

    # Persistent session state for tracking game progress
    if 'count' not in st.session_state:
        st.session_state.count = 0
        st.session_state.player_score = 0
        st.session_state.computer_score = 0

    if st.session_state.count < 3:
        st.write(f"#### Round {st.session_state.count + 1}")
        user_guess = st.selectbox("Choose your move:", options, key=f"move_{st.session_state.count}")
      
        def display():
            computer_guess = random.choice(options)
            
            st.write(f"**COMPUTER GUESS:** {computer_guess}")
            st.write(f"**YOUR GUESS:** {user_guess}")

            result = check(user_guess, computer_guess)
            st.write(f"**RESULT:** {result}")

            if result == "YOU WIN!!":
                st.session_state.player_score += 1
            elif result == "YOU LOSE!!":
                st.session_state.computer_score += 1

            st.session_state.count += 1
        st.button("Submit Move",on_click= display())
    else:
        st.write("### Final Scores")
        st.write(f"PLAYER: {st.session_state.player_score} | COMPUTER: {st.session_state.computer_score}")

        if st.session_state.player_score > st.session_state.computer_score:
            st.success("🏆 CONGRATULATIONS! YOU ARE THE WINNER! 🏆")
        elif st.session_state.player_score < st.session_state.computer_score:
            st.error("💻 COMPUTER WINS THIS ROUND! BETTER LUCK NEXT TIME! 💻")
        else:
            st.info("🤝 IT'S A TIE! WELL PLAYED! 🤝")

        if st.button("Play Again"):
            st.session_state.count = 0
            st.session_state.player_score = 0
            st.session_state.computer_score = 0

def main():
    st.set_page_config(page_title="RPS Game", page_icon="⚔️", layout="centered")
    welcome_page()
    game()

if __name__ == "__main__":
    main()
