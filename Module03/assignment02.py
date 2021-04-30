
from random import randint
import random

# You've built an inflight entertainment system with on-demand movie streaming.
# Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane usually lands before they can see the ending.
# So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.
# Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
# Try to solve with Dictionary!
# When building your function:
# Assume your users will watch exactly two movies
# Don't make your users watch the same movie twice
# Optimize for runtime over memory

print("\n-----===== Start =====-----\n")

def get_movies(flight_length, movie_lengths):
    possibility = False
    movies = set()
    for i in movie_lengths:
        if i < flight_length:
            if i in movies:
                possibility = True
            else:
                movies.add(flight_length - i)
    return possibility

flight_length = randint(120,240)

movie_lengths = []
for i in range(randint(2,20)):
    movie_lengths.append(randint(60,120))

print(f"Flight length: {flight_length} minutes")
print(f"Movie lengths: {movie_lengths}")

print(f"Can you watch two movies? {'yes' if get_movies(flight_length, movie_lengths) else 'No'}")

print("\n-----===== End =====-----")
