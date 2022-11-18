This is a movie rating prediction engine. It uses the KNN (k-nearest neighbors)
algorithm with cosine similarity to find out the nearest neighbors (people with similar preference)
to a user and uses their rating to a movie to predict how that user might rate the movie.

The 3 main files that interact while the program runs are: 'user.py', 'predictor.py'
and 'simulation.py'. Of these, 'simulation.py' is the top layer that we launch.
It's like the class with the main method in java. We can make use of the other files by
importing them in other files.

When 'simulation.py' is launched, it randomly draws a user (one who watches and rates movies)
and a movie that user has already voted. Then it predicts what rating the user could have given
the movie and prints both the prediction and actual value for us to compare.

The 3 files mentioned above get the data they need from binary files stored in the same folder.
These binary files are serialized (pickled) objects that can be unpickled into lists(for some)
or maps(for others). These binary files contain data extracted from the raw csv files in the
'raw files' directory by using the scripts in the 'helper_files' directory. These scripts assume
the raw files are in the same directory as the scripts.

I got the raw data from Kaggle: https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database
it's a real life data collected from people watching and rating anime.

The two raw data files are highly truncated becuase the couldn't be pushed to github with their original sizes.
I put the truncated files here to demonstrate what their content looks like.
