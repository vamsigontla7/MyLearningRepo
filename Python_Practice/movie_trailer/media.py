import webbrowser


class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]


    def __init__(
        self, movie_title, movie_description, movie_poster, movie_trailer
    ):
        self.title = movie_title
        self.storyline = movie_description
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer


    def show_trailer(self1):
        webbrowser.open(self1.trailer)
