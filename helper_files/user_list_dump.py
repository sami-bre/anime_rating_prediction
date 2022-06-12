"""this file creates the massive user_list we'll be using later and dumps it 
to a file named ... well, 'user_list'"""

import pickle
import user

# a big list caontaining all user objects
user_list = []

with open('user_movie_ratings_map', 'rb') as stream:
    # this is a map from user_id -> (map from movie_id -> movie_taring)
    user_movie_ratings_map = pickle.load(stream)

for user_id in user_movie_ratings_map:
    user_obj = user.User(user_id, user_movie_ratings_map[user_id])
    user_list.append(user_obj)
    print(user_obj)

with open('user_list', 'bw') as stream:
    pickle.dump(user_list, stream)

