import streamlit as st

# Function to generate bot response
def get_bot_response(user_input):
    # You can implement your own logic here to generate bot responses
    bot_response = "Hello! how can i help you"
    return bot_response

# Custom CSS styling
st.markdown(
    """
    <style>
    /* Add some padding and background color to the main container */
    .stApp {
        padding: 1rem;
        background-color: black; /* Change background color to black */
    }
    /* Style the title */
    .title h1 {
        color: #333;
        text-align: center;
    }
    /* Style the text input */
    .stTextInput > div > div > input {
        border-radius: 1rem;
        border: 1px solid #ddd;
        padding: 0.5rem;
        background-color: grey; /* Change background color to grey */
    }
    /* Style the submit button */
    .stButton button {
        border-radius: 1rem;
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 0.5rem 1rem;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #45a049; /* Darker Green */
    }
    /* Style the bot response text area */
    .stTextArea textarea {
        border-radius: 1rem;
        border: 1px solid #ddd;
        padding: 0.5rem;
        background-color: #888; /* Change background color to grey */
        color: green; /* Change text color to green */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit UI components
st.title("Chatbot")

# Text input for user to type messages
user_input = st.text_input("Enter your message here:")

# Button to submit the message
submit_button = st.button("Send")

# Display bot response when button is clicked
if submit_button:
    bot_response = get_bot_response(user_input)
    st.text_area("Bot's Response:", value=bot_response, height=60, max_chars=None)
