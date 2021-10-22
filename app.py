



import pickle

import streamlit as st
import requests
import pandas as pd

#title write
st.title("create by Hira movie Recommender")

#model new movies

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
new_movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

#write function recommend return 5 type movie








def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=0d3807f1cb4c4bb4d2bc4b62efe3f0cf&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/" +poster_path
    return full_path


def recommend(movie):
    index=new_movies[new_movies['title']==movie].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distances[1:6]:
        movie_id = new_movies.iloc[i[0]].movie_id
        recommend_poster.append(fetch_poster(movie_id))
        recommend_movie.append(new_movies.iloc[i[0]].title)
    return recommend_movie,recommend_poster










Selected_movie_name = st.selectbox(
'How would you like to be contacted?',
new_movies['title'].values)








if st.button('Show Recommendation'):
    recommendation,poster= recommend(Selected_movie_name)
    # for i in recommendation:
    #     st.write(i)
    # 
    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
         st.text(recommendation[0])
         st.image(poster[0])
    with col2:
        st.text(recommendation[1])
        st.image(poster[1])
    with col3:
        st.text(recommendation[2])
        st.image(poster[2])
    with col4:
        st.text(recommendation[3])
        st.image(poster[3])
    with col5:
        st.text(recommendation[4])
        st.image(poster[4])

    
    