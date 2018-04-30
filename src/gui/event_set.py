import vlc


class EventSet(set):
    mp: vlc.MediaPlayer = None

    def __init__(self, media_path: str):
        self.mp = vlc.MediaPlayer(media_path)
