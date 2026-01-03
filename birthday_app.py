import streamlit as st
import time

# 1. Set page config
st.set_page_config(page_title="HBD 21!", page_icon="💖", layout="centered")

# 2. Advanced CSS for Animated Background and Floating Hearts
st.markdown("""
    <style>
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fad0c4, #ffd1ff);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Glowing Title Effect */
    .glow-text {
        color: white;
        text-align: center;
        font-size: 50px !important;
        text-shadow: 2px 2px 4px #000000;
        font-family: 'Comic Sans MS', cursive;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    /* Custom Button Style */
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 50px;
        border: 2px solid white;
        padding: 10px 24px;
        font-size: 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #ff4b4b;
        border: 2px solid #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Logic for the Surprise
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

# --- SCREEN 1: THE TEASE ---
if not st.session_state.clicked:
    st.markdown("<h1 class='glow-text'>🎁 A Secret Message...</h1>", unsafe_allow_html=True)
    st.write("---")
    st.write("### Hi Beautiful, I built something just for you.")
    st.write("Since it's your **21st**, a regular text message wasn't enough.")
    st.button("CLICK TO UNLOCK YOUR SURPRISE 🔓", on_click=click_button)

# --- SCREEN 2: THE CELEBRATION ---
else:
    # Trigger Animations
    st.balloons()
    time.sleep(1) # Small delay for effect
    st.snow()
    
    st.markdown("<h1 class='glow-text'>🎉 HAPPY 21st BIRTHDAY! 🎉</h1>", unsafe_allow_html=True)
    
    # Optional: Add a YouTube link to her favorite song (it will play in the background)
    st.video("https://www.youtube.com/watch?v=Kz0vK2M9Wsc", start_time=0) # Example: Happy Birthday song
    
    st.write("---")
    
    # Create Columns for a nicer layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("🥂 Cheers!")
        st.write("""
        You're officially 21! 
        I'm so lucky to be by your side 
        as you start this new chapter.
        """)
        
    with col2:
        st.header("💖 My Wish")
        st.write("""
        I hope today is full of 
        love, laughter, and maybe 
        a few cocktails! 🍸
        """)

    st.write("---")
    
    # Interactive "Gift Reveal"
    with st.expander("🕵️‍♀️ WHERE IS YOUR GIFT?"):
        st.write("### Go check the [Location Name] right now!")
        st.write("I hope you love it as much as I love you.")
    
    # Progress Bar as a "Love Meter"
    st.write("My Love Level for you:")
    bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        bar.progress(percent_complete + 1)
    st.write("Error: Love level exceeded 100%! ❤️🚀")
