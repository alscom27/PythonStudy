import csv
import pprint

with open("movies.csv", "r") as file:
    reader = csv.reader(file)
    movies = list(reader)

for record in movies:
    genre = record[1]
    print(genre, end=" ")

# pprint.pprint(movies) # 개행을 해주는거같음..?
print(movies)
