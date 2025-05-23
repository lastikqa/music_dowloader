import flet as ft
from main_page import MainPage


async def main(page: ft.Page):
    main_page = MainPage(page, ft)
    await main_page.build()


ft.app(target=main)

