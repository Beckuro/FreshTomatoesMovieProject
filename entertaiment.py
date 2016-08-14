import fresh_tomatoes
import media
import json
import urllib2
import requests


#function that return list of movie
def list_of_movies():

	#create action movie
	FBHFT = create_movie('tt3183660',"act",
						 "https://www.youtube.com/watch?v=YdgQj7xcDJo")
	TDK	  =	create_movie('tt0468569',"act",
						 "https://www.youtube.com/watch?v=EXeTwQWrcwY")
	OB    = create_movie('tt0364569',"act",
						 "https://www.youtube.com/watch?v=2HkjrJ6IK5E")
	TR    = create_movie('tt1899353',"act",
						 "https://www.youtube.com/watch?v=7KJ0N7ik3yI")

	#create comedy movie
	THTG  = create_movie('tt0371724',"com",
						 "https://www.youtube.com/watch?v=eLdiWe_HJv4")
	DAD   = create_movie('tt0109686',"com",
						 "https://www.youtube.com/watch?v=l13yPhimE3o")
	TH    = create_movie('tt1119646',"com",
						 "https://www.youtube.com/watch?v=vhFVZsk3XEs")
	TW    = create_movie('tt3152624',"com",
						 "https://www.youtube.com/watch?v=2MxnhBPoIx4")

	#create drama movie
	BH    = create_movie('tt1065073',"dra",
						 "https://www.youtube.com/watch?v=Ys-mbHXyWX4")
	TP    = create_movie('tt0482571',"dra",
						 "https://www.youtube.com/watch?v=o4gHCmTQDVI")
	TSR   = create_movie('tt0111161',"dra",
						 "https://www.youtube.com/watch?v=6hB3S9bIaco")
	TGF   = create_movie('tt0068646',"dra",
						 "https://www.youtube.com/watch?v=sY1S34973zA")

	movies = [FBHFT,TDK,OB,TR,THTG,DAD,TH,TW,BH,TP,TSR,TGF]
	return movies


#function to create movie
def create_movie(id,genre,trailer):
	respons = urllib2.urlopen('http://www.omdbapi.com/?i='+id+'&plot=short&r=json')
	data 	 = json.load(respons)
	movie 	 = media.Movie(data['Title'],data['Plot'],data['Actors'],
						   data['Poster'], trailer, genre, data['Year'])

	return movie
   
#this function is to create a html page
def create_page():
	movies = list_of_movies()
	action = []			#list of action movie
	drama = []			#list of drama movie
	comedy = []			#list of comedy movie

	#sort movie based on their category
	for movie in movies:
		if movie.category == "act":
			action.append(movie)
		elif movie.category == "com":
			comedy.append(movie)
		else:
			drama.append(movie)

	fresh_tomatoes.open_movies_page(action,comedy,drama)

create_page()