import pickle

# this is a list of all the genres in the data, extracted using the 
# 'extract_genre_efficinet.py file
all_genres = []

# a map from movie_id to the list of genres of the movie, extracted from the 
# data using the 'prepare_mov_map.py' file
mov_map = {}

with open('all_genres', 'br') as stream:
    all_genres = pickle.load(stream)

with open('mov_map', 'br') as stream:
    mov_map = pickle.load(stream)


class User:
    def __init__(self, user_id, user_movie_ratings):
        self.user_id = user_id
        self.movie_ratings = user_movie_ratings     # map from movie_id -> movie_rating
        self.genre_ratings = {all_genres[i]:0 for i in range(len(all_genres))}   # map from genre -> genre_rating
        # now populate the genre_rating map
        for movie_id in self.movie_ratings:
            for genre in mov_map[movie_id]:
                self.genre_ratings[genre] += self.movie_ratings[movie_id]
