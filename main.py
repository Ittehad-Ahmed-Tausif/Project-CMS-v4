import streamlit as st
from login_signup import login_signup # import the login_signup class from the login_signup.py file
# import ezsheets
# import pandas   

st.title("Login or Sign Up") # Set the title of the page
st.sidebar.title("Project CMS") # Set the Side menu
page = st.sidebar.radio("## Menu", ["Login", "Create an account"])  # Create a radio button for page selection
              
# Page routing logic
if page == "Login":
    login_signup.login()
elif page == "Create an account":
    login_signup.create_an_account()
elif page == "forgot_password":
    login_signup.forgot_password()