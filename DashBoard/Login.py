import streamlit as st
import pymongo
#from streamlit_pages import MultiPage
from datetime import datetime
import os
import Config
#import webbrowser

global cluster
global db
global user
# cluster = pymongo.MongoClient(
#     "mongodb+srv://gurleen2113:parika13@cluster0.70n9crp.mongodb.net/?retryWrites=true&w=majority",serverSelectionTimeoutMS=60000)
# db = cluster["Server"]
# user = db["Users"]
# #serverSelectionTimeoutMS=60000
# def connection():
#     global user
#     cluster = pymongo.MongoClient(
#     "mongodb+srv://gurleen2113:parika13@cluster0.70n9crp.mongodb.net/?retryWrites=true&w=majority")
#     db = cluster["Server"]
#     user = db["Users"]
#     return user
# def open_new_page():
#     url='https://gurleen21-capstoneserverdashboard-app-o649ro.streamlit.app/'
#     webbrowser.open_new_tab(url)
# def home():
#     st.write("Welcome to home page")
#     if st.button("Click Home"):
#         st.write("Welcome to home page")


# def about():
#     st.write("Welcome to about page")
#     if st.button("Click about"):
#         st.write("Welcome to About page")


# def contact():
#     st.write("Welcome to contact page")
#     if st.button("Click Contact"):
#         st.write("Welcome to contact page")
# app = MultiPage()
# app.add_page("Home",home)
# app.add_page("About",about)
# app.add_page("Contact",contact)
# app.run()


st.title("Login")
username = st.text_input("Username", key="name")
password = st.text_input("Password", key= "password",type="password")
login_button = st.button("Login")

is_logged_in = False
if login_button:
    # Add your login logic here
    # results = user.find()
    # for result in results:
    #     print(result['Username'])
        # if username == result['Username'] and password == result['Password']:
    if username == '102003133' and password == 'Admin@123':
        st.success("Logged in successfully!")
        is_logged_in = True
        os.system(f'{Config.Parent}Dashboard_main.py')
            # st.markdown('<a href="https://gurleen21-capstoneserverdashboard-app-o649ro.streamlit.app/" >Go to Dashboard</a>', unsafe_allow_html=True)
    if(is_logged_in == False):
        st.error("Invalid Login")

# def open_new_page():
#     new_page_url = "https://www.google.com/"  # Replace with the desired URL
#     new_page_script = f"""
#     <script type="text/javascript">
#         window.location.href = "{new_page_url}";
#     </script>
#     """
#     st.write(new_page_script, unsafe_allow_html=True)
# def main(user):
#     now = datetime.now()
#     now = now.strftime("%S")
#     now=str(now)
#     if(now==0 or now==00 or now==30):
#         user = connection()
#     is_logged_in = st.session_state.get('is_logged_in', False)
#     login(user)

# if __name__ == "__main__":
#     user = connection()
#     login(user)
#     #main(user)
