class Video(object):
    '''This class represent Video
    Attributes:
            title (str): store the video title
            starring(list): store person who involved in the video
            year(string): year of the video release

    '''
    def __init__(self,title,starring,year):
        self.title = title
        self.starring = starring
    	self.year = year


class Movie(Video):
    '''This class represent Movie and child from class Video
    Attribute:
            plot(string): store the movie plot
            poster_image_url(string): store the movie poster url
            trailer_youtube_url: store the movie youtube url
            category(string): store the genre of the movie
    '''
    def __init__(self,title,plot,starring,poster,trailer,category,year):
        super(Movie, self).__init__(title,starring,year)
    	self.poster_image_url = poster
    	self.trailer_youtube_url = trailer
    	self.category = category
    	self.plot       = plot

#this function return a string that contains actor names
    def getActor(self,starring):
        actors = starring
    	string = ""

    	for actor in actors:
    	    string += actor
    	return string
