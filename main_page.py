import flet as ft
from search_field import SearchField
from track_field import TrackField
from player_buttons import PlayerButtons
from music_player import MusicPlayer

class MainPage:
    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.player = MusicPlayer()
        self.search_field = SearchField(self.page, self.ft)
        self.track_field = TrackField(self.page, self.ft)
        self.search_field.track_field = self.track_field
        self.player_buttons = PlayerButtons(self.page, self.ft)
        self.track_field.player_buttons = self.player_buttons
        self.track_field.player = self.player
        self.player_buttons.player = self.player

    async def build(self):
        await self.search_field.setup_file_search_field()






