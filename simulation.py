import pickle
from random import randint
from predictor import Predictor

with open('user_list', 'rb') as stream:
    user_list = pickle.load(stream)

# select a subject randomly
random_subject = user_list.pop(randint(0,8800)) # 8800 is nearly the length of the user_list.
#select a random movie that the subject has rated. selecting randomly from a dictionary needs some work ... 
random_movie_id = ''
end = randint(0, len(random_subject.movie_ratings))
counter = 0
for movie_id in random_subject.movie_ratings:
    counter += 1
    if counter == end:
        random_movie_id = movie_id

# create the predictor engine and give it a subject
engine = Predictor(random_subject)
# train the engine with the user_list
engine.train(user_list)
# time to hit the road :)
prediction_result = engine.predict(random_movie_id)

print("user_id: ", random_subject.user_id)
print("movie for prediction: ", random_movie_id)
print("actual rating by the user: ", random_subject.movie_ratings[random_movie_id])
print("prediction: ", prediction_result)

