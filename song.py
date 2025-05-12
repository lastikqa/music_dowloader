class Song:
    def __init__(self, *args):
        self.author = args[0]
        self.track_name = args[1]
        self.track_link = args[-1]
        self.track_bytes = None
        self.button = self.author + ' - ' + self.track_name
