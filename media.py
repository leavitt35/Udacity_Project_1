import webbrowser

class Movie():
    """This class provides a way to create Movie objects.
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_director, release_year):
        # Defines Movie Attributes
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = movie_director
        self.release_year = release_year

    def show_trailer(self):
        # Opens Web Browser to YouTube link
        webbrowser.open(self.trailer_youtube_url)
