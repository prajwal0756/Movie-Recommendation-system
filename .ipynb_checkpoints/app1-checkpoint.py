import pickle
import pandas as pd
import requests
import streamlit as st

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)


import os
import gdown

if not os.path.exists("movie_dict.pkl"):
    gdown.download(
    id="14Oedl_TN05k98Q4oR7UoAAtfBP_OBrFG",
    output="movie_dict.pkl",
    quiet=False
)

if not os.path.exists("similarity.pkl"):
   gdown.download(
    id="1yRa2rw9frcDNmth4wrDrXPAkEBc4a3w9",
    output="similarity.pkl",
    quiet=False
)

# -----------------------------
# Load Files
# -----------------------------
movies = pickle.load(open("movie_dict.pkl", "rb"))

# If pickle is dictionary convert to DataFrame
if isinstance(movies, dict):
    movies = pd.DataFrame(movies)

similarity = pickle.load(open("similarity.pkl", "rb"))

# -----------------------------
# Fetch Movie Poster
# -----------------------------
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"


def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

        response = requests.get(url)

        if response.status_code != 200:
            return "https://via.placeholder.com/300x450?text=No+Image"

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path is None:
            return "https://via.placeholder.com/300x450?text=No+Image"

        return f"https://image.tmdb.org/t/p/w500{poster_path}"

    except:
        return "https://via.placeholder.com/300x450?text=No+Image"


# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie):

    movie_index = movies[movies["title"] == movie]

    if movie_index.empty:
        return [], []

    movie_index = movie_index.index[0]

    distances = list(enumerate(similarity[movie_index]))

    distances = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )

    recommended_movies = []
    posters = []

    for i in distances[1:6]:

        movie_id = movies.iloc[i[0]]["movie_id"]

        recommended_movies.append(
            movies.iloc[i[0]]["title"]
        )

        posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, posters


# -----------------------------
# UI
# -----------------------------
st.title("🎬 Movie Recommendation System")

movie_list = movies["title"].tolist()

selected_movie = st.selectbox(
    "Choose a Movie",
    movie_list
)

if st.button("Recommend Movies"):

    names, posters = recommend(selected_movie)

    if len(names) == 0:
        st.error("Movie not found.")
    else:

        cols = st.columns(5)

        for col, name, poster in zip(cols, names, posters):

            with col:
                st.image(
                    poster,
                    use_container_width=True
                )
                st.caption(name)