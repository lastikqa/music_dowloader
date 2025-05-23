import aiohttp
import sounddevice as sd


class Song:
    def __init__(self, author,track_name,track_link, path=""):
        self.author = author
        self.track_name = track_name
        self.track_link = track_link
        self._track_bytes = None  # private attribute
        self.button_name = self.author + ' - ' + self.track_name
        self.duration = None
        self.path = path


    async def download_song(self):
        """the function downloads track by using a link."""
        if self._track_bytes is None:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.track_link) as response:
                    self._track_bytes = await response.read()

    async def get_track_bytes(self):
        """Get track bytes, downloading if necessary."""
        if self._track_bytes is None:
            await self.download_song()
        return self._track_bytes

    async def writing_song(self):
        """the function writes song on your computer disk"""
        await self.download_song()
        with open(self.path + fr"/{self.button_name}.mp3", "wb") as my_file:
            my_file.write(self._track_bytes)






