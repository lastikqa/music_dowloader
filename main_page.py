import flet as ft
from parser import MusicParser


def main(page: ft.Page):

    page.title = "Music Downloader"

    def parsing(e):

        cl = ft.Column(
            spacing=1,
            height=550,
            width=float("inf"),
            scroll=ft.ScrollMode.ALWAYS,
        )
        parser = MusicParser()
        parser.browser_search(user_search=user_search.value)
        parser.page_walking()

        musics = [(ft.Row([ft.IconButton(ft.icons.PLAY_CIRCLE_OUTLINED),
                           ft.IconButton(ft.icons.DOWNLOADING, data=i, on_click=click),
                  ft.Text(f"{i}")])) for i in parser.music_dict]

        cl.controls.extend(musics)

        page.add(cl)

        page.update()

    user_search = ft.TextField(label="Search your song", icon=ft.icons.SEARCH, on_submit=parsing)
    page.add(user_search)


ft.app(target=main)
