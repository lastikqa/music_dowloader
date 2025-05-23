from pathlib import Path


class SearchField:
    def __init__(self, page, ft):
        self.ft = ft
        self.page = page
        self.search_field = None
        self.file_field = None
        self.track_field = None
        self.path = ""
    async def creating_track_field(self, e):
        if self.track_field:
            while len(self.page.controls) > 1:
                self.page.controls.pop()
            await self.track_field.create_track_field(e.control.value)

    async def setup_search_field(self):
        self.search_field = self.ft.TextField(
            label=r"Search your song",
            icon=self.ft.Icons.SEARCH,
            hint_text="Put your song or author here",
            on_submit=self.creating_track_field
        )
        self.page.clean()
        self.page.add(self.search_field)
        self.page.update()

    async def search_field_submit(self, e):
        if Path(e.control.value).exists():
            self.path = e.control.value
            self.track_field.path = self.path
            await self.setup_search_field()
        else:
            message = self.ft.Text("the path does not exists")
            while len(self.page.controls) > 1:
                self.page.controls.pop()
            self.page.add(message)
        self.page.update()

    async def setup_file_search_field(self):
        self.file_field = self.ft.TextField(
            label=r"Put the path where u want to save tracks",
            icon=self.ft.Icons.SEARCH,
            hint_text=r"like 'C:\Users\User\\Desktop\songs'",
            on_submit=self.search_field_submit
        )
        self.page.add(self.file_field)
        self.page.update()




