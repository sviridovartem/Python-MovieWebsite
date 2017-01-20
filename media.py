import webbrowser

class Movie():
    def __init__(self, title, movie_storyline, poster_img, trailer_link):
        self.title = title
        self.movie_storyline = movie_storyline
        self.poster_img = poster_img
        self.trailer_link = trailer_link

    def show_trailer(self):
        webbrowser.open(self.trailer_link)