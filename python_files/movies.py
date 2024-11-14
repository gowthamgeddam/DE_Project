import streamlit as st
from user import user_dashboard
from admin import admin_dashboard

# Set page configuration and add CSS for custom styling
st.set_page_config(page_title="Movies Dashboard", page_icon=":bar_chart:", layout="wide")

def add_custom_css():
    st.markdown(
        """
        <style>
        /* Background color for the page */
        body {
            background-color: #01172B;
        }
        .header1 {
            padding: 2rem;
            color: white;
            background-color: #4B6587;
            text-align: left;
            width: 100%;
            border-radius: 8px;
        }
        
        /* Centered login form with dark container background */
        .login-container {
            padding: 1rem;
            background-color:01172B;
            border-radius: 8px;
            
            margin: auto;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
        }

        /* Header with light color */
        .header {
            color: #FFFFFF;
            text-align: center;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        /* Styled input fields */
        .stTextInput, .stPasswordInput, .stSelectbox {
            width: 100% !important;
            background-color: #3A3A3A !important;
            color: #FFFFFF !important;
            border-radius: 5px !important;
        }

        /* Styled login button */
        .login-button button {
            background-color: #007ACC !important;
            color: white !important;
            width: 100%;
            padding: 0.5rem 0;
            font-size: 1rem;
            border-radius: 5px;
        }

        /* Error message styling */
        .stAlert {
            background-color: #5C5C5C !important;
            color: #FFC107 !important;
            border-radius: 5px;
            padding: 0.5rem;
            margin-top: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Call function to add custom CSS styling
add_custom_css()

def login():
    st.markdown('<div class="header1"><h1>Movies Dashboard</h1></div>', unsafe_allow_html=True)
    
    # Header
    st.markdown('<div class="login-container"><div class="header"><h2>Login</h2></div></div>', unsafe_allow_html=True)
    
    # Text inputs for username and password with placeholders
    username = st.text_input("Username", placeholder="Enter your username", key="input_username")
    password = st.text_input("Password", type="password", placeholder="Enter your password", key="input_password")
    

    # Login button
    if st.button("Login", key="login_button"):
        if authenticate(username, password):
            # Set session state only upon successful login
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["password"] = password
        else:
            st.error("Please enter your username and password")
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close login-container

def authenticate(username, password):
    # Hardcoded users for example, replace with database check
    users = {"user": "123", "admin": "456"}
    return username in users and users[username] == password 

def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        if st.session_state["password"] == "456" and st.session_state["username"] == "admin":
            admin_dashboard()
        elif st.session_state["password"] == "123" and st.session_state["username"] == "user":
            user_dashboard()
        else:
            login()   
            st.error("Please enter your username and password")
    else:
        login()

if __name__ == "__main__":
    main()


