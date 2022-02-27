# here we download pycountry pacakge to convert the country codes in two alphabet form which are
# basically the country code

import streamlit as st
import requests as re
import pycountry as py
# from api import apiKEY

myKey= 'f68509a72e2b4dddaaf2ba057b5d994a'
st.title('News App')
# now for dividing whole screen into two parts we can use st.columns
col1,col2=st.columns([3,1]) # 75,25

with col1:
    user=st.text_input('Enter country name')

with  col2:
    st.radio('Choose one  category',('Technology','Sports'))
    btn= st.button('Enter')

if btn:
    country=py.countries.get(name=user).alpha_2
    url=f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={myKey}"
    r = re.get(url)
    r=r.json()# here we have everything all the components of news
    articles = r['articles']

    for article in articles:
        st.header(article['title'])
        if article['author']:
            st.write('Author:',article['author'])
        st.write('Source:',article['source']['name'])
        try:
            st.image(article['urlToImage'])
        except Exception:
            pass






