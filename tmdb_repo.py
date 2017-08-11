import json
import movie
import urllib

# defining dependencies for api consumption
api_key = '6cf19aac43d3d3a2c70dc6d54face94f'
api_url = "https://api.themoviedb.org/3"
poster_image_url = "https://image.tmdb.org/t/p/w500"

# function to get youtube trailer for movie
def get_youtube_trailer(movie_id):
	data = urllib.urlopen(api_url + "/movie/" + str(movie_id) + "/videos?api_key=6cf19aac43d3d3a2c70dc6d54face94f")
	youtube_trailers = json.load(data)
	# getting first result from and fetching key
	youtube_trailer_key = youtube_trailers["results"][0]["key"]
	return "https://www.youtube.com/watch?v="+youtube_trailer_key

# helper method to convert tmdb json to our Movie
def convert_to_movie_obj(tmdb_array):
	return movie.Movie(tmdb_array["title"],
						tmdb_array["overview"],
						poster_image_url + tmdb_array["poster_path"],
						get_youtube_trailer(tmdb_array["id"]))

# get movies from offline / online
def get_movies(strategy):
	if "online" in strategy:
		return get_online_list()
	else :
		return get_offline_list()

# get 5 movies from tmdb
def get_online_list():
	data = urllib.urlopen(api_url + "/discover/movie?sort_by=popularity.desc&append_to_response=videos&api_key=6cf19aac43d3d3a2c70dc6d54face94f")
	movies = json.load(data)
	movie_list = []
	for movie in movies["results"][:5]:
		movie_list.append(convert_to_movie_obj(movie))
	return movie_list

# get offline list of movies
def get_offline_list():
    # Movie 1
    delhi_belly = movie.Movie("Delhi Belly", "A man faces life",
                              'http://contact25.com/uploads/7_16764.jpg',
                              "https://www.youtube.com/watch?v=iSVhPXvFDw8")
    # Movie 2
    avengers = movie.Movie("Avengers : Age of ultron",
                           "The avengers fight a powerful AI who want's to finish humanity",
                           'https://static.comicvine.com/uploads/scale_small/11/113509/4413258-ultron.jpg',
                           "https://www.youtube.com/watch?v=rD8lWtcgeyg")

    # Movie 3
    war_for_the_planet = movie.Movie("War for the Planet of the Apes",
                                     "Caesar (Andy Serkis) and his apes are forced into a deadly conflict with an army of humans led by a ruthless colonel (Woody Harrelson). " +
                                     "After the apes suffer unimaginable losses, Caesar wrestles with his darker instincts and begins his own mythic quest to avenge his kind." +
                                     "As the journey finally brings them face to face, Caesar and the colonel are pitted against each other in an epic battle that will determine " +
                                     "the fate of both of their species and the future of the planet.",
                                     'http://cdn.collider.com/wp-content/uploads/2016/12/war-for-the-planet-of-the-apes-poster.jpg',
                                     "https://www.youtube.com/watch?v=qxjPjPzQ1iU")
    # Movie 4
    the_man_who_knew_infinity = movie.Movie("The man who knew infinity",
                                            "The story of the life and academic career of the pioneer Indian mathematician, Srinivasa Ramanujan, and his friendship with his mentor, Professor G.H. Hardy.",
                                            'http://www.newdvdreleasedates.com/images/posters/large/the-man-who-knew-infinity-2015-04.jpg',
                                            "https://www.youtube.com/watch?v=oXGm9Vlfx4w")
    # Movie 5
    wonder_woman = movie.Movie("Wonder Woman",
                               "Before she was Wonder Woman (Gal Gadot), she was Diana, princess of the Amazons, trained to be an unconquerable warrior. " +
                               "Raised on a sheltered island paradise, Diana meets an American pilot (Chris Pine) who tells her about the massive conflict that's raging in the outside world. " +
                               "Convinced that she can stop the threat, Diana leaves her home for the first time. Fighting alongside men in a war to end all wars, " +
                               "she finally discovers her full powers and true destiny.",
                               'http://vignette3.wikia.nocookie.net/dccu/images/8/8e/Wonder_Woman_first_look_promo.jpg/revision/latest?cb=20160708135809',
                               "https://www.youtube.com/watch?v=oXGm9Vlfx4w")
    return [delhi_belly,
			avengers,
			war_for_the_planet,
			the_man_who_knew_infinity,
			wonder_woman]