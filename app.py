import streamlit as st

# =====================================================================
# 📚 MOVIE DATA ENGINE (50 Blockbuster Movies - Verified Genres)
# =====================================================================
movie_database = [
    # --- ACTION ---
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0},
    {"title": "Inception", "genre": "Action", "rating": 8.8},
    {"title": "The Matrix", "genre": "Action", "rating": 8.7},
    {"title": "Gladiator", "genre": "Action", "rating": 8.5},
    {"title": "Avengers: Endgame", "genre": "Action", "rating": 8.4},
    {"title": "Spider-Man: Into the Spider-Verse", "genre": "Action", "rating": 8.4},
    {"title": "Mad Max: Fury Road", "genre": "Action", "rating": 8.1},
    {"title": "Logan", "genre": "Action", "rating": 8.1},
    {"title": "Skyfall", "genre": "Action", "rating": 7.8},
    {"title": "John Wick", "genre": "Action", "rating": 7.4},

    # --- SCI-FI ---
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6},
    {"title": "Spirited Away", "genre": "Sci-Fi", "rating": 8.6},
    {"title": "Star Wars: A New Hope", "genre": "Sci-Fi", "rating": 8.6},
    {"title": "The Prestige", "genre": "Sci-Fi", "rating": 8.5},
    {"title": "Back to the Future", "genre": "Sci-Fi", "rating": 8.5},
    {"title": "Terminator 2: Judgment Day", "genre": "Sci-Fi", "rating": 8.6},
    {"title": "Blade Runner 2049", "genre": "Sci-Fi", "rating": 8.0},
    {"title": "Dune", "genre": "Sci-Fi", "rating": 8.0},
    {"title": "Arrival", "genre": "Sci-Fi", "rating": 7.9},
    {"title": "Avatar", "genre": "Sci-Fi", "rating": 7.8},

    # --- COMEDY ---
    {"title": "The Truman Show", "genre": "Comedy", "rating": 8.2},
    {"title": "The Grand Budapest Hotel", "genre": "Comedy", "rating": 8.1},
    {"title": "Deadpool", "genre": "Comedy", "rating": 8.0},
    {"title": "Knives Out", "genre": "Comedy", "rating": 7.9},
    {"title": "The Hangover", "genre": "Comedy", "rating": 7.7},
    {"title": "Superbad", "genre": "Comedy", "rating": 7.6},
    {"title": "Zombieland", "genre": "Comedy", "rating": 7.5},
    {"title": "Borat", "genre": "Comedy", "rating": 7.4},
    {"title": "Mean Girls", "genre": "Comedy", "rating": 7.1},
    {"title": "Free Guy", "genre": "Comedy", "rating": 7.1},

    # --- HORROR & THRILLER ---
    {"title": "Parasite", "genre": "Thriller/Horror", "rating": 8.6},
    {"title": "Psycho", "genre": "Thriller/Horror", "rating": 8.5},
    {"title": "Alien", "genre": "Thriller/Horror", "rating": 8.5},
    {"title": "The Shining", "genre": "Thriller/Horror", "rating": 8.4},
    {"title": "Get Out", "genre": "Thriller/Horror", "rating": 7.7},
    {"title": "The Conjuring", "genre": "Thriller/Horror", "rating": 7.5},
    {"title": "A Quiet Place", "genre": "Thriller/Horror", "rating": 7.5},
    {"title": "It", "genre": "Thriller/Horror", "rating": 7.3},
    {"title": "Hereditary", "genre": "Thriller/Horror", "rating": 7.3},
    {"title": "Insidious", "genre": "Thriller/Horror", "rating": 6.8},

    # --- ROMANCE ---
    {"title": "Forrest Gump", "genre": "Romance", "rating": 8.8},
    {"title": "Before Sunrise", "genre": "Romance", "rating": 8.1},
    {"title": "La La Land", "genre": "Romance", "rating": 8.0},
    {"title": "Titanic", "genre": "Romance", "rating": 7.9},
    {"title": "The Notebook", "genre": "Romance", "rating": 7.8},
    {"title": "About Time", "genre": "Romance", "rating": 7.8},
    {"title": "Pride & Prejudice", "genre": "Romance", "rating": 7.8},
    {"title": "500 Days of Summer", "genre": "Romance", "rating": 7.7},
    {"title": "A Star Is Born", "genre": "Romance", "rating": 7.6},
    {"title": "Crazy Rich Asians", "genre": "Romance", "rating": 6.9}
]

# =====================================================================
# 🎨 STREAMLIT INTERFACE DESIGN
# =====================================================================

st.set_page_config(page_title="CineMatch Recommender", page_icon="🎬", layout="centered")

st.title("🎬 CineMatch AI")
st.subheader("Simple & Elegant Genre-Based Movie Recommender")
st.write("Find the highest-rated blockbusters instantly across major cinematic categories.")
st.markdown("---")

# Sidebar setup for engine stats
st.sidebar.header("📊 Engine Metadata")
st.sidebar.write(f"**Total Indexed Catalog:** {len(movie_database)} titles")
st.sidebar.markdown("---")
st.sidebar.info("💡 **Core Logic:** Knowledge-Based Filtering System sorting filtered arrays by rating intensity.")

# Dropdown Selection Menu for Genres
genres_available = ["Action", "Sci-Fi", "Comedy", "Thriller/Horror", "Romance"]
selected_genre = st.selectbox("👉 Select your preferred Movie Genre:", genres_available)

if st.button("🍿 Generate Recommendations", type="primary"):
    
    st.write("") 
    st.subheader(f"🎯 Top {selected_genre} Movies For You:")

    # 1. SORT MECHANISM
    sorted_movies = sorted(movie_database, key=lambda x: x["rating"], reverse=True)

    # 2. FILTER MECHANISM
    rank = 1
    for movie in sorted_movies:
        if movie["genre"] == selected_genre:
            with st.container():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f"#### **{rank}. {movie['title']}**")
                with col2:
                    st.success(f"⭐ {movie['rating']}/10")
                st.markdown("---")
            rank += 1
