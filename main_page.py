import flet as ft


def main(page : ft.Page):
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            track_color={
                ft.ControlState.HOVERED: ft.colors.AMBER,
                ft.ControlState.DEFAULT: ft.colors.TRANSPARENT,
            },
            track_visibility=True,
            track_border_color=ft.colors.BLUE,
            thumb_visibility=True,
            thumb_color={
                ft.ControlState.HOVERED: ft.colors.RED,
                ft.ControlState.DEFAULT: ft.colors.GREY_300,
            },
            thickness=30,
            radius=15,
            main_axis_margin=5,
            cross_axis_margin=10,
            interactive=True,
        )
    )

    cl = ft.Column(
        spacing=10,
        height=400,
        width=float("inf"),
        scroll=ft.ScrollMode.ALWAYS,
    )
    page.add(ft.TextField("Search your song"), ft.IconButton(ft.icons.SEARCH))

    page.title = "Music Downloader"

    n = ft.Row([ft.IconButton(ft.icons.PLAY_CIRCLE_OUTLINED),ft.IconButton(ft.icons.DOWNLOADING),ft.Text("Music")])
    m = []
    for i in range(25):
        m.append(n)
    #page.add(*m)

    for i in m:
        cl.controls.append(i)

    page.add(ft.Container(cl, border=ft.border.all(1)))

ft.app(target=main)
