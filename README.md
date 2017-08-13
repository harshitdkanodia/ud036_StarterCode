# My Favorite Movies
A python app that opens a webpage containing information about my favorite movies.

## Instruction to run
* [Install python](https://www.python.org/downloads/release/python-2713/)
* Clone this project
* Navigate to the directory where the project is cloned with terminal / command prompt
* Type in `python entertainment_center.py` and hit enter/return
* See a list of my favorite movies!
* **BONUS**: type in `python entertainment_center.py online` to get a list of popular movies


## About the project

The project displays a list of my favorite movies.


## tmdb_repo.py

You may import this and use it in any file to get a list of Movie objects.
### Methods
* **get_movies(strategy)** : strategy can be online / offline
* **get_online_list()** : gets a list of top 5 popular movies from tmdb
* **et_offline_list()** : gets a list of my top 5 favorite movies
* **convert_to_movie_obj([type='Array'  tmdb_array])** : helper method to convert tmdb json to Movie

## entertainment_cetner.py

This file is responsible for accessing tmdb_repo and show online / offline suggestions based on arguments passed via CLI

