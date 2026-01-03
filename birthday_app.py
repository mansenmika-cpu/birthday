import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="A Special Surprise", page_icon="🎂")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #fff0f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎂 Happy 21st Birthday!")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


if not st.session_state.clicked:
    st.write("### I made something small for your big day...")
    st.button("Click to Open Your Surprise", on_click=click_button)
else:
    st.balloons()
    st.header("✨ Cheers to 21 Years! ✨")

    # You can add a photo of you two here
    # st.image("your_photo.jpg", caption="Our favorite memory")

    st.write("""
    To the most amazing girl,

    Happy 21st! You’ve officially unlocked the 'full adulthood' 
    achievement. I am so proud of the person you are. 

    I hope today is as beautiful and bright as your smile.
    """)

    with st.expander("Click here for your gift hint"):
        st.write("Check the glove box of your car! 🎁")

    st.snow()