import sqlite3 as sq
import hashlib as hs
import streamlit as st

conn = sq.connect('data.db')
c = conn.cursor()
def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS userTable(username TEXT, pass TEXT)')

def add_UserData(username,passw):
    c.execute('INSERT INTO userTable(username,pass) VALUES (?, ?)',(username,passw))
    conn.commit()

def loginUser(username, passw):
    c.execute('SELECT * FROM usertable WHERE username = ? AND pass=?',(username,passw))
    data=c.fetchall()
    return data


# for making our pass more secure we will encrypt our data

def makeHashes(passw):
    return hs.sha256(str.encode(passw)).hexdigest()

def checkHashes(passw, hashText):
    if makeHashes(passw)==hashText:
        return hashText
    return False


# Adding signup section
choice=""
if choice=='Signup':
    st.subheader("Create an Account")
    newUser = st.text_input('Username')
    newPass = st.text_input('Password')
    if st.button('Signup'):
        createTable()
        add_UserData(newUser, newPass)
        st.success("Account created")

elif choice=="Login":
    user = st.sidebar.text_input('Username')
    passw = st.sidebar.text_input('Password')
    if st.button('Login'):
        hashPass = makeHashes(passw)
        result = loginUser(user,checkHashes(passw, hashPass))
        if result:
            st.write("Welcome")
        else:
            st.write("Please check the credentials")







