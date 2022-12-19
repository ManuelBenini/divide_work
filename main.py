
from getDbData import GetDbData

all_Actors = GetDbData.getAllActors()
all_films = GetDbData.getAllFilms()

for actor in all_Actors:
    print(actor)

for film in all_films:
    print(film)