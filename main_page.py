import flet as ft
from parser import MusicParser

def main(page : ft.Page):
    parser = MusicParser()
    page.title = "Music Downloader"


    def parsing(e):
        container = ft.Container
        parser.browser_search(user_search=user_search.value)
        music_dict = parser.browser_get()
        musics = [(ft.Row([ft.IconButton(ft.icons.PLAY_CIRCLE_OUTLINED), ft.IconButton(ft.icons.DOWNLOADING),
                             ft.Text(f"{i}")])) for i in music_dict]

        page.update()
        cl.controls.extend(musics)
        
        page.add(container(cl, border=ft.border.all(1)))

        page.update()

    user_search = ft.TextField(label="Search your song", icon=ft.icons.SEARCH, on_submit=parsing)
    page.add(user_search)



    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            track_color={
                ft.ControlState.HOVERED: ft.colors.AMBER,
                ft.ControlState.DEFAULT: ft.colors.TRANSPARENT,
            },
            track_visibility=True,
            #track_border_color=ft.colors.BLUE,
            thumb_visibility=True,
            thumb_color={
                ft.ControlState.HOVERED: ft.colors.RED,
                ft.ControlState.DEFAULT: ft.colors.GREY_300,
            },
            thickness=30,
            radius=15,
            main_axis_margin=1,
            cross_axis_margin=3,
            interactive=True,
        )
    )

    cl = ft.Column(
        spacing=10,
        height=400,
        width=float("inf"),
        scroll=ft.ScrollMode.ALWAYS,
    )






ft.app(target=main)
