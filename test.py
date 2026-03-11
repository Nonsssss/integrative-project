import streamlit as st
import random as rd

st.markdown("""
<style>
.stApp {
    background-color: #0F172A;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
div.stButton > button {
    background-color: #F97316;
    color: white;
    border-radius: 10px;
    border: none;

div.stButton > button:hover {
    background-color: #EA580C;
}
}
</style>
""", unsafe_allow_html=True)


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
if "theme" not in st.session_state:
    st.session_state.theme = "#FFFFFF"

st.sidebar.markdown("""<style>
[data-testid="stSidebar"] {
    background-color: #1E293B;
}
</style>
""", unsafe_allow_html=True)
    
st.sidebar.title("Game Settings")


Choices = ["Rock", "Paper", "Scissors"]

for var, default in [("wins",0), ("losses",0), ("draws",0), ("round_count",0), ("difficulty","Medium"), ("rounds",3)]:
    if var not in st.session_state:
        st.session_state[var] = default

menu = st.sidebar.radio( "Navigation" , ["Home", "Play Game", "Settings", "About"])
if menu == "Home":

    col1, col2 = st.columns(2)
    with col1:
            st.image("images/RPS.png", width = 300 )
    with col2:
            st.title("Welcome to Rock Paper Scissors Game!")


    st.write("""
    - Navigate using the sidebar to **Play Game**, adjust **Settings**, or learn more **About** the game.
    - In the **Play Game** section, select your move and see how you fare against the computer. Keep track of your wins, losses, and draws on the scoreboard.
    - Check your **Scoreboard** to see your wins, losses,draws.
    - Use **Settings** to change difficulty and number of rounds.
    - Click **Reset Score** to start fresh and challenge yourself again!
    """)
    
    st.header("Features:")
    st.markdown("""  
    
        - Track wins, losses, and draws immediately after each round.
        - Play multiple rounds with adjustable settings for difficulty and number of rounds.
        - Fun and Interactive UI with Immediate Feedback on Game Results.
    """)

    st.header("How to Play")
    st.write("""    
    1. Select "Play Game" from the sidebar.
    2. Choose your move (Rock, Paper, or Scissors) from the dropdown.
    3. Click the "Play" button to see the computer's move and the result of the round.
    4. Keep track of your wins, losses, and draws on the  scoreboard.
    5. Adjust the difficulty and number of rounds in the "Settings" section to increase the challenge.
    6. Click "Reset Score" to start a new game and see if you can improve your score!
    """)

    st.header("Game Rules")
    st.write("""
    - Rock beats Scissors
    - Scissors beats Paper
    - Paper beats Rock
    - If both players choose the same move, it's a draw.
    """)

    st.header("Difficulty Levels")
    st.write("""
    - **Easy**: Computer chooses moves randomly with equal probability.
    - **Medium**: Computer favors certain moves based on weighted probabilities.
    - **Hard**: Computer always tries to beat the player's move.
    """)





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

    col1, col2, col3 = st.columns(3)
    with col1:
         st.session_state.theme = st.color_picker("", st.session_state.get("theme", "#FFFFFF"), width=5000) 
        

    with col2:
        st.markdown(
        f"<h1 style='color:{st.session_state.theme}; margin:0'>Game Settings</h1>"
        f"</div>", unsafe_allow_html=True)
              
        
    
    st.session_state.difficulty = st.selectbox(
        "Select Difficulty", ["Easy", "Medium", "Hard"], index= ["Easy", "Medium", "Hard"].index(st.session_state.difficulty)
        
        )
    
    
    st.session_state.rounds = st.slider(
        "Number of Rounds",
        min_value=1,
        max_value=10,
        value=st.session_state.rounds
    )
    

    

    tips = st.checkbox("Show Tips", value=False)
    if tips:
       st.info("Tips: Rock beats Paper!")
       Video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
       st.video(Video_url, autoplay = True)

    if st.button("Reset Score"):
        st.session_state.wins = 0
        st.session_state.losses = 0
        st.session_state.draws = 0
        st.session_state.round_count = 0
        st.success("Score has been reset!")

    

elif menu == "About":
    st.title("About This Game")
    st.header("Use Case")
    st.write("This app allows users to play a simple **Rock Paper Scissors** game against the computer.")

    st.header("Target Users")
    st.write("This game is designed for anyone who wants to play a quick game of **Rock Paper Scissors** against the computer.")

    st.header("Inputs Collected")
    st.markdown("""
    - Player Move (Rock, Paper, Scissors)
    - Computer Move (Randomly Generated)
    - Number of Rounds
    """)

    st.header("Outputs Displayed")
    st.markdown("""
    - Computer's Move
    - Game Result (Win, Lose, Draw)
    - Score Statistics """)





   


    