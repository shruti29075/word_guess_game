import streamlit as st
from .logic import choose_word, check_letter, is_word_complete
from .database import add_score, get_top_scores

def render_ui():
    st.title("🔠 Word Guesser Game")
    st.caption("Guess the hidden word, one letter at a time!")

    # Initialize session state
    if "secret" not in st.session_state:
        st.session_state.secret = choose_word()
        st.session_state.guessed = []
        st.session_state.attempts = 0
        st.session_state.input_letter = ""
        st.session_state.name_saved = False  # tracks if score saved

    def process_letter():
        letter = st.session_state.input_letter.lower()
        if letter and letter not in st.session_state.guessed:
            st.session_state.guessed.append(letter)
            st.session_state.attempts += 1
        st.session_state.input_letter = ""  # clear input box

    # Text input with on_change
    st.text_input("Enter a letter:", key="input_letter", max_chars=1, on_change=process_letter)

    # Display current progress
    progress = check_letter(st.session_state.secret, st.session_state.guessed)
    st.header(progress)

    # Check game status
    if is_word_complete(st.session_state.secret, st.session_state.guessed):
        st.success(f"🎉 You guessed it! The word was '{st.session_state.secret}'")

        if not st.session_state.name_saved:
            name = st.text_input("Enter your name for leaderboard:", key="name_input")
            if name and st.button("Save Score"):
                add_score(name, st.session_state.attempts)
                st.success("🏅 Score saved!")
                st.session_state.name_saved = True  # mark as saved

        # Reset game button
        if st.session_state.name_saved and st.button("Play Again"):
            st.session_state.secret = choose_word()
            st.session_state.guessed = []
            st.session_state.attempts = 0
            st.session_state.name_saved = False

    st.divider()
    st.subheader("🏆 Top 5 Players")
    for i, (name, score) in enumerate(get_top_scores(), 1):
        st.write(f"{i}. {name} — {score} attempts")