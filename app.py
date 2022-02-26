import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

# in order to remove the three lines and the made with streamlit watermark we use below
hideStyle="""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility:hidden;}
    </style>"""

st.set_page_config(page_title="My WebPage",page_icon=":tada:",layout="wide")
st.markdown(hideStyle,unsafe_allow_html=True)

def lott(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottieCode =lott("https://assets10.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# header section
# go to https://www.webfx.com/tools/emoji-cheat-sheet to get the emoji names
st.subheader("Hii, I am Sandeep :wave:")
st.title("A student in the college")
st.write("I am passionate about finding ways to use python")


with st.container():
    st.write("---")
    leftCol,rightCol =st.columns(2)
    with leftCol:
        st.header("What I do")
        st.write("##")
        st.write("""
        I am a student studying in a college
        looking to build the best applications possible""")

        st.write(" You can checkout my works [here](https://youtube.com)")

        # now we are going to add animation using lottie
    with rightCol:
        st_lottie(lottieCode,height=300,key="Coding")

# this below line is used to use break between the section
# st.write("---")

# with st.container():
#     imgCol,textCol=st.columns((1,2))
#     with imgCol:
#         st.write("---")
#         # we can add an image as well using pil

with st.container():
    st.write("---")
    st.header(":mailbox: Get in touch with me")

    contactForm="""
    <form action="https://formsubmit.co/your@email.com" method="POST">
    <p>Name </p><input type="text" name="name" required>
    <p>Email</p>
    <input type="email" name="email" required><br> <br>
    <button type="submit">Submit</button>
    </form>"""
    st.markdown(contactForm,unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("You can contact me from below")
    # now to get the icons of the social header we can use ionicons website
    components.html("""
    <html>
    <style>
    .twitter {
  color: sky-blue;}
  
    .youtube{
    color: red;}
    </style>
    <body>
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
    
    <!-- using class to modify the color-->
    
    <h3 style="color:white">Twitter</h3> 
     <a class="twitter" href="https://twitter.com" target="blank">
        <ion-icon name="logo-twitter"></ion-icon> </a>
        
    <h3 style="color:white">YouTube</h3>
    <a class="youtube" href="https://youtube.com" target="blank">
       <ion-icon name="logo-youtube"></ion-icon></a>
    </body>
    </html>""")




