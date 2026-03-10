import streamlit as st
import random as rd

if "wins" not in st.session_state:
    st.session_state.wins = 0
if "losses" not in st.session_state:
    st.session_state.losses = 0
if "draws" not in st.session_state:
    st.session_state.draws = 0
if "round_count" not in st.session_state:
    st.session_state.round_count = 0
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Easy"
if "rounds" not in st.session_state:
    st.session_state.rounds = 5
st.sidebar.title("Game Settings")


Choices = ["Rock", "Paper", "Scissors"]

for var, default in [("wins",0), ("losses",0), ("draws",0), ("round_count",0), ("difficulty","Medium"), ("rounds",3)]:
    if var not in st.session_state:
        st.session_state[var] = default

menu = st.sidebar.radio( "Navigation" , ["Home", "Play Game", "Settings", "About"])
if menu == "Home":
    st.write("Welcome to the Rock Paper Scissors Game! Use the sidebar to navigate through the game and settings.")




elif menu == "Play Game":
    st.title("Rock Paper Scissors Game")
    
    # Scoreboard
    st.subheader("Scoreboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Wins", st.session_state.wins)
    col2.metric("Losses", st.session_state.losses)
    col3.metric("Draws", st.session_state.draws)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Round", st.session_state.round_count)
    col2.metric("Total Rounds", st.session_state.rounds)
    col3.metric("Difficulty", st.session_state.difficulty)
    
    # Player move
    choice = st.selectbox("Choose your move:", ["Choose your move"] + Choices)
    
    # Play button
    if st.session_state.round_count < st.session_state.rounds:
        if st.button("Play"):
            if choice == "Choose your move":
                st.warning("Please select a move to play the game.")
            else:
                # Determine computer move
                difficulty = st.session_state.difficulty
                if difficulty == "Easy":
                    computer_choice = rd.choice(Choices)
                elif difficulty == "Medium":
                    computer_choice = rd.choices(Choices, weights=[0.5,0.3,0.2])[0]
                else:  # Hard
                    # Always tries to beat the player
                    if choice == "Rock":
                        computer_choice = "Paper"
                    elif choice == "Paper":
                        computer_choice = "Scissors"
                    else:
                        computer_choice = "Rock"
                
                st.write(f"Computer chose: {computer_choice}")
                
                # Update scores immediately
                if choice == computer_choice:
                    st.session_state.draws += 1
                    st.warning("It's a draw!")
                elif (choice == "Rock" and computer_choice == "Scissors") or \
                     (choice == "Paper" and computer_choice == "Rock") or \
                     (choice == "Scissors" and computer_choice == "Paper"):
                    st.session_state.wins += 1
                    st.success("You win!")
                else:
                    st.session_state.losses += 1
                    st.error("You lose!")
                
                st.session_state.round_count += 1
    
    # Reset button
    if st.session_state.round_count >= st.session_state.rounds:
        st.error("Maximum rounds reached! Please reset the score to play again.")
    
    if st.button("Reset Score"):
        st.session_state.wins = 0
        st.session_state.losses = 0
        st.session_state.draws = 0
        st.session_state.round_count = 0
        st.success("Score has been reset!")
       
    
elif menu == "Settings":
    st.title("Game Settings")
    st.session_state.difficulty = st.selectbox(
        "Select Difficulty", ["Easy", "Medium", "Hard"], index= ["Easy", "Medium", "Hard"].index(st.session_state.difficulty)
        
        )
    

    st.session_state.rounds = st.slider(
        "Number of Rounds",
        min_value=1,
        max_value=10,
        value=st.session_state.rounds
    )
    

    theme = st.color_picker("Theme Color")

    tips = st.checkbox("Show Tips", value=False)
    if tips:
       st.info("Tips: Rock beats Paper!")

    if st.button("Reset Score"):
        st.session_state.wins = 0
        st.session_state.losses = 0
        st.session_state.draws = 0
        st.session_state.round_count = 0
        st.success("Score has been reset!")

    

elif menu == "About":
    st.title("About This Game")
    st.header("Use Case")
    st.write("This app allows users to play a simple Rock Paper Scissors game against the computer.")

    st.header("Target Users")
    st.write("This game is designed for anyone who wants to play a quick game of Rock Paper Scissors against the computer.")

    st.header("Inputs Collected")
    st.markdown("""
    - Player Move (Rock, Paper, Scissors)
    - Computer Move (Randomly Generated)
    """)

    st.header("Outputs Displayed")
    st.markdown("""
    - Computer's Move
    - Game Result (Win, Lose, Draw)
    -Score Statistics """)





   


    