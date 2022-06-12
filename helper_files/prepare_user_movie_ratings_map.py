import pickle

user_ratings = dict()
mov_map = dict()

with open('mov_map', 'rb') as mov_map_file:
    mov_map = pickle.load(mov_map_file)


with open('rating.csv', 'r') as raw_file:
    with open('user_movie_ratings_map', 'wb') as pickle_file:
        line = raw_file.readline()  # this is the heading row so do readline again
        line = raw_file.readline()
        counter = 0
        while line != '':
            entry_as_array = line.split(',')
            user_id = entry_as_array[0]
            movie_id = entry_as_array[1]
            user_movie_rating = entry_as_array[2]
            user_movie_rating = int(user_movie_rating)
            if user_movie_rating != -1 and movie_id in mov_map:
                print(entry_as_array)
                # ratings.append(entry_as_array)
                if user_id not in user_ratings:
                    user_ratings[user_id] = dict()
                user_ratings[user_id][movie_id] = user_movie_rating
            line = raw_file.readline()
            # break it once you get enough data
            counter += 1
            if counter > 1000000:
                break
        pickle.dump(user_ratings, pickle_file)