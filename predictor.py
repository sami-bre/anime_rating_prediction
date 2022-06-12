class Predictor:
    def __init__(self, subject):
        self.subject = subject
        self.similar_people = dict()   # a map from user_obj to proximity

    def train(self, user_list):
        """training means populating the similar_people map"""
        # we use a list of tuples like [(user_obj, proximity), (...)] and sort it with proximity
        user_proximity = []
        for user in user_list:
            # we're doing cosine
            dot_product = 0
            subject_magnitude = 0
            user_magnitude = 0
            for genre in user.genre_ratings:
                dot_product += self.subject.genre_ratings[genre] * user.genre_ratings[genre]
                subject_magnitude += self.subject.genre_ratings[genre]**2
                user_magnitude += user.genre_ratings[genre]**2
            proximity = dot_product/(subject_magnitude*user_magnitude)
            user_proximity.append((user, proximity))
        user_proximity.sort(key=lambda x : x[1])
        # add the 500 most similar people to self.similar_people
        for i in range(500):
            self.similar_people[user_proximity[i][0]] = user_proximity[i][1]

    def predict(self, movie_id):
        # we're doing weighted mean of the ratings given to the movie by the closest people.
        # the weight is the proximity of the person to the subject.
        total_sum = 0
        proximity_sum = 0
        users = 0   # a counter to tell us what number of users we're using for the prediction.
        for user in self.similar_people:
            # there might be similar people (to the subject) who haven't rated the movie so we do filering.
            if movie_id in user.movie_ratings:
                users += 1
                total_sum += user.movie_ratings[movie_id] * self.similar_people[user]
                proximity_sum += self.similar_people[user]
        print(f'doing prediction with {users} users')
        # this is the prediction for the rating of the subject on the movie
        # it's the weighted mean of the ratings of similar people on the movie.
        prediction = total_sum/proximity_sum
        return prediction
