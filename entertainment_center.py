import movie
import fresh_tomatoes
delhi_belly = movie.Movie("Delhi Belly"
							,"A man faces life"
							,'https://i2.wp.com/bollywoodcopy.com/cron/posters/14.jpg'
							,"https://www.youtube.com/watch?v=iSVhPXvFDw8")
avengers = movie.Movie("Avengers : Age of ultron"
							,"The avengers fight an AI got out of hand"
							,'https://static.comicvine.com/uploads/scale_small/11/113509/4413258-ultron.jpg'
							,"https://www.youtube.com/watch?v=rD8lWtcgeyg")
movies = [delhi_belly,avengers]
fresh_tomatoes.open_movies_page(movies)