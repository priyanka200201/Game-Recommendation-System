import streamlit as st
import pickle
import pandas as pd

# Function to recommend games
def recommend(game):
    Game_index = games[games['Title'] == game].index[0]
    distances = similarity[Game_index]
    steam_games_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_games = []
    for i in steam_games_list:
        recommended_games.append(games.iloc[i[0]].Title)
    return recommended_games

# Load data
games_dict = pickle.load(open('games_dict.pkl', 'rb'))
games = pd.DataFrame(games_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set page title with game emoji
st.title('ProPlay Advisor 🎮')

# Add animation to title
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: scale(0.5);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    .stApp .title-wrapper {
        animation: fadeIn 1s;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set background color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Increase the size of the sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        width: 350px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Increase the size of the content area
st.markdown(
    """
    <style>
    .css-1tq79qb {
        max-width: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a sidebar for user inputs
selected_game_name = st.sidebar.selectbox('Enter a Game:', games['Title'].values)
recommend_button = st.sidebar.button('Recommend', help='Click to get recommendations')

# Main content area
col1, col2 = st.columns([2, 3])

# Display selected game
with col1:
    st.subheader('Selected Game:')
    if selected_game_name:
        st.write(f"<div class='selected-game'>{selected_game_name}</div>", unsafe_allow_html=True)

# Display recommended games
with col2:
    if recommend_button:
        recommendations = recommend(selected_game_name)
        st.subheader('Recommended Games:')
        for i, recommendation in enumerate(recommendations, start=1):
            st.write(f"<div class='recommended-game'>{i}. {recommendation}</div>", unsafe_allow_html=True)

# Add CSS styling for selected and recommended games
st.markdown(
    """
    <style>
    .selected-game {
        color: #32CD32; /* Light green */
        font-size: 25px;
        font-weight: bold;
        font-style: italic;
    }
    .recommended-game {
        color: #008080; /* Teal */
        font-size: 20px;
        font-weight: bold;
        font-style: italic;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)
