from newsapi import NewsApiClient
import pycountry as pc
import streamlit as st
import datetime


hideStyle=""" <style>
    header {visibility:hidden}
    footer {visibility: hidden}
    #MainMenu {visibility:visible}"""

st.markdown(hideStyle,unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# 3498DB
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-light" style="background-color: #B2EA14;">
  <a class="navbar-brand" href="https://share.streamlit.io/sandeep12-2021/stream-prac/main/app.py" target="_self">Home  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item ">
        <a class="nav-link" href="https://share.streamlit.io/sandeep12-2021/stream-prac/main/newApp.py" target="_self">News</a>
      </li>
      <li class="nav-item ">
        <a class="nav-link" href="#">Analysis <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8501" target="_self">Forecast</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# pass =#@Project123
key ="ef8a6ffb16594c56820310414dc5922d"

newsapi = NewsApiClient(api_key=key)

# category for the news
categoryList=['General','Business','Health','Technology','Science', 'Entertainment','Sports']
cat = st.sidebar.selectbox("Select the news category",options=categoryList)
st.sidebar.write("##")

newsCount=st.sidebar.selectbox("Select the number of news headlines",[5,10,15,20,25,30],index=3)

# name of the country in 2 digits
contryList= ['United Arab Emirates', 'Argentina', 'Austria', 'Australia', 'Belgium', 'Bulgaria', 'Brazil', 'Canada',
              'Switzerland', 'China', 'Colombia', 'Cuba', 'Czech Republic', 'Germany', 'Egypt', 'France',
              'Britain (UK)', 'Greece', 'Hong Kong', 'Hungary', 'Indonesia', 'Ireland', 'Israel', 'India',
              'Italy', 'Japan', 'Korea (South)', 'Lithuania', 'Latvia', 'Morocco', 'Mexico', 'Malaysia',
              'Nigeria', 'Netherlands', 'Norway', 'New Zealand', 'Philippines', 'Poland', 'Portugal', 'Romania',
              'Serbia', 'Russia', 'Saudi Arabia', 'Sweden', 'Singapore', 'Slovenia', 'Slovakia', 'Thailand',
              'Turkey', 'Taiwan', 'Ukraine', 'United States', 'Venezuela', 'South Africa']

st.sidebar.write("##")
contry = st.sidebar.selectbox("Select the country for headlines",options=contryList,index=23)
contName=pc.countries.get(name=contry).alpha_2

st.sidebar.write("##")
particularNews= st.sidebar.text_input("If any particular news type here")

if not particularNews:
    data = newsapi.get_top_headlines(category=cat.lower(), country=contName.lower(), language='en', page_size=newsCount)
else:
    data = newsapi.get_everything(q=particularNews, language='en',page_size=newsCount)


articles = data['articles']

for article in articles:
    st.header(article['title'])
    if article['author']:
        st.write('Author:', article['author'])
    st.write('Source:', article['source']['name'])
    try:
        st.image(article['urlToImage'])
    except Exception:
        pass
    loc = article['url']
    content= ('Read more clicking [here]({loc})'.format(loc=loc))
    st.markdown(content,unsafe_allow_html=True)

