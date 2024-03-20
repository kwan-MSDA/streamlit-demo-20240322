###############################################################
# import python libraries
###############################################################
import streamlit as st
import random

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Guess a number Chatbot - Demo class | 2024-03-22 HUMA5630 Digital Humanities",
    page_icon="🌞", 
    layout="wide",
    initial_sidebar_state="expanded", 
)

###############################################################
# page content
###############################################################

'''
# Guess a Number - Traditional Chatbot

Streamlit Chat elements: https://docs.streamlit.io/library/api-reference/chat

Streamlit Session state feature: https://docs.streamlit.io/library/advanced-features/session-state
'''

# If want to design a fix number for the answer, then no need use st.session_state
# number_to_guess = 3

# Generate a random number between 1 and 10 as the answer
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 10)

with st.expander("Click here to see the answer"):
    st.write(st.session_state.number_to_guess)

# Start or retrieve session
session_state = st.session_state.get("session_state", {"conversation": []})

# Retrieve conversation from session state
conversation = session_state["conversation"]

messages = st.container(height=500)

# Check if there is no existing conversation
if not conversation:
    # Add default assistant message
    conversation.append(("assistant", "Let's start guessing a number!"))
    for role, content in conversation:
        messages.chat_message(role).write(content)

# React to user input
if prompt := st.chat_input("Let's guess! Input a number here."):
    # Check if the input is a number
    try:
        user_input = int(prompt)
        conversation.append(("user", prompt))

        # Check if the guess is correct
        if user_input == st.session_state.number_to_guess:
            response = "Superb! You guessed the number correctly. A fresh number has been generated. Let's begin another round of guessing right away!"
            # Generate a new random number for the next round
            st.session_state.number_to_guess = random.randint(1, 10)
        elif user_input < st.session_state.number_to_guess:
            response = "Too low! Try again."
        elif user_input > st.session_state.number_to_guess:
            response = "Too high! Try again."
        else:
            response = "Please enter a number."

        # Add assistant response to conversation
        conversation.append(("assistant", response))

    except ValueError:
        response = "Invalid input. Please enter a number (integer)."
        conversation.append(("assistant", response))

    # Update conversation in session state
    session_state["conversation"] = conversation

    # Display conversation history
    for role, content in conversation:
        messages.chat_message(role).write(content)

# Update session state
st.session_state["session_state"] = session_state