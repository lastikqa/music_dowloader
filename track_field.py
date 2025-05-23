from playwright.async_api import async_playwright
from parser import MusicParser

class TrackField:
    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.track_field = None
        self.player_buttons = None
        self.path = ""
        self.player = None
        self.parser = MusicParser()

    async def click_play_track(self,e):
        self.player.new_track(e.control.data)
        self.player_buttons.track = e.control.data
        await self.player.play()
        while len(self.page.controls) >2:
            self.page.controls.pop()
        self.player_buttons.build_player_buttons()

    async def click_download_button(self, e):

        await self.parser.music_dict[e.control.data].writing_song()

    async def create_track_field(self, user_search):
        self.track_field = self.ft.Column(
            spacing=1,
            height=550,
            width=float("inf"),
            scroll=self.ft.ScrollMode.ALWAYS,
        )

        async with async_playwright() as playwright:
            await self.parser.init_browser(playwright, user_search, self.path)


        music_rows = [(self.ft.Row([self.ft.IconButton(self.ft.Icons.PLAY_CIRCLE_OUTLINED, data=i, on_click = self.click_play_track),
                                    self.ft.IconButton(self.ft.Icons.DOWNLOADING, data=i, on_click=self.click_download_button),
                       self.ft.Text(f"{i}")])) for i in self.parser.music_list]
        self.player.music_dict = self.parser.music_dict
        self.player_buttons.track = self.parser.music_list[0]
        self.track_field.controls.extend(music_rows)
        self.page.add(self.track_field)
        self.player_buttons.build_player_buttons()
        self.page.update()