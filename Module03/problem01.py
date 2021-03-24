
from random import randint, seed

seed(1337)

# flight_length = 60
flight_length = randint(60,180)

# movie_lengths = [25,35]
movie_lengths = []
for i in range(20):
    movie_lengths.append(randint(60,90))

print(f"Flight length: {flight_length}\n Movie lengths: {movie_lengths}")

def get_movies(flight_length, movie_lengths):
    possibility = False
    if len(movie_lengths) > 1:
        for i in movie_lengths:
            for j in movie_lengths:
                if (i + j) == flight_length:
                    possibility = True
    return possibility

print(get_movies(flight_length, movie_lengths))
