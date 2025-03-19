import streamlit as st

# Initialize session state variables
if "lower_range" not in st.session_state:
    st.session_state.lower_range = None

if "higher_range" not in st.session_state:
    st.session_state.higher_range = None

if "computer_guess" not in st.session_state:
    st.session_state.computer_guess = None

if "message" not in st.session_state:
    st.session_state.message = ""

if "game_active" not in st.session_state:
    st.session_state.game_active = False

if "user_feedback" not in st.session_state:
    st.session_state.user_feedback = ""

# Input for lower and higher range
st.title("🎯 Number Guessing Game by Computer")
st.write("The computer will try to guess your number!")

st.session_state.lower_range = st.number_input("Enter the lower range:", step=1, min_value=0, key="lower_range_input")
st.session_state.higher_range = st.number_input("Enter the higher range:", step=1, min_value=1, key="higher_range_input")

# Start game button
if st.button("Start Game"):
    if st.session_state.lower_range >= st.session_state.higher_range:
        st.error("Please enter a valid range (lower range should be less than higher range).")
    else:
        st.session_state.game_active = True
        st.session_state.computer_guess = (st.session_state.lower_range + st.session_state.higher_range) // 2
        st.session_state.message = f"Computer's first guess: {st.session_state.computer_guess}"

# Game logic
if st.session_state.game_active:
    st.write(st.session_state.message)

    # User input for feedback
    feedback_options = ["", "guess lower", "guess higher", "correct"]
    st.session_state.user_feedback = st.selectbox(
        "Select your feedback for the computer's guess:",
        options=feedback_options,
        key="user_feedback_select"
    )

    def check_feedback():
        if st.session_state.user_feedback == "guess lower":
            st.session_state.higher_range = st.session_state.computer_guess - 1
        elif st.session_state.user_feedback == "guess higher":
            st.session_state.lower_range = st.session_state.computer_guess + 1
        elif st.session_state.user_feedback == "correct":
            st.success("🎉 Hooray! The computer guessed your number!")
            st.session_state.game_active = False
        else:
            st.warning("Please select a valid feedback option.")

        # Recalculate the guess only if the game is still active
        if st.session_state.game_active:
            st.session_state.computer_guess = (
                st.session_state.lower_range + st.session_state.higher_range
            ) // 2
            st.session_state.message = f"Computer's new guess: {st.session_state.computer_guess}"

    # Submit feedback button
    st.button("Submit Feedback",on_click=check_feedback())
