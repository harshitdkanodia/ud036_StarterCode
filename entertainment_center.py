import movie
import fresh_tomatoes
import tmdb_repo
import sys

if len(sys.argv) > 1:
  # getting strategy if argument is supplied
  strategy = sys.argv[1]
else:
  # defaulting to offline if no argument supplied
  strategy = "offline"
print("getting movies from " + strategy + " repo")
# open webpage to display movies from TMDB
movies = tmdb_repo.get_movies(strategy)
# show movies
fresh_tomatoes.open_movies_page(movies)



