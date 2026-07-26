# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using Machine Learning that recommends similar movies based on user preferences. The application provides movie recommendations along with posters fetched dynamically using the TMDB API.

🌐 Live Demo: [(https://movietalk.streamlit.app)]

📂 Repository: [(https://github.com/prajwal0756/Movie-Recommendation-system.git)]


## 📌 Project Overview

Recommendation systems are widely used in platforms like Netflix, YouTube, and Amazon to personalize user experiences.

This project implements a **content-based recommendation system** where users select a movie, and the system recommends similar movies based on the similarity between movie features.

The complete system is deployed as an interactive Streamlit web application where users can search and explore movie recommendations.


## 🚀 Features

- 🎥 Search and select a movie
- 🤖 Machine Learning based recommendations
- 🔍 Content-based filtering approach
- 🎯 Provides top 5 similar movie recommendations
- 🖼️ Fetches movie posters dynamically using TMDB API
- 🌐 Interactive Streamlit dashboard
- ☁️ Deployed on Streamlit Cloud


## 🏗️ Project Workflow
Dataset <br>
|
↓
Data Cleaning & Preprocessing<br>
|
↓
Feature Engineering<br>
|
↓
Movie Feature Vector Creation<br>
|
↓
Similarity Calculation<br>
|
↓
Model Serialization (Pickle)<br>
|
↓
Streamlit Application<br>
|
↓
Cloud Deployment



## 🧠 Machine Learning Approach

### Content-Based Filtering

This project uses a content-based recommendation approach.

The system recommends movies by calculating similarity between movies based on their features.

When a user selects a movie:

1. The system finds the selected movie index.
2. Calculates similarity scores with other movies.
3. Sorts movies based on similarity score.
4. Returns the top recommended movies.


## ⚙️ Technologies Used

### Programming Language

- Python


### Data Processing

- Pandas
- NumPy


### Machine Learning

- Scikit-learn
- Cosine Similarity


### Application Development

- Streamlit


### API Integration

- TMDB API


### Deployment

- Streamlit Cloud


## 📂 Project Structure
Movie-Recommendation-System/<br>
│
├── app.py<br>
├── requirements.txt<br>
│
├── movie_dict.pkl<br>
├── similarity.pkl<br>
│
├── tmdb dataset/<br>
│
└── README.md<br>



## 📊 Dataset

The project uses TMDB movie dataset containing information about movies including:

- Movie title
- Movie ID
- Genres
- Keywords
- Cast
- Crew
- Overview


## 🔥 How It Works

Example:

Input:
Interstellar

Output:
Recommended Movies:<br>
Inception<br>
The Martian<br>
Gravity<br>
Arrival<br>
Blade Runner 2049


## 💻 Installation and Usage

Clone the repository:

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git

Install dependencies:
pip install -r requirements.txt

Run the application:
streamlit run app.py
```




##  📈 Future Improvements

* Add user-based recommendation
* Add hybrid recommendation system
* Add user ratings
* Add authentication
* Deploy using FastAPI + React architecture
* Improve recommendation accuracy using deep learning embeddings

---

## 👨‍💻 Author

**Prajwal Subedi**  
Data Science Enthusiast | Machine Learning | AI

* **GitHub:** [prajwal0756](https://github.com/prajwal0756)
* **LinkedIn:** [Prajwal Subedi](https://www.linkedin.com/in/prajwal-subedi)