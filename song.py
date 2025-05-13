import aiohttp

class Song:
    path = ""
    def __init__(self, *args):
        self.author = args[0]
        self.track_name = args[1]
        self.track_link = args[-1]
        self.track_bytes = None
        self.button_name = self.author + ' - ' + self.track_name


    async def download_song(self):
        """the function downloads track by using a link."""

        async with aiohttp.ClientSession() as session:
            async with session.get(self.track_link) as response:
                self.track_bytes = await response.read()

    async def writing_song(self):
        """the function writes song on your computer disk"""
        await self.download_song()
        with open(self.path + "/" + self.button_name +".mp3", "wb") as my_file:
            my_file.write(self.track_bytes)

