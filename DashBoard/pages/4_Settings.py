import streamlit as st
import pymongo

cluster = pymongo.MongoClient("mongodb+srv://gurleen2113:parika13@cluster0.70n9crp.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Authentication"]
collection = db["Admin"]
name=[]
# document = collection.find_one()
# for result in document:
#     name.append(document['Username'])

column_name = 'Username'
result = collection.distinct(column_name)

# Print the retrieved entries
for entry in result:
    name.append(entry)

#db2=cluster["Authentication"]
collection2=db["Users"]

name_u=[]
column_name_u = 'Username'
result_u = collection2.distinct(column_name_u)
for entry_u in result_u:
    name_u.append(entry_u)

#db3=cluster["Authentication"]
collection3=db["Managers"]

name_m=[]
column_name_m = 'Username'
result_m = collection3.distinct(column_name_m)
for entry_m in result_m:
    name_m.append(entry_m)


t1, t2, t3 = st.tabs(['       👤       Manage Admin     ','       💻        Manager           ','     👥       Manage User      '])

def admin():
    a1, a2, a3 = st.tabs(['     ➕👤    Add Admin      ','       ➖👤    Delete Admin     ', '    📄👤    View Admins     '])

    with a1:
        name_ad=st.text_input("Name",key="name_ad")
        email_ad=st.text_input("Email",key="email_ad")
        username = st.text_input("Username", key="name")
        password = st.text_input("Password", key= "password",type="password")
        c_password = st.text_input("Confirm Password", key= "password_c",type="password")
        add = st.button("Add Admin")

        if add:
            if password == c_password:
                post = {"Name":name_ad,"Email":email_ad,"Username": username, "Password": password}
                collection.insert_one(post)
                st.success("Admin added successfully!")
            else:
                st.error("Passwords do not match")


    # col1 ,col2, col3=st.columns(3)
    # with col1:
    #     if st.button("Add Admin"):
    #         st.write("Add")
    # with col2:
    #     if st.button("Delete Admin"):
    #         st.write("Delete")
    # with col3:
    #     if st.button("View Admin"):
    #         st.write("View")

    with a2:
        username = st.text_input("Username", key="name2")
        dele = st.button("Delete Admin")

        if dele:
            delete_filter = {'Username': username}
            collection.delete_one(delete_filter)
            st.success("Admin deleted successfully!")

    with a3:
        st.write(name)

def manager():
    u1, u2, u3 = st.tabs(['    ➕👥   Add Manager     ','     ➖👥   Delete Manager    ', '    📄👥   View Manager    '])

    with u1:
        username_m = st.text_input("Username", key="name_ma")
        password_m = st.text_input("Password", key= "password_ma",type="password")
        c_password_m = st.text_input("Confirm Password", key= "password_mac",type="password")
        add_u = st.button("Add Manager")

        if add_u:
            if password_m == c_password_m:
                post_m = {"Username": username_m, "Password": password_m}
                collection3.insert_one(post_m)
                st.success("Manager added successfully!")
            else:
                st.error("Passwords do not match")

    with u2:
        username_m = st.text_input("Username", key="name2_ma")
        dele_m = st.button("Delete Manager")
        #st.button("Delete User")

        if dele_m:
            delete_filter_m = {'Username': username_m}
            collection3.delete_one(delete_filter_m)
            st.success("Manager deleted successfully!")

    with u3:
        #st.write(name)
        st.write(name_m)

def user() :
    u1, u2, u3 = st.tabs(['     ➕👥     Add User      ','       ➖👥     Delete User     ', '    📄👥     View Users     '])

    with u1:
        name_us=st.text_input("Name",key="name_user")
        username_u = st.text_input("Username", key="name_u")
        password_u = st.text_input("Password", key= "password_u",type="password")
        c_password_u = st.text_input("Confirm Password", key= "password_uc",type="password")
        add_u = st.button("Add User")

        if add_u:
            if password_u == c_password_u:
                post_u = {"Name":name_us,"Username": username_u, "Password": password_u}
                collection2.insert_one(post_u)
                st.success("User added successfully!")
            else:
                st.error("Passwords do not match")


    # col1 ,col2, col3=st.columns(3)
    # with col1:
    #     if st.button("Add Admin"):
    #         st.write("Add")
    # with col2:
    #     if st.button("Delete Admin"):
    #         st.write("Delete")
    # with col3:
    #     if st.button("View Admin"):
    #         st.write("View")

    with u2:
        username_u = st.text_input("Username", key="name2_u")
        dele_u = st.button("Delete User")
        #st.button("Delete User")

        if dele_u:
            delete_filter_u = {'Username': username_u}
            collection2.delete_one(delete_filter_u)
            st.success("User deleted successfully!")

    with u3:
        #st.write(name)
        st.write(name_u)

with t1:
    #st.write('     Dashboard    ')
    mac1, mac2,mac3 = st.columns([1,10,1])
    with mac1:
        st.empty()
    with mac2:
        st.title('      Manage Admin      ')
    with mac3:
        st.empty()
    admin()
with t2:
    mac1, mac2,mac3 = st.columns([1,10,1])
    with mac1:
        st.empty()
    with mac2:
        st.title('      Manager Info      ')
    with mac3:
        st.empty()
    manager()
with t3:
    mac1, mac2,mac3 = st.columns([1,10,1])
    with mac1:
        st.empty()
    with mac2:
        st.title('      Manage User      ')
    with mac3:
        st.empty()
    user()

